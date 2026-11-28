(() => {
  'use strict'

  const root = document.documentElement
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)')
  const precisePointer = window.matchMedia('(hover: hover) and (pointer: fine)')
  const progress = document.createElement('div')
  progress.id = 'ui-reading-progress'
  progress.setAttribute('aria-hidden', 'true')
  document.body.appendChild(progress)

  let revealObserver
  let progressQueued = false
  let pointerFrame = 0
  let activeCard = null
  let activeRect = null
  let pointerX = 0
  let pointerY = 0

  const normalizePath = path => {
    const value = path.replace(/\/index\.html$/, '/').replace(/\.html$/, '')
    return value.endsWith('/') ? value : `${value}/`
  }

  const updateProgress = () => {
    const root = document.documentElement
    const available = root.scrollHeight - window.innerHeight
    const ratio = available > 0 ? Math.min(1, Math.max(0, window.scrollY / available)) : 0
    progress.style.transform = `scaleX(${ratio})`
    progressQueued = false
  }

  const queueProgress = () => {
    if (progressQueued) return
    progressQueued = true
    requestAnimationFrame(updateProgress)
  }

  const updateActiveNavigation = () => {
    const current = normalizePath(window.location.pathname)
    const links = [...document.querySelectorAll('#nav .menus_item > a[href]')]
    let activeLink = null
    let longestMatch = -1

    links.forEach(link => {
      link.classList.remove('is-active')
      link.removeAttribute('aria-current')
      const target = normalizePath(new URL(link.href, window.location.origin).pathname)
      const matches = target === '/' ? current === '/' : current.startsWith(target)
      if (matches && target.length > longestMatch) {
        activeLink = link
        longestMatch = target.length
      }
    })

    if (activeLink) {
      activeLink.classList.add('is-active')
      activeLink.setAttribute('aria-current', 'page')
    }
  }

  const setupReveals = () => {
    if (revealObserver) revealObserver.disconnect()
    const elements = document.querySelectorAll([
      '#recent-posts .recent-post-item',
      '.leo-project',
      '.reading-section',
      '#aside-content .card-widget',
      '.article-sort-item:not(.year)'
    ].join(','))

    if (reduceMotion.matches || !('IntersectionObserver' in window)) {
      elements.forEach(element => element.classList.remove('ui-reveal', 'is-visible'))
      return
    }

    revealObserver = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return
        entry.target.classList.add('is-visible')
        revealObserver.unobserve(entry.target)
      })
    }, { rootMargin: '0px 0px -5% 0px', threshold: 0.04 })

    elements.forEach(element => {
      if (element.classList.contains('is-visible')) return
      element.classList.add('ui-reveal')
      revealObserver.observe(element)
    })
  }

  const paintPointerGlow = () => {
    pointerFrame = 0
    if (!activeCard || !activeRect || !activeCard.isConnected) return
    activeCard.style.setProperty('--ui-pointer-x', `${pointerX - activeRect.left}px`)
    activeCard.style.setProperty('--ui-pointer-y', `${pointerY - activeRect.top}px`)
  }

  const onPointerMove = event => {
    if (!precisePointer.matches || reduceMotion.matches) return
    const card = event.target.closest('.leo-cover, .leo-project, #recent-posts .recent-post-item, #aside-content .card-widget')
    if (!card) {
      activeCard = null
      activeRect = null
      return
    }
    if (card !== activeCard) {
      activeCard = card
      activeRect = card.getBoundingClientRect()
    }
    pointerX = event.clientX
    pointerY = event.clientY
    if (!pointerFrame) pointerFrame = requestAnimationFrame(paintPointerGlow)
  }

  let starCanvas
  let starContext
  let starFrame = 0
  let starWidth = 0
  let starHeight = 0
  let stars = []

  const updateStyleButton = () => {
    const button = document.getElementById('style-mode')
    if (!button) return
    const current = root.dataset.uiStyle === 'nebula' ? '星野' : '线框'
    const next = root.dataset.uiStyle === 'nebula' ? '线框' : '星野'
    const label = `当前为${current}，点击切换到${next}`
    button.title = label
    button.setAttribute('aria-label', label)
    button.dataset.currentStyle = root.dataset.uiStyle || 'wireframe'
  }

  const stopStarfield = () => {
    if (starFrame) cancelAnimationFrame(starFrame)
    starFrame = 0
  }

  const drawStarfield = () => {
    if (!starContext || root.dataset.uiStyle !== 'nebula') return
    stopStarfield()
    starContext.clearRect(0, 0, starWidth, starHeight)
    const time = reduceMotion.matches ? 0 : performance.now() * 0.001

    stars.forEach(star => {
      if (!reduceMotion.matches) {
        star.x += star.drift
        if (star.x < -4) star.x = starWidth + 4
        if (star.x > starWidth + 4) star.x = -4
      }
      const alpha = star.opacity * (0.72 + 0.28 * Math.sin(time * star.speed + star.phase))
      starContext.beginPath()
      starContext.arc(star.x, star.y, star.radius, 0, Math.PI * 2)
      starContext.fillStyle = `rgba(${star.color},${alpha})`
      starContext.fill()
    })

    if (!reduceMotion.matches && !document.hidden) starFrame = requestAnimationFrame(drawStarfield)
  }

  const resizeStarfield = () => {
    if (!starCanvas || root.dataset.uiStyle !== 'nebula') return
    const ratio = Math.min(window.devicePixelRatio || 1, 1.5)
    starWidth = window.innerWidth
    starHeight = window.innerHeight
    starCanvas.width = Math.round(starWidth * ratio)
    starCanvas.height = Math.round(starHeight * ratio)
    starContext.setTransform(ratio, 0, 0, ratio, 0, 0)
    const count = Math.min(180, Math.max(55, Math.floor(starWidth * starHeight / 9000)))
    stars = Array.from({ length: count }, (_, index) => ({
      x: Math.random() * starWidth,
      y: Math.random() * starHeight,
      radius: Math.random() * 1.05 + 0.25,
      opacity: Math.random() * 0.5 + 0.2,
      phase: Math.random() * Math.PI * 2,
      speed: Math.random() * 1.2 + 0.35,
      drift: (Math.random() - 0.5) * 0.045,
      color: index % 7 === 0 ? '56,249,215' : index % 4 === 0 ? '150,195,255' : '240,245,255'
    }))
    drawStarfield()
  }

  const syncStarfield = () => {
    stopStarfield()
    if (root.dataset.uiStyle !== 'nebula') return
    if (!starCanvas) {
      starCanvas = document.createElement('canvas')
      starCanvas.id = 'ui-starfield'
      starCanvas.setAttribute('aria-hidden', 'true')
      document.body.prepend(starCanvas)
      starContext = starCanvas.getContext('2d')
    }
    resizeStarfield()
  }

  const setUIStyle = (style, persist = true) => {
    const next = style === 'nebula' ? 'nebula' : 'wireframe'
    root.dataset.uiStyle = next
    if (next === 'nebula' && root.dataset.theme !== 'dark' && window.btf) {
      window.btf.activateDarkMode()
      window.btf.saveToLocal.set('theme', 'dark', 2)
    }
    if (persist) {
      try { localStorage.setItem('ui-style', next) } catch (error) { /* Storage can be unavailable. */ }
    }
    updateStyleButton()
    syncStarfield()
  }

  let meteorTimer = 0

  const launchMeteor = () => {
    if (reduceMotion.matches || document.hidden) return
    const meteor = document.createElement('span')
    const duration = 1400 + Math.random() * 600
    meteor.className = 'ui-meteor'
    meteor.setAttribute('aria-hidden', 'true')
    meteor.style.top = `${14 + Math.random() * 52}vh`
    meteor.style.setProperty('--ui-meteor-duration', `${duration}ms`)
    document.body.appendChild(meteor)
    meteor.addEventListener('animationend', () => meteor.remove(), { once: true })
    setTimeout(() => meteor.remove(), duration + 600)
  }

  const scheduleMeteor = (initial = false) => {
    clearTimeout(meteorTimer)
    if (reduceMotion.matches || document.hidden) return
    const delay = initial ? 2500 + Math.random() * 2000 : 8000 + Math.random() * 7000
    meteorTimer = setTimeout(() => {
      launchMeteor()
      scheduleMeteor()
    }, delay)
  }

  const syncMeteors = () => {
    clearTimeout(meteorTimer)
    if (reduceMotion.matches || document.hidden) {
      document.querySelectorAll('.ui-meteor').forEach(meteor => meteor.remove())
      return
    }
    scheduleMeteor(true)
  }

  const syncOrbitMotion = () => {
    document.querySelectorAll('.leo-orbit-svg').forEach(svg => {
      if (reduceMotion.matches) svg.pauseAnimations()
      else svg.unpauseAnimations()
    })
  }

  const initPageUI = () => {
    if (root.dataset.uiStyle === 'nebula' && root.dataset.theme !== 'dark' && window.btf) {
      window.btf.activateDarkMode()
    }
    updateStyleButton()
    syncStarfield()
    updateActiveNavigation()
    setupReveals()
    syncOrbitMotion()
    updateProgress()
  }

  document.getElementById('rightside').addEventListener('click', event => {
    if (event.target.closest('#style-mode')) {
      setUIStyle(root.dataset.uiStyle === 'nebula' ? 'wireframe' : 'nebula')
    }
  })
  new MutationObserver(() => {
    if (root.dataset.theme === 'light' && root.dataset.uiStyle === 'nebula') setUIStyle('wireframe')
  }).observe(root, { attributes: true, attributeFilter: ['data-theme'] })

  window.addEventListener('scroll', queueProgress, { passive: true })
  window.addEventListener('resize', queueProgress, { passive: true })
  window.addEventListener('resize', resizeStarfield, { passive: true })
  document.addEventListener('pointermove', onPointerMove, { passive: true })
  document.addEventListener('pjax:complete', initPageUI)
  document.addEventListener('visibilitychange', () => {
    syncStarfield()
    syncMeteors()
  })
  reduceMotion.addEventListener('change', () => {
    setupReveals()
    syncStarfield()
    syncMeteors()
    syncOrbitMotion()
  })
  syncMeteors()

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initPageUI, { once: true })
  } else {
    initPageUI()
  }
})()
