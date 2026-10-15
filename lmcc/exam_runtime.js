var ExamRuntime = (function () {
  var STORAGE_VERSION = 2;
  var STORAGE_KEY = "lmcc_exam_state_v2";

  function djb2Hex(text) {
    var h = 5381;
    for (var i = 0; i < text.length; i++) {
      h = (((h << 5) + h + text.charCodeAt(i)) >>> 0);
    }
    var hex = h.toString(16);
    while (hex.length < 8) hex = "0" + hex;
    return hex;
  }

  function questionFingerprint(data) {
    var practice = (data && data.practice_bank) || {};
    var parts = ["practice-revision\t" + (practice.single_revision || "")];
    var mods = (data && data.modules) || [];
    for (var i = 0; i < mods.length; i++) {
      var qs = mods[i].questions || [];
      for (var j = 0; j < qs.length; j++) {
        var q = qs[j];
        parts.push([
          mods[i].id || "", q.num, q.type, q.answer, q.body,
          (q.options || []).join("\u241f"), q.explanation || "", q.revision || ""
        ].join("\t"));
      }
    }
    var mock = data && data.mock_exam;
    var mqs = Array.isArray(mock) ? mock : ((mock && mock.questions) || []);
    for (var k = 0; k < mqs.length; k++) {
      var mq = mqs[k];
      parts.push([
        "mock", mq.num, mq.type, mq.answer, mq.body,
        (mq.options || []).join("\u241f"), mq.explanation || "", mq.revision || ""
      ].join("\t"));
    }
    return djb2Hex(parts.join("\n"));
  }

  function normalizeAnswer(value) {
    var letters = String(value == null ? "" : value).toUpperCase().match(/[A-D]/g) || [];
    return Array.from(new Set(letters)).sort().join("");
  }

  function persistTimer(opts) {
    opts = opts || {};
    var now = opts.now;
    var remaining = Math.max(0, Number(opts.remaining) || 0);
    var running = !!opts.running;
    var submitted = !!opts.submitted;
    if (submitted) {
      return { submitted: true, running: false, remaining: 0, deadline: null };
    }
    if (running) {
      return { submitted: false, running: true, remaining: remaining, deadline: now + remaining };
    }
    return { submitted: false, running: false, remaining: remaining, deadline: null, paused_at: now };
  }

  function restoreTimer(saved, now, duration) {
    if (!saved) {
      return { remaining: duration, running: false, submitted: false, deadline: null };
    }
    if (saved.submitted) {
      return { remaining: 0, running: false, submitted: true, deadline: null };
    }
    if (saved.running && saved.deadline != null) {
      var rem = Math.max(0, Math.floor(saved.deadline - now));
      return { remaining: rem, running: rem > 0, submitted: false, deadline: saved.deadline };
    }
    var paused = Math.max(0, Number(saved.remaining != null ? saved.remaining : duration));
    return { remaining: paused, running: false, submitted: false, deadline: null };
  }

  function onLeaveMock(timer, now) {
    var rem = timer && timer.remaining != null ? timer.remaining : 0;
    if (timer && timer.running && timer.deadline != null) {
      rem = Math.max(0, Math.floor(timer.deadline - now));
    }
    return persistTimer({
      now: now,
      remaining: rem,
      running: false,
      submitted: !!(timer && timer.submitted)
    });
  }

  function onEnterMock(timer, now, duration) {
    var restored = restoreTimer(timer, now, duration);
    if (restored.submitted) {
      restored.autosubmit = false;
      return restored;
    }
    if (restored.remaining <= 0) {
      return { remaining: 0, running: false, submitted: false, deadline: null, autosubmit: true };
    }
    var persisted = persistTimer({
      now: now,
      remaining: restored.remaining,
      running: true,
      submitted: false
    });
    restored.running = true;
    restored.deadline = persisted.deadline;
    restored.autosubmit = false;
    return restored;
  }

  function onTick(opts) {
    opts = opts || {};
    var nextRem = Math.max(0, Number(opts.remaining) - 1);
    var autosubmit = opts.mode === "mock" && nextRem <= 0 && !opts.submitted;
    var keepTicking = opts.mode === "mock" && nextRem > 0 && !opts.submitted;
    return { remaining: nextRem, autosubmit: autosubmit, keep_ticking: keepTicking };
  }

  function shouldAutosubmit(opts) {
    opts = opts || {};
    return opts.mode === "mock" && Number(opts.remaining) <= 0 && !opts.submitted;
  }

  function shouldReuseSavedState(saved, currentFp, currentVersion) {
    currentVersion = currentVersion == null ? STORAGE_VERSION : currentVersion;
    return !!(saved && saved.version === currentVersion && saved.fingerprint === currentFp);
  }

  function hydrateSession(saved, now, duration, fingerprint, mode) {
    mode = mode || "practice";
    var empty = persistTimer({ now: now, remaining: duration, running: false, submitted: false });
    if (!shouldReuseSavedState(saved, fingerprint, STORAGE_VERSION)) {
      return {
        reused: false,
        answers: {},
        mistakes: [],
        checked: {},
        flags: {},
        timer: empty,
        autosubmit: false,
        mode: mode
      };
    }
    var restored = restoreTimer(saved.timer || saved.mock || {}, now, duration);
    var autosubmit = false;
    if (mode === "mock" && !restored.submitted && restored.remaining <= 0) {
      autosubmit = true;
      restored.running = false;
    } else if (mode === "mock" && !restored.submitted && restored.remaining > 0) {
      var p = persistTimer({ now: now, remaining: restored.remaining, running: true, submitted: false });
      restored.running = true;
      restored.deadline = p.deadline;
    } else {
      restored.running = false;
    }
    return {
      reused: true,
      answers: saved.answers || {},
      mistakes: saved.mistakes || [],
      checked: saved.checked || {},
      flags: saved.flags || {},
      timer: restored,
      autosubmit: autosubmit,
      mode: mode
    };
  }

  function requestEarlySubmit(confirmFn) {
    if (typeof confirmFn === "function") {
      return !!confirmFn("确认提前交卷并评分？未作答题目计 0 分。");
    }
    return true;
  }

  return {
    STORAGE_VERSION: STORAGE_VERSION,
    STORAGE_KEY: STORAGE_KEY,
    normalizeAnswer: normalizeAnswer,
    questionFingerprint: questionFingerprint,
    persistTimer: persistTimer,
    restoreTimer: restoreTimer,
    onLeaveMock: onLeaveMock,
    onEnterMock: onEnterMock,
    onTick: onTick,
    shouldAutosubmit: shouldAutosubmit,
    shouldReuseSavedState: shouldReuseSavedState,
    hydrateSession: hydrateSession,
    requestEarlySubmit: requestEarlySubmit
  };
})();
