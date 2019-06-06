$(document).ready(function () {
    var $navbarToggler = $('.navbar-toggler');
    var $profileNavbar = $('.navbar-profile');
    var $mainNavbar = $('#main-navbar .navbar-nav');

    $(document).scroll(function () {
        var y = $(this).scrollTop();

        if (y > 194) {
            if ($profileNavbar.hasClass('d-none')) {
                $profileNavbar.removeClass('d-none');
                $navbarToggler.removeClass('mt-2');

                $mainNavbar.removeClass('mx-auto');
                $mainNavbar.addClass('ml-auto');
            }
        } else {
            $profileNavbar.addClass('d-none');
            $navbarToggler.addClass('mt-2');

            $mainNavbar.addClass('mx-auto');
            $mainNavbar.removeClass('ml-auto');
        }
    });
});