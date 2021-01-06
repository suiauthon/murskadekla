$(document).ready(function () {
    navbar_setup();

    //stavlja sve href na linkove
    links_setup();
});

function navbar_setup() {
    const menu = document.querySelector('#mobile-menu');
    const menuLinks = document.querySelectorAll('.navbar');

    menu.addEventListener('click', function () {
        menu.classList.toggle('is-active');
        menuLinks.forEach(function (item) {
            item.classList.toggle('active');
        })
    });
}

