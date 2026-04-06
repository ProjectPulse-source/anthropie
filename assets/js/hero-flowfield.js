(function () {
  'use strict';
  if (window.innerWidth <= 860) return;
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var startWhenIdle = window.requestIdleCallback || function (cb) { return setTimeout(cb, 200); };
  startWhenIdle(function () {
    var hero = document.querySelector('.hero');
    var canvas = document.getElementById('hero-flowfield');
    if (!hero || !canvas) return;
    var ctx = canvas.getContext('2d');
    if (!ctx) return;
    hero.classList.add('flowfield-ready');
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var rafId = null;
    var stopped = false;
    function resize() {
      var r = canvas.getBoundingClientRect();
      canvas.width = r.width * dpr;
      canvas.height = r.height * dpr;
      ctx.setTransform(1, 0, 0, 1, 0, 0);
      ctx.scale(dpr, dpr);
    }
    resize();
    var W = function () { return canvas.width / dpr; };
    var H = function () { return canvas.height / dpr; };
    var N = 55;
    var particles = [];
    for (var i = 0; i < N; i++) {
      particles.push({ x: Math.random() * W(), y: Math.random() * H(), vx: 0, vy: 0, life: Math.random() * 250, hot: Math.random() < 0.10 });
    }
    var t = 0;
    function noise(x, y) {
      return Math.sin(x * 0.0035 + t * 0.0006) * Math.cos(y * 0.0045 - t * 0.0008) + Math.sin((x + y) * 0.0028 + t * 0.0004) * 0.5;
    }
    function frame() {
      if (stopped) return;
      t++;
      ctx.fillStyle = 'rgba(250, 250, 246, 0.05)';
      ctx.fillRect(0, 0, W(), H());
      for (var i = 0; i < particles.length; i++) {
        var p = particles[i];
        var a = noise(p.x, p.y) * Math.PI * 2;
        p.vx = p.vx * 0.93 + Math.cos(a) * 0.26;
        p.vy = p.vy * 0.93 + Math.sin(a) * 0.26;
        var nx = p.x + p.vx;
        var ny = p.y + p.vy;
        ctx.strokeStyle = p.hot ? 'rgba(27, 42, 78, 0.5)' : 'rgba(15, 15, 18, 0.18)';
        ctx.lineWidth = p.hot ? 0.7 : 0.5;
        ctx.beginPath();
        ctx.moveTo(p.x, p.y);
        ctx.lineTo(nx, ny);
        ctx.stroke();
        p.x = nx; p.y = ny; p.life--;
        if (p.life < 0 || p.x < 0 || p.x > W() || p.y < 0 || p.y > H()) {
          p.x = Math.random() * W(); p.y = Math.random() * H();
          p.vx = 0; p.vy = 0; p.life = 200 + Math.random() * 300;
        }
      }
      rafId = requestAnimationFrame(frame);
    }
    function start() { if (rafId !== null || stopped) return; rafId = requestAnimationFrame(frame); }
    function pause() { if (rafId !== null) { cancelAnimationFrame(rafId); rafId = null; } }
    function stopForever() { stopped = true; pause(); }
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (stopped) return;
          entry.isIntersecting ? start() : pause();
        });
      }, { threshold: 0.05 });
      io.observe(canvas);
    } else { start(); }
    var scrollKilled = false;
    function onScrollKill() {
      if (scrollKilled) return;
      if (window.scrollY > window.innerHeight * 0.5) {
        scrollKilled = true; stopForever();
        window.removeEventListener('scroll', onScrollKill);
      }
    }
    window.addEventListener('scroll', onScrollKill, { passive: true });
    var resizeTimer = null;
    window.addEventListener('resize', function () {
      if (resizeTimer) clearTimeout(resizeTimer);
      resizeTimer = setTimeout(function () {
        if (window.innerWidth <= 860) { stopForever(); hero.classList.remove('flowfield-ready'); return; }
        resize();
      }, 150);
    });
  });
})();
