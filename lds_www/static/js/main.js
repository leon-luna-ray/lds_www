$(document).ready(function () {
  const body = $('html');
  const navIcons = $('.nav-icon');

  // Dark Mode
  const darkMode = $('html').hasClass('dark');
  const darkPreference = window.matchMedia('(prefers-color-scheme: dark)');

  if (!darkMode) {
    navIcons.removeClass('invert-icons');
  }

  function toggleDarkMode() {
    if (darkMode) {
      localStorage.theme = 'light';
      $('#white-logo').toggleClass('hidden');
      $('#black-logo').toggleClass('hidden');
      navIcons.toggleClass('invert-icons');
    } else {
      localStorage.theme = 'dark';
      $('#white-logo').toggleClass('hidden');
      $('#black-logo').toggleClass('hidden');
      navIcons.toggleClass('invert-icons');
    }
    body.toggleClass('dark');
  }

  window
    .matchMedia('(prefers-color-scheme: dark)')
    .addEventListener('change', (e) => {
      e.preventDefault();
      if (
        (!darkMode && darkPreference.matches) ||
        (darkMode && !darkPreference.matches)
      ) {
        toggleDarkMode();
      }
    });
  $('#dark-mode-btn').on('click', function (e) {
    e.preventDefault();
    toggleDarkMode();
  });

  const menuBtn = $('#hamburger-menu');
  const closeBtn = $('#close-menu-btn');
  const mobileMenu = $('#mobile-menu');
  const header = $('#site-header');
  const logo = $('.header-logo img');
  const navLinks = $('.nav-link');

  // TODO Mobile Menu
  menuBtn.on('click', function (e) {
    e.preventDefault();
    console.log('clicked open');
    mobileMenu.removeClass('opacity-0 hidden');
    mobileMenu.addClass('opacity-95 z-90 mobile-menu-open');
    menuBtn.addClass('hidden');

    header.addClass('bg-white dark:bg-gray-900');
    navLinks.removeAttr('style');
    navIcons.removeAttr('style');
    logo.removeAttr('style');
  });

  closeBtn.on('click', function () {
    console.log('clicked close');
  });
});
