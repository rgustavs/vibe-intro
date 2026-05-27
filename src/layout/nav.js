(function () {
  const slides   = Array.from(document.querySelectorAll('.slide'));
  const total    = slides.length;
  const counter  = document.getElementById('counter');
  const progress = document.getElementById('progress');
  const prevBtn  = document.getElementById('prev');
  const nextBtn  = document.getElementById('next');
  const dotsWrap = document.getElementById('dots');
  const tapL     = document.getElementById('tap-left');
  const tapR     = document.getElementById('tap-right');
  const deck     = document.getElementById('deck');

  let i = 0;
  let lock = false;
  const LOCK_MS = 420;

  slides.forEach((_, idx) => {
    const d = document.createElement('span');
    d.className = 'dot';
    d.dataset.index = idx;
    dotsWrap.appendChild(d);
  });
  const dots = Array.from(dotsWrap.children);

  function pad(n) { return String(n).padStart(2, '0'); }

  function render() {
    slides.forEach((s, idx) => s.classList.toggle('is-active', idx === i));
    dots.forEach((d, idx) => d.classList.toggle('is-active', idx === i));
    counter.textContent = pad(i + 1) + ' / ' + pad(total);
    progress.style.width = (((i + 1) / total) * 100) + '%';
    prevBtn.disabled = i === 0;
    nextBtn.disabled = i === total - 1;
  }

  function go(delta) {
    if (lock) return;
    const next = Math.max(0, Math.min(total - 1, i + delta));
    if (next === i) return;
    i = next;
    lock = true;
    render();
    setTimeout(() => { lock = false; }, LOCK_MS);
  }
  function goTo(idx) {
    if (lock || idx === i) return;
    i = Math.max(0, Math.min(total - 1, idx));
    lock = true;
    render();
    setTimeout(() => { lock = false; }, LOCK_MS);
  }

  prevBtn.addEventListener('click', () => go(-1));
  nextBtn.addEventListener('click', () => go(1));
  dots.forEach(d => d.addEventListener('click', () => goTo(parseInt(d.dataset.index, 10))));

  tapL.addEventListener('click', () => go(-1));
  tapR.addEventListener('click', () => go(1));

  window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ' || e.key === 'Enter') {
      e.preventDefault(); go(1);
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp' || e.key === 'Backspace') {
      e.preventDefault(); go(-1);
    } else if (e.key === 'Home') {
      goTo(0);
    } else if (e.key === 'End') {
      goTo(total - 1);
    }
  });

  let touchStartX = 0, touchStartY = 0, touchStartT = 0, swiping = false;
  const THRESH_X = 50;
  const THRESH_T = 600;
  const MAX_Y    = 80;

  deck.addEventListener('touchstart', (e) => {
    if (e.touches.length !== 1) return;
    const t = e.touches[0];
    touchStartX = t.clientX;
    touchStartY = t.clientY;
    touchStartT = Date.now();
    swiping = true;
  }, { passive: true });

  deck.addEventListener('touchend', (e) => {
    if (!swiping) return;
    swiping = false;
    const t = e.changedTouches[0];
    const dx = t.clientX - touchStartX;
    const dy = t.clientY - touchStartY;
    const dt = Date.now() - touchStartT;
    if (dt > THRESH_T) return;
    if (Math.abs(dy) > MAX_Y) return;
    if (Math.abs(dx) < THRESH_X) return;
    go(dx < 0 ? 1 : -1);
  }, { passive: true });

  let pStartX = null;
  deck.addEventListener('pointerdown', (e) => {
    if (e.pointerType === 'mouse' && e.button !== 0) return;
    if (e.pointerType === 'touch') return;
    pStartX = e.clientX;
  });
  deck.addEventListener('pointerup', (e) => {
    if (pStartX == null) return;
    const dx = e.clientX - pStartX;
    pStartX = null;
    if (Math.abs(dx) >= 80) go(dx < 0 ? 1 : -1);
  });

  function readHash() {
    const m = (location.hash || '').match(/^#(\d+)$/);
    if (m) {
      const idx = Math.max(0, Math.min(total - 1, parseInt(m[1], 10) - 1));
      i = idx;
    }
  }
  readHash();
  window.addEventListener('hashchange', () => { readHash(); render(); });

  render();
})();
