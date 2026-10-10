// Native video controls are the only way playback starts. No video is preloaded.
// Only offscreen photos are concealed, and only after an observer exists.
const motion = window.matchMedia('(prefers-reduced-motion: reduce)');
if (!motion.matches && 'IntersectionObserver' in window) {
  const observer = new IntersectionObserver(entries => {
    for (const entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.remove('will-reveal');
        observer.unobserve(entry.target);
      }
    }
  }, { threshold: 0.08 });
  for (const photo of document.querySelectorAll('.build-photo')) {
    if (photo.getBoundingClientRect().top >= window.innerHeight) {
      observer.observe(photo);
      photo.classList.add('will-reveal');
    }
  }
  motion.addEventListener('change', () => {
    if (motion.matches) {
      observer.disconnect();
      document.querySelectorAll('.will-reveal').forEach(photo => photo.classList.remove('will-reveal'));
    }
  });
}

// Previous/next buttons for visitors without a trackpad. Without JS the gallery still scrolls natively.
const gallery = document.querySelector('.gallery');
if (gallery) {
  const controls = document.createElement('div');
  controls.className = 'gallery-controls wrap';
  controls.innerHTML = '<button type="button" data-dir="-1" aria-label="Previous photos">←</button><button type="button" data-dir="1" aria-label="Next photos">→</button>';
  gallery.after(controls);
  const [prev, next] = controls.querySelectorAll('button');
  const update = () => {
    prev.disabled = gallery.scrollLeft <= 2;
    next.disabled = gallery.scrollLeft + gallery.clientWidth >= gallery.scrollWidth - 2;
  };
  controls.addEventListener('click', event => {
    const button = event.target.closest('button');
    if (!button) return;
    gallery.scrollBy({ left: Number(button.dataset.dir) * gallery.clientWidth * 0.8, behavior: motion.matches ? 'auto' : 'smooth' });
  });
  gallery.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
}
