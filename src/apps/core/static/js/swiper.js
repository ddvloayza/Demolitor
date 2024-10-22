function initializeSwiper() {
    var swiper = new Swiper('.swiper-container.two', {
        pagination: '.swiper-pagination',
        paginationClickable: false,
        effect: 'coverflow',
        loop: false,
        centeredSlides: true,
        slidesPerView: 'auto',
        initialSlide: 1,
        coverflow: {
            rotate: 0,
            stretch: 0,
            depth: 300,
            modifier: 1.5,
            scale: 1,
            slideShadows: false,
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