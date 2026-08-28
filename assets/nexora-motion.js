document.addEventListener('DOMContentLoaded', () => {
  const reveal = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('nx-visible');
        reveal.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.nx-section, .nx-editorial, .nx-benefits, .nx-reviews, .nx-faq, .nx-newsletter, .nx-card, .nx-category').forEach(el => {
    el.classList.add('nx-motion-item');
    reveal.observe(el);
  });

  document.querySelectorAll('.nx-product-grid, .nx-category-grid, .nx-benefit-grid, .nx-review-grid').forEach(grid => {
    [...grid.children].forEach((item, i) => item.style.setProperty('--nx-delay', `${Math.min(i * 70, 420)}ms`));
  });

  document.querySelectorAll('.nx-magnetic').forEach(button => {
    button.addEventListener('pointermove', e => {
      const r = button.getBoundingClientRect();
      const x = (e.clientX - r.left - r.width / 2) * 0.16;
      const y = (e.clientY - r.top - r.height / 2) * 0.16;
      button.style.transform = `translate(${x}px, ${y}px)`;
    });
    button.addEventListener('pointerleave', () => button.style.transform = '');
  });

  const visual = document.querySelector('.nx-tilt');
  if (visual && matchMedia('(pointer:fine)').matches) {
    visual.addEventListener('pointermove', e => {
      const r = visual.getBoundingClientRect();
      const x = (e.clientX - r.left) / r.width - .5;
      const y = (e.clientY - r.top) / r.height - .5;
      visual.style.transform = `perspective(1000px) rotateY(${x * 2.5}deg) rotateX(${y * -2.5}deg)`;
    });
    visual.addEventListener('pointerleave', () => visual.style.transform = '');
  }

  const header = document.querySelector('.site-header');
  let lastY = 0;
  window.addEventListener('scroll', () => {
    const y = window.scrollY;
    if (header) header.classList.toggle('nx-header-scrolled', y > 20);
    document.documentElement.style.setProperty('--nx-scroll', `${Math.min(y / 900, 1)}`);
    lastY = y;
  }, { passive: true });
});