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
});
