// 后台删除用户的提示 是否删除
function doDel(ui){
    if(confirm("确定要删除吗？")){
    	//ui 获取的值： /myadmin/userdel/2
        //alert(ui)
        window.location=ui;
    }
}
