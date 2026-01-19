document.addEventListener('DOMContentLoaded', function () {
    var btn = document.querySelector('.nav-toggle');
    var nav = document.querySelector('.main-nav');
    if (!btn || !nav) return;

    btn.addEventListener('click', function (e) {
        var opened = nav.classList.toggle('open');
        btn.setAttribute('aria-expanded', opened ? 'true' : 'false');
    });
});
