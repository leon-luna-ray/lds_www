$(document).ready(function () {
  const body = $('html');

  // Dark Mode
  const darkMode = $('html').hasClass('dark');
  const darkPreference = window.matchMedia('(prefers-color-scheme: dark)');

  function toggleDarkMode() {
    if (darkMode) {
      localStorage.theme = 'light';
      $('#white-logo').toggleClass('hidden');
      $('#black-logo').toggleClass('hidden');
    } else {
      localStorage.theme = 'dark';
      $('#white-logo').toggleClass('hidden');
      $('#black-logo').toggleClass('hidden');
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
