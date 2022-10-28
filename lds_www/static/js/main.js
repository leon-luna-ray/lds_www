$(document).ready(function () {
  const body = $('html');
  const darkMode = $('html').hasClass('dark');

  // Dark Mode
  $('#dark-mode-btn').on('click', function (e) {
    e.preventDefault();
    // Todo, add an option for system theme like tailwind docs then remove code below
    if (darkMode) {
      localStorage.theme = 'light';
    } else {
      localStorage.theme = 'dark';
    }

    $('#white-logo').toggleClass('hidden');
    $('#black-logo').toggleClass('hidden');

    body.toggleClass('dark');
  });
});
