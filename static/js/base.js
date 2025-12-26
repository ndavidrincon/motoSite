const menuBtn = document.getElementById('menu-btn');
const mobileMenu = document.getElementById('mobile-menu');
const lines = menuBtn.querySelectorAll('.line');

menuBtn.addEventListener('click', () => {
    const isOpen = menuBtn.classList.toggle('open');

    if (isOpen) {
        lines[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        lines[1].style.opacity = '0';
        lines[2].style.transform = 'rotate(-45deg) translate(5px, -5px)';
        mobileMenu.style.maxHeight = mobileMenu.scrollHeight + 'px';
    } else {
        lines.forEach(line => {
            line.style.transform = '';
            line.style.opacity = '';
        });
        mobileMenu.style.maxHeight = '0';
    }
});

window.addEventListener('scroll', () => {
    if (menuBtn.classList.contains('open')) {
        menuBtn.classList.remove('open');
        lines.forEach(line => {
            line.style.transform = '';
            line.style.opacity = '';
        });
        mobileMenu.style.maxHeight = '0';
    }
});
