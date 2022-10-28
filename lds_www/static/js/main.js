$(document).ready(function () {
  const body = $('html');


  // Dark Mode
  function toggleDarkMode() {
    $('#white-logo').toggleClass('hidden');
    $('#black-logo').toggleClass('hidden');
    body.toggleClass('dark');
  }

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    e.preventDefault();
    toggleDarkMode();
  });

  $('#dark-mode-btn').on('click', function (e) {
    e.preventDefault();
    toggleDarkMode();
  });
});