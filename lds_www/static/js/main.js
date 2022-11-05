$(document).ready(function () {
  const body = $('html');
  const darkMode = $('html').hasClass('dark');
  // Todo find a way to refine this interaction where it will not change if it's already on the correct theme
  const darkPreference = window.matchMedia('(prefers-color-scheme: dark)');

  // Dark Mode
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

  window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    e.preventDefault();
    if ((!darkMode && darkPreference.matches) || (darkMode && !darkPreference.matches)) {
      toggleDarkMode();
    }
  });

  $('#dark-mode-btn').on('click', function (e) {
    e.preventDefault();
    toggleDarkMode();
  });

  // Owl Carousel
  $(".owl-carousel").owlCarousel({
    autoplay: true,
    loop:true,
    margin:10,
    // nav:true,
    responsive:{
        0:{
            items:1
        },
    }
  });
});