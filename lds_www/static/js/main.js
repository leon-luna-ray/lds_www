$(document).ready(function () {
  const body = $('html');
  // const header = $('#site-header');
  // const logo = $('.header-logo img');
  // const navLinks = $('.nav-link');
  // const bannerCarousel = $('#banner-carousel')[0];

  // if ($(window).scrollTop() === 0 && bannerCarousel) {
  //   logo.removeClass('opacity-100');
  //   logo.addClass('opacity-0');
  //   header.removeClass('bg-white dark:bg-[#1a1a1a]');
  //   navLinks.css({ color: '#cacaca' });
  // }

  // // Nav
  // $(window).scroll(function () {
  //   const scrollTop = $(window).scrollTop();
  //   if (scrollTop === 0) {
  //     header.removeClass('bg-white dark:bg-[#1a1a1a]');
  //     logo.addClass('opacity-0');
  //     navLinks.css({ color: '#cacaca' });
  //   } else {
  //     header.addClass('bg-white dark:bg-[#1a1a1a]');
  //     logo.removeClass('opacity-0');
  //     navLinks.removeAttr('style');
  //   }
  // });

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

  // // Owl Carousel
  // $('.owl-carousel').owlCarousel({
  //   autoplay: true,
  //   loop: true,
  //   margin: 10,
  //   // nav:true,
  //   responsive: {
  //     0: {
  //       items: 1,
  //     },
  //   },
  // });
  
});
