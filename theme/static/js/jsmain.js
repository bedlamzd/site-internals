$('.sl').slick(
{
  slidesToShow:1,
  autoplay:true,
  autoplaySpeed:2000,
  speed:1000,
  dots: true,
  arrows: false,
}
);

$('.projects').slick({
  dots: true,
  arrows: false,
  infinite: false,
  speed: 300,
  slidesToShow: 4,
  slidesToScroll: 4,
  responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 3,
        infinite: true,
        dots: true
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 2
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
    // You can unslick at a given breakpoint now by adding:
    // settings: "unslick"
    // instead of a settings object
  ]
});

$(window).scroll(function(){
	if($(this).scrollTop() > $(this).height()) {
		$(".top").addClass("active");
	} else {
		$(".top").removeClass("active");
	}
});

$(".top").click(function(){
	$("html, body").stop().animate({scrollTop: 0}, "slow", "swing");
});
