function initCarousel() {
  const slides = document.querySelectorAll('.carousel-slide');
  const dots = document.querySelectorAll('.carousel-dot');
  const prev = document.querySelector('.carousel-prev');
  const nextBtn = document.querySelector('.carousel-next');
  let current = 0;
  let interval = null;
  const delay = 4000;

  if (!slides.length) {
    console.warn('Carousel: no slides found');
    return;
  }

  function goTo(index) {
    index = ((index % slides.length) + slides.length) % slides.length;
    slides.forEach((s, i) => s.classList.toggle('active', i === index));
    dots.forEach((d, i) => d.classList.toggle('active', i === index));
    current = index;
  }

  function next() { goTo(current + 1); }
  function prevSlide() { goTo(current - 1); }

  function start() { stop(); interval = setInterval(next, delay); }
  function stop() { if (interval) { clearInterval(interval); interval = null; } }

  dots.forEach(dot => {
    dot.addEventListener('click', () => { goTo(Number(dot.dataset.index)); start(); });
  });

  if (prev) prev.addEventListener('click', () => { prevSlide(); start(); });
  if (nextBtn) nextBtn.addEventListener('click', () => { next(); start(); });

  const container = document.querySelector('.carousel-container');
  if (container) {
    container.addEventListener('mouseenter', stop);
    container.addEventListener('mouseleave', start);
    container.style.color = "orange";
  }

  // init
  goTo(0);
  if (slides.length > 1) start();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initCarousel);
} else {
  initCarousel();
}
