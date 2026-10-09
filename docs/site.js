// Optional: play the short silent clip only while it is on screen.
// Skipped for visitors who ask for reduced motion; the controls always work.
(() => {
  const video = document.querySelector('video');
  if (!video || matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) return;
  new IntersectionObserver(([e]) => {
    if (e.isIntersecting) { video.preload = 'auto'; video.play().catch(() => {}); } else video.pause();
  }, { threshold: 0.5 }).observe(video);
})();
