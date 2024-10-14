
var swiper = new Swiper( '.swiper-container.two', {
		pagination: '.swiper-pagination',
		paginationClickable: true,
		effect: 'coverflow',
		loop: false,
		centerInsufficientSlides: true,
		centeredSlides: true,
		slidesPerView: 'auto',
		initialSlide: 1,
		coverflow: {
			rotate: 0,
			stretch: 0,
			depth: 300,
			modifier: 1.5,
			scale: 1,
			slideShadows : false,
		}
} );
