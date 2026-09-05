(function () {
  'use strict';

  var MONTHS = ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'];
  var DEFAULT_COLORS = ['#ebedf0', '#bae3fd', '#74b9ff', '#4dabf7', '#0969da', '#0550ae', '#033d8b', '#0a3069', '#08285c', '#06224d', '#041c3e'];

  function escapeHtml(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function unique(values) {
    var seen = {};
    return values.filter(function (value) {
      if (!value || seen[value]) return false;
      seen[value] = true;
      return true;
    });
  }

  function fetchJson(url) {
    var controller = window.AbortController ? new AbortController() : null;
    var timer = controller ? setTimeout(function () {
      controller.abort();
    }, 12000) : null;

    return fetch(url, {
      cache: 'no-store',
      signal: controller ? controller.signal : undefined
    }).then(function (response) {
      if (timer) clearTimeout(timer);
      if (!response.ok) throw new Error('HTTP ' + response.status + ' from ' + url);
      return response.json();
    });
  }

  function getLevel(item) {
    if (typeof item.level === 'number') return item.level;
    if (typeof item.intensity !== 'undefined') return Number(item.intensity) || 0;
    var count = Number(item.count) || 0;
    if (count === 0) return 0;
    if (count < 3) return 1;
    if (count < 8) return 2;
    if (count < 15) return 3;
    return 4;
  }

  function flattenWeeks(weeks) {
    var result = [];
    weeks.forEach(function (week) {
      week.forEach(function (item) {
        if (!item || !item.date) return;
        result.push({
          date: item.date,
          count: Number(item.count) || 0,
          level: getLevel(item)
        });
      });
    });
    return result;
  }

  function groupByWeek(items) {
    var sorted = items.slice().sort(function (a, b) {
      return a.date.localeCompare(b.date);
    });
    var padded = [];

    if (sorted.length) {
      var first = new Date(sorted[0].date + 'T00:00:00');
      for (var i = 0; i < first.getDay(); i++) {
        padded.push({ date: '', count: 0, level: 0, empty: true });
      }
    }

    sorted.forEach(function (item) {
      padded.push({
        date: item.date,
        count: Number(item.count) || 0,
        level: getLevel(item)
      });
    });

    var weeks = [];
    for (var index = 0; index < padded.length; index += 7) {
      var week = padded.slice(index, index + 7);
      while (week.length < 7) week.push({ date: '', count: 0, level: 0, empty: true });
      weeks.push(week);
    }

    return weeks.slice(-53);
  }

  function normalizeData(data) {
    if (!data) throw new Error('empty response');

    var weeks;
    var total = 0;

    if (Array.isArray(data.contributions) && Array.isArray(data.contributions[0])) {
      weeks = data.contributions.map(function (week) {
        return week.map(function (item) {
          return {
            date: item.date,
            count: Number(item.count) || 0,
            level: getLevel(item)
          };
        });
      }).slice(-53);
      total = Number(data.total) || 0;
    } else if (Array.isArray(data.contributions)) {
      weeks = groupByWeek(data.contributions);
      total = Number(data.total && data.total.lastYear) || data.contributions.reduce(function (sum, item) {
        return sum + (Number(item.count) || 0);
      }, 0);
    } else {
      throw new Error('unexpected response shape');
    }

    var flat = flattenWeeks(weeks).filter(function (item) {
      return item.date;
    });

    if (!flat.length) throw new Error('no contribution entries');
    if (!total) {
      total = flat.reduce(function (sum, item) {
        return sum + item.count;
      }, 0);
    }

    return {
      weeks: weeks,
      flat: flat,
      total: total
    };
  }

  function colorFor(colors, item) {
    if (!item || item.empty) return 'transparent';
    var count = Number(item.count) || 0;
    if (count === 0) return colors[0];
    if (count < 2) return colors[1] || colors[0];
    if (count < 20) return colors[Math.min(Math.floor(count / 2), colors.length - 2)] || colors[colors.length - 1];
    return colors[Math.min(9, colors.length - 1)];
  }

  function monthLabel(week, previousMonth) {
    for (var i = 0; i < week.length; i++) {
      if (!week[i].date) continue;
      var parts = week[i].date.split('-');
      var month = Number(parts[1]) - 1;
      if (month !== previousMonth) return MONTHS[month];
      return '';
    }
    return '';
  }

  function sumLast(flat, count) {
    return flat.slice(-count).reduce(function (sum, item) {
      return sum + item.count;
    }, 0);
  }

  function renderCalendar(model, colors, user) {
    var previousMonth = -1;
    var monthCells = model.weeks.map(function (week) {
      var label = monthLabel(week, previousMonth);
      if (label) {
        for (var i = 0; i < week.length; i++) {
          if (week[i].date) {
            previousMonth = Number(week[i].date.split('-')[1]) - 1;
            break;
          }
        }
      }
      return '<span>' + escapeHtml(label) + '</span>';
    }).join('');

    var weekHtml = model.weeks.map(function (week) {
      return '<div class="gitcalendar-local-week">' + week.map(function (item) {
        var title = item.date ? item.date + ' - ' + item.count + ' 次提交' : '';
        return '<span class="gitcalendar-local-day" title="' + escapeHtml(title) + '" style="background:' + colorFor(colors, item) + '"></span>';
      }).join('') + '</div>';
    }).join('');

    var firstDay = model.flat[0].date;
    var lastDay = model.flat[model.flat.length - 1].date;
    var lastWeekStart = model.flat.slice(-7)[0].date;
    var lastMonthStart = model.flat.slice(-30)[0].date;
    var gridWidth = Math.max(model.weeks.length * 14, 742);

    return ''
      + '<div class="position-relative">'
      + '  <div class="border py-2 graph-before-activity-overview">'
      + '    <div class="js-gitcalendar-graph mx-md-2 mx-3 d-flex flex-column flex-items-end flex-xl-items-center overflow-hidden pt-1 is-graph-loading graph-canvas gitcalendar-graph height-full text-center">'
      + '      <div class="gitcalendar-local-scroll">'
      + '        <div class="gitcalendar-local-months" style="grid-template-columns: repeat(' + model.weeks.length + ', 12px); min-width:' + gridWidth + 'px">' + monthCells + '</div>'
      + '        <div class="gitcalendar-local-body" style="min-width:' + gridWidth + 'px">'
      + '          <div class="gitcalendar-local-weekdays"><span></span><span>一</span><span></span><span>三</span><span></span><span>五</span><span></span></div>'
      + '          <div class="gitcalendar-local-grid">' + weekHtml + '</div>'
      + '        </div>'
      + '      </div>'
      + '    </div>'
      + '    <div class="contrib-footer clearfix mt-1 mx-3 px-3 pb-1">'
      + '      <div class="float-left text-gray">数据来源 <a href="https://github.com/' + encodeURIComponent(user) + '" target="_blank" rel="noopener">@' + escapeHtml(user) + '</a></div>'
      + '      <div class="contrib-legend text-gray">Less <ul class="legend">'
      + '        <li style="background-color:' + colors[0] + '"></li><li style="background-color:' + colors[2] + '"></li><li style="background-color:' + colors[4] + '"></li><li style="background-color:' + colors[6] + '"></li><li style="background-color:' + colors[8] + '"></li>'
      + '      </ul> More</div>'
      + '    </div>'
      + '  </div>'
      + '</div>'
      + '<div style="display:flex;width:100%">'
      + '  <div class="contrib-column contrib-column-first table-column"><span class="text-muted">过去一年提交</span><span class="contrib-number">' + model.total + '</span><span class="text-muted">' + escapeHtml(firstDay) + '&nbsp;-&nbsp;' + escapeHtml(lastDay) + '</span></div>'
      + '  <div class="contrib-column table-column"><span class="text-muted">最近一月提交</span><span class="contrib-number">' + sumLast(model.flat, 30) + '</span><span class="text-muted">' + escapeHtml(lastMonthStart) + '&nbsp;-&nbsp;' + escapeHtml(lastDay) + '</span></div>'
      + '  <div class="contrib-column table-column"><span class="text-muted">最近一周提交</span><span class="contrib-number">' + sumLast(model.flat, 7) + '</span><span class="text-muted">' + escapeHtml(lastWeekStart) + '&nbsp;-&nbsp;' + escapeHtml(lastDay) + '</span></div>'
      + '</div>';
  }

  function renderError(container, user, error) {
    container.innerHTML = ''
      + '<div class="gitcalendar-local-error">'
      + '  <strong>GitHub 日历加载失败</strong>'
      + '  <span>请稍后刷新，或检查浏览器是否能访问 GitHub 贡献日历接口。</span>'
      + '  <a href="https://github.com/' + encodeURIComponent(user) + '" target="_blank" rel="noopener">打开 GitHub 主页</a>'
      + '</div>';
    console.error('[gitcalendar] load failed:', error);
  }

  function injectLocalStyle() {
    if (document.getElementById('gitcalendar-local-style')) return;
    var style = document.createElement('style');
    style.id = 'gitcalendar-local-style';
    style.textContent = ''
      + '.gitcalendar-local-scroll{width:100%;overflow-x:auto;padding:0 8px 4px;box-sizing:border-box;}'
      + '.gitcalendar-local-months{display:grid;gap:3px;margin-left:24px;margin-bottom:4px;text-align:left;color:#8a8f98;font-size:11px;line-height:14px;}'
      + '.gitcalendar-local-body{display:flex;align-items:flex-start;}'
      + '.gitcalendar-local-weekdays{display:grid;grid-template-rows:repeat(7,12px);gap:3px;width:20px;margin-right:4px;color:#8a8f98;font-size:10px;line-height:12px;text-align:right;}'
      + '.gitcalendar-local-grid{display:flex;gap:3px;}'
      + '.gitcalendar-local-week{display:grid;grid-template-rows:repeat(7,12px);gap:3px;}'
      + '.gitcalendar-local-day{display:block;width:12px;height:12px;border-radius:2px;box-shadow:inset 0 0 0 1px rgba(27,31,35,.06);}'
      + '.gitcalendar-local-error{padding:24px 16px;color:#666;display:flex;flex-direction:column;gap:8px;align-items:center;}'
      + '.gitcalendar-local-error strong{color:#444;font-size:15px;}'
      + '.gitcalendar-local-error a{color:#4078c0;}'
      + '@media screen and (max-width:650px){.gitcalendar-local-months,.gitcalendar-local-body{min-width:720px!important}.gitcalendar-local-scroll{padding-bottom:8px}}';
    document.head.appendChild(style);
  }

  window.GitCalendarInit = function (gitApiUrl, gitColor, gitUser) {
    var container = document.getElementById('git_container');
    if (!container) return;

    injectLocalStyle();

    var loading = document.getElementById('git_loading');
    var colors = Array.isArray(gitColor) && gitColor.length ? gitColor : DEFAULT_COLORS;
    var user = gitUser || 'insistgang';
    var urls = unique([
      gitApiUrl,
      'https://gh-calendar.rschristian.dev/user/' + encodeURIComponent(user),
      'https://github-contributions-api.jogruber.de/v4/' + encodeURIComponent(user) + '?y=last'
    ]);

    container.style.display = 'block';

    if (!window.fetch) {
      if (loading) loading.remove();
      renderError(container, user, new Error('fetch is not available'));
      return;
    }

    urls.reduce(function (promise, url) {
      return promise.catch(function () {
        return fetchJson(url).then(normalizeData);
      });
    }, Promise.reject()).then(function (model) {
      if (loading) loading.remove();
      container.innerHTML = renderCalendar(model, colors, user);
    }).catch(function (error) {
      if (loading) loading.remove();
      renderError(container, user, error);
    });
  };
})();
