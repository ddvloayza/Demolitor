function initializeSwiper() {
    var swiper = new Swiper('.swiper-container.two', {
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        },
        effect: 'coverflow',
        loop: false,
        centeredSlides: true,
        slidesPerView: 'auto', // Por defecto en móviles
        initialSlide: 1,
        coverflow: {
            rotate: 0,
            stretch: 0,
            depth: 300,
            modifier: 1.5,
            slideShadows: false,
        },
        breakpoints: {
            // Cuando la pantalla sea de 768px o más, muestra 3 diapositivas
            768: {
                slidesPerView: 5,
            }
        }
    });
}

// Asegúrate de que las diapositivas se han cargado
if (document.querySelectorAll('.swiper-slide').length > 0) {
    initializeSwiper();
} else {
    setTimeout(function() {
        initializeSwiper();
    }, 1000); // Espera 1 segundo para verificar de nuevo
}