$('#aa').click(function(){
	// alert('qiunima');
});


// 滚动事件
$(window).scroll(function(){
    // console.log("gun gun gun")
    
});



$(window).scroll(function(){
    // if($(window).width()>1024){
    // if($(window).scrollTop()>=150){
    //     $('#scroll_nav').slideDown();
    // }else{
    //     $('#scroll_nav').slideUp();
    // }
    // }else if($(window).width()<=1024){
    //     $('#scroll_nav').css('display','none');
    // }
    if($(window).scrollTop()>=120){
        // $('#scroll_nav').slideDown();
        // $('#scroll_nav').css({"position":"fixed","top":"0px"});.navbar-fixed-top
        $('#scroll_nav').attr("class","navbar-fixed-top");
    }else{
        // $('#scroll_nav').slideUp();
        $('#scroll_nav').removeAttr("class","navbar-fixed-top");
    }
});

