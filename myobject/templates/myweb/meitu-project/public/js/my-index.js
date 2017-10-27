//当鼠标移入 商品div中时

$('.info2').mouseenter(function(){
	$(this).find('.isimgdiv').css("border","12px solid #fff");
	// $(this).find('p').fadeOut(500);
	// $(this).find('p').css("font-size","18");
	// $(this).find('span').css("font-size","25px")
	$(this).find('.price').css("color","red")
})
$('.info2 .isimgdiv').mouseleave(function(){
	$('.info2 .isimgdiv').css("border","0px solid #fff");
	$('.info2 .price').css("color","black")
	// $('.info2 p').fadeOut(500);
	// $('.info2 .price').css("font-size","30px;")
})