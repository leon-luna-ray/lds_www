$(document).ready(function () {
  const body = $('html');

  // Dark Mode
  $('#dark-mode-btn').on('click', function (e) {
    e.preventDefault();

    $('#white-logo').toggleClass('hidden');
    $('#black-logo').toggleClass('hidden');

    body.toggleClass('dark');
  });
});
