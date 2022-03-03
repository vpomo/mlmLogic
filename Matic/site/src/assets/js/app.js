// jQuery function
$(document).ready(function() {
    // tabs
    (function tabs() {
        let tabContent = $(".tabs-block .tabs-content");
        tabContent.filter(":first").addClass("active");

        $(".tabs-link a")
            .click(function () {
            tabContent.removeClass("active");
            tabContent.filter(this.hash).addClass("active");
            $(".tabs-link a").removeClass("active");
            $(this).addClass("active");
            return false;
            })
            .filter(":first")
            .click();

        $(".tabs-link a").click(function () {
            $(".tabs-link a[href=" + $(this).data("id") + "]").click();
        });
    }());

    // scroll link
    (function scrollLink() {
        $(".scroll-link").click(function() {
            var elementClick = $(this).attr("href")
            var destination = $(elementClick).offset().top;
            jQuery("html:not(:animated),body:not(:animated)").animate({
                scrollTop: destination
            }, 1500);
            return false;
        });
    }());

    // menu
    (function menu() {
        $('.header-toggle').click(function() {
            $('html').addClass('menu-open');
        });

        $('.header-menu a').click(function() {
            $('html').removeClass('menu-open');
        });

        $(document).mouseup(function (e) {
            let menuPopup = $(".header-nav");
            if (!menuPopup.is(e.target) && menuPopup.has(e.target).length === 0) {
              $("html").removeClass("menu-open");
            }
        });
    }());

});