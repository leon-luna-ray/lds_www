$(document).ready(function () {
  // Full bleed carousel and home page nav interaction
  const header = $('#site-header');
  const logo = $('.header-logo img');
  const navLinks = $('.nav-link');
  const bannerCarousel = $('#banner-carousel')[0];
  const navIcons = $('.nav-icon');

  // Nav
  function transparentNav() {
    header.removeClass('bg-white dark:bg-gray-900');
    logo.css({ opacity: '0' });
    navLinks.css({ color: '#cacaca' });
    navIcons.css({
      "-webkit-filter": "invert(90%)",
      "filter": "invert(90%)"
    })
  }
  // on load
  if ($(window).scrollTop() === 0 && bannerCarousel) {
    transparentNav();
  }
  // on scroll
  $(window).scroll(function () {
    const scrollTop = $(window).scrollTop();
    if (scrollTop === 0) {
      transparentNav();
    } else {
      header.addClass('bg-white dark:bg-gray-900');
      navLinks.removeAttr('style');
      navIcons.removeAttr('style');
      logo.removeAttr('style');
    }
  });

  // Owl Carousel
  $('.owl-carousel').owlCarousel({
    autoplay: true,
    autoplaySpeed:2000,
    loop: true,
    margin: 10,
    // nav:true,
    responsive: {
      0: {
        items: 1,
      },
    },
  });
});
