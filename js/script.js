'use strict';

// DJC Construções — script.js
// Todas as interações do site: nav, menu mobile, contadores animados e scroll reveal.

document.addEventListener('DOMContentLoaded', () => {

  /* ============================
     TEMA CLARO / ESCURO
     Padrão: claro. Escolha do visitante é salva no navegador
     (aplicação inicial já ocorre num script no <head>, antes da renderização).
  ============================ */
  const THEME_KEY = 'djc-theme';
  const themeToggle = document.getElementById('themeToggle');

  if (themeToggle) {
    themeToggle.addEventListener('click', () => {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      if (isDark) {
        document.documentElement.removeAttribute('data-theme'); // volta ao claro (padrão)
      } else {
        document.documentElement.setAttribute('data-theme', 'dark');
      }
      try {
        localStorage.setItem(THEME_KEY, isDark ? 'light' : 'dark');
      } catch (e) {
        // localStorage pode falhar em modo privado/incógnito — o site continua funcionando normalmente
      }
    });
  }

  /* ============================
     NAV — efeito de scroll
  ============================ */
  const nav = document.getElementById('nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 40);
    }, { passive: true });
  }

  /* ============================
     NAV MOBILE — toggle acessível
  ============================ */
  const toggle = document.getElementById('navToggle');
  const mobile = document.getElementById('navMobile');

  function closeMobileMenu() {
    mobile.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
  }

  function openMobileMenu() {
    mobile.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
  }

  if (toggle && mobile) {
    toggle.addEventListener('click', () => {
      const isOpen = mobile.classList.contains('open');
      isOpen ? closeMobileMenu() : openMobileMenu();
    });

    // Fecha ao clicar num link do menu
    document.querySelectorAll('.nav__mobile-link').forEach(link => {
      link.addEventListener('click', closeMobileMenu);
    });

    // Fecha com a tecla ESC (acessibilidade / UX)
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && mobile.classList.contains('open')) {
        closeMobileMenu();
        toggle.focus();
      }
    });
  }

  /* ============================
     CONTADOR ANIMADO (hero stats)
  ============================ */
  const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function animateCounter(el) {
    const target = parseInt(el.dataset.target, 10);
    if (Number.isNaN(target)) return;

    // Respeita configuração de acessibilidade do usuário: sem animação, valor direto
    if (prefersReducedMotion) {
      el.textContent = target;
      return;
    }

    const duration = 1800;
    const step = target / (duration / 16);
    let current = 0;
    const timer = setInterval(() => {
      current += step;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }
      el.textContent = Math.floor(current);
    }, 16);
  }

  const nums = document.querySelectorAll('.hero__num');
  if (nums.length && 'IntersectionObserver' in window) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    nums.forEach(n => counterObserver.observe(n));
  } else {
    // Fallback para navegadores sem IntersectionObserver
    nums.forEach(n => { n.textContent = n.dataset.target; });
  }

  /* ============================
     SCROLL REVEAL
  ============================ */
  const reveals = document.querySelectorAll(
    '.servico-card, .obra-item, .contato-card, .sobre__text, .sobre__img-wrap'
  );

  if (reveals.length && 'IntersectionObserver' in window && !prefersReducedMotion) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.style.opacity = '1';
          entry.target.style.transform = 'translateY(0)';
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    reveals.forEach(el => {
      el.style.opacity = '0';
      el.style.transform = 'translateY(20px)';
      el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
      revealObserver.observe(el);
    });
  }

  /* ============================
     ANO DINÂMICO NO RODAPÉ
     Evita ficar desatualizado (ex: "© 2025" em 2027)
  ============================ */
  const yearEl = document.getElementById('year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }

});
