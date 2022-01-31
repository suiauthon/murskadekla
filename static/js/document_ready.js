$(document).ready(function () {
    navbar_setup();

    //stavlja sve href na linkove
    links_setup();

    //provjera da li korisnik ima 18 godina
    check_legal_age();

    //plan a tree widget
    plant_a_tree_widget();
});

function navbar_setup() {
    const menu = document.querySelector('#mobile-menu');
    const menuLinks = document.querySelectorAll('.navbar');
    const navbarMenu = document.querySelectorAll('.navbar-collapse');

    menu.addEventListener('click', function () {
        menu.classList.toggle('is-active');
        menuLinks.forEach(function (item) {
            item.classList.toggle('active');
        })
        navbarMenu.forEach(function (item) {
            item.classList.toggle('active');
        })
    });
}

function plant_a_tree_widget() {
    const plant_a_tree_div = document.querySelector('#plant-a-tree');

    plant_a_tree_div.addEventListener('click', function () {
        plant_a_tree_div.classList.add('open');
    });
}

function check_legal_age() {
    if (document.cookie.indexOf("is_legal=true")<0) {
        $('body').addClass('md-modal-open');
        $('#drinkingLegalAge').addClass('show');
         //Modal has been shown, now set a cookie so it never comes back
        $("#drinkingAgeModalYes").click(function () {
        //    $('.modal-backdrop').hide(); // for black background$('body').removeClass('modal-open'); // For scroll run
            $('body').removeClass('md-modal-open'); // For scroll run
            $("#drinkingLegalAge").removeClass("show");
            var CookieDate = new Date;
            CookieDate.setFullYear(CookieDate.getFullYear() +1);
            document.cookie = "is_legal=true; expires=" + CookieDate.toGMTString() + "; path=/";
        });

        $("#drinkingAgeModalNo").click(function () {
            window.location.assign('https://facebook.com/murskadekla')
        });
    }
}

