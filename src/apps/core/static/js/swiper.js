document.addEventListener("DOMContentLoaded", function () {
    function initializeSwiper() {
        var swiperConfig = {
            pagination: '.swiper-pagination',
            paginationClickable: true,
            spaceBetween: 30,
            effect: 'coverflow',
            loop: false,
            centeredSlides: true,
            slidesPerView: 'auto',
            nextButton: '.swiper-button-next',
            prevButton: '.swiper-button-prev',
            initialSlide: 1,
            coverflow: {
                rotate: 0,
                stretch: 0,
                depth: 300,
                modifier: 1.5,
                slideShadows: false,
            }
        };

        // Detecta el tamaño de la pantalla y ajusta las propiedades
        if (window.innerWidth >= 768) {
            swiperConfig.slidesPerView = 5; // Cambia a 3 diapositivas en pantallas más grandes
        }

        // Inicializa el Swiper con la configuración seleccionada
        var swiper = new Swiper('.swiper-container.two', swiperConfig);
    }

    // Verifica que las diapositivas se hayan cargado
    if (document.querySelectorAll('.swiper-slide').length > 0) {
        initializeSwiper();
    } else {
        setTimeout(function() {
            initializeSwiper();
        }, 1000);
    }

    // Detecta cambios en el tamaño de la ventana para ajustar el Swiper
    window.addEventListener('resize', function() {
        var swiper = document.querySelector('.swiper-container.two').swiper;
        if (window.innerWidth >= 768) {
            swiper.params.slidesPerView = 5; // Cambia a 3 diapositivas
        } else {
            swiper.params.slidesPerView = 'auto'; // Cambia a diapositivas automáticas en pantallas pequeñas
        }
        swiper.update(); // Actualiza el Swiper con los nuevos parámetros
    });
});