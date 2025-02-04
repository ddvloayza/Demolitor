var swiper = new Swiper('.swiper-container', {
    effect: 'coverflow',
    loop: false,
    allowTouchMove: true, // Permite el desplazamiento táctil
    spaceBetween: 100, // Espacio entre cada slide
    centeredSlides: true,
    slidesPerView: 'auto', // Número de slides visibles
    initialSlide: 1,
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },
    coverflow: {
        rotate: 0,
        stretch: 0,
        depth: 300,
        modifier: 1.5,
        slideShadows: false,
    },


});