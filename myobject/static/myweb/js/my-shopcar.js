
// 商品总价格
// window.onload=function(){
// 	// shuliang
//     var n = $('#num');
//     var x = document.getElementsByName('xiaoji');
//     var result = 0;
//     var num = 0;
//     for (var i = x.length - 1; i >= 0; i--) {
//         // console.log($(n[i]).text());
//         // console.log($(x[i]).val());
//         result = result +  parseInt($(x[i]).text());
//         num = num +  parseInt(n.val());
//     };
//     $('#countprice').html(result);
//     $('#countnum').html(num);
// }



/*购物车--------------------------------------------*/ 

//选择框操作
function allSelect(){
  var aee = false;
  var see = false;
  // 全选 按钮单击事件
  $('#quanxuan').click(function(){
  	// alert('nmb')
    if(aee==false){
      //  所有的input checkbox 加上选中
      $("input[type='checkbox']").attr("checked", true);
      aee = true;
    }else if(aee==true){
      // 反选
      $("input[type='checkbox']").attr("checked", false);
      aee = false;
    }
    loadTotal();
  })

  //单选  没点击一下单选 统计一下价格
  $('#danxuan').click(function(){
    if(see==false){
      $(this).attr("checked", true);
      see = true;
    }else if(see==true){
      $(this).attr("checked", false);
      see = false;
    }
    loadTotal();
  })
}

//计算商品数量和总金额   这是总共的金额  不是根据单选计算  后期再改
function loadTotal(){
    var n = $('#num');
    var x = document.getElementsByName('xiaoji');
    var result = 0;
    var num = 0;
    for (var i = x.length - 1; i >= 0; i--) {
        result = result +  parseInt($(x[i]).text());
        num = num +  parseInt(n.val());
    };
    $('#countprice').html(result);
    $('#countnum').html(num);
}






// // 单选
// function func(num){
// 	var lives = document.getElementsByTagName('input');

// 	for (var i = 0;i<lives.length; i++) {
// 		console.log(lives[i]);
// 			switch(num){
// 				case 1:
// 					//全选
// 					lives[i].checked = true;
// 					break;
// 				case 2:
// 					lives[i].checked = false;
// 					break;
// 				case 3:
// 					lives[i].checked = !lives[i].checked;
// 					break;
// 			}
// 		}
// }



