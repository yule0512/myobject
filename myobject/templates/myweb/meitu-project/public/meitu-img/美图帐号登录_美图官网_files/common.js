var MT = MT || {};
MT.win = $(window);

MT.doc = $(document);

MT.body = $(document.body);

MT.api = {

    account:'/users/isUserNameAvailable',
    login: '/users/login',
    isNameAvailable: '/users/isNameAvailable',
    register: '/users/register',
    reset_verify: '/users/send_reset_password_email_or_phone_verify_code',
    phone_verify_code: '/users/check_reset_password_verify_code',
    reset_password: '/users/resetPasswordInForgot',
    modify_password: '/users/resetPassword', 
	cancelbind: '/connect/unbind',
    update : '/users/update',
    set_username_password: '/users/set_username_password',
    verify_phone: '/users/verify_phone',
    login_verify_phone: '/verify_phone',
    send_verify_code_to_current_phone: '/users/send_verify_code_to_current_phone',
    send_verify_email_to_current_email: '/users/send_verify_email_to_current_email',
    unbind_email_or_phone : '/users/unbind_email_or_phone'
    
};


MT.code = {
    10114: '非法访问，请检查浏览器设置或联系管理员',
    10104:'该帐号已经注册',
	10105: '系统错误',
    20003: '请输入您的密码',
    20024: '旧密码错误',
    20031: '登录次数过多，请输入校验码',
    20725: '邮箱格式错误',
    20742: '密码不能为空',
    20743: '重复密码不能为空',
    20744: '两次输入密码不一致',
    20745: '该手机已被注册，<a href="/" target="_top" onclick=top.location.href="/">立即登录</a>',
    20746: '该邮箱已被注册，<a href="/" target="_top" onclick=top.location.href="/">立即登录</a>',
    20747: '该手机已被注册',
    20748: '该邮箱已被注册',
    20749: '该帐号已被注册',
    20750: '该手机号已被注册，请直接<a href="/logout" target="_top" onclick=top.location.href="/logout">登录</a>',
    20167: '验证码发送频率太快，请稍候再发',
    20198: '该帐号已被注册',
    20765: '验证码不能为空',
    20766: '验证码错误',
    20767: '验证码已失效，请重新发送',
    20158: '发送验证码每天最多三次',
    20160:'60秒内只能发送一次',
    22120: '请输入旧密码',
    22121: '不能为空',
    22122: '密码太长啦，最多16位',
    22123: '密码请勿使用特殊符号',
    22124: '',//重置错误信息勿删
    22125: '昵称不能为空',
    22126: '昵称至少4个字符或2个汉字',
    22127: '昵称最多20个字符或10个汉字',
    22128: '昵称不能含有#、@、空格、冒号、引号哦',
    22129: '支持中英文、数字、-或者“_”', 
    22130: '昵称不能以符号开头',
    22131: '邮箱不能为空',
    22132: '该邮箱地址过长',
    22133: '密码太短啦，最少6位',
    22134: '帐号不能为空',
    22135: '帐号格式错误',
    22140: '昵称已经存在',
    22141: '昵称中包含特殊字符',
    22145: '必须同意美图帐号服务条款',
    22150: '请选择性别',
    22151: '请选择你的生日',
    22152: '请选择你的所在地',
    22196: '手机号不能为空',
    22197: '手机号格式错误',
    22198: '格式错误，仅支持中国大陆手机号',
    22201: '本账号对应的美图手机已锁定，暂时不支持修改账号密码，请在解锁手机后再操作。',
    10107: '网络问题，请稍后重试', //服务器端的参数错误
	20015: '帐号或密码错误',
	20016: '帐号尚未注册，<a href="/register" target="_top" onclick=top.location.href="/register">立即注册</a>',
	20014: '密码错误',
    20199: '该帐号还未注册哦~',
    20728: '邮件发送失败',
    50051: '用户未设置登录邮箱',
    50159: '每天最多只能设置3次邮箱',
    50160: '每天最多只能设置3次手机号码'
};

// $.ajaxSetup({
//     xhrFields: {
//        withCredentials: true
//     },
//     crossDomain: true
// });

MT.register = function(){
    //register、reset_passwor、setting_password都调用了这里的focus,blur
    var flag_username, 
        flag_password, 
        flag_re_password,
        flag_verifycode,
        $form = $('#reg_form'),
        $username = $('#username'),
        $password = $('#password'),
        $re_password = $('#re_password'),
        $verifycode  = $('#verifycode');

    
    /* 帐号验证*/
    $username.blur(function(){

        /* reg_form的regtype 
          //已去除邮箱注册，所以不必维持regType,注册的账号验证都是验证phone  
          //@ZHY 20150418
        */
        var a = $form.attr('regtype'),
            $this = $(this);
        flag_username = MT.validate.phone($this);
        MT.tip.fn(flag_username,$this);
    })
    .focus(function(){
        MT.tip.hide($(this));
        MT.tip.hide($password);
    })/*
    .keyup(function(){
        var a = $('#reg_form').attr('regtype'),
            $this = $(this);
        if(a==0){
            flag_username = MT.validate.phone($this);
        }else{
            flag_username = MT.validate.mail($this);
        }
        MT.tip.fn(flag_username,$this);
    }); */

    /* 密码验证*/
    $password.blur(function(){
        flag_password = MT.validate.password();
        MT.tip.fn(flag_password,$password);
    })
    .focus(function(){
        MT.tip.hide($(this));

    });

    /* 重复密码验证*/
    $re_password.blur(function(){
        flag_re_password = MT.validate.re_password();
        MT.tip.fn(flag_re_password,$re_password);
    })
    .focus(function(){

        MT.tip.hide($(this));

    });

    /* 验证码 验证*/

    // $verifycode.blur(function(){
    //     flag_verifycode = MT.validate.verifycode();
    //     MT.tip.fn(flag_verifycode,$verifycode);
    // })
    // .focus(function(){

    //     MT.tip.hide($(this));

    // });
};

MT.login = function(){
    var flag_username, 
        flag_password, 
        $username = $('#username'),
        $password = $('#password');

    
    /* 帐号验证*/
    $username.blur(function(){
        var $this = $(this);
        flag_username = MT.validate.account();
        MT.tip.fn(flag_username,$this);
    })
    .focus(function(){
        
        MT.tip.hide($(this));
        if($(this).val()==''){
            MT.tip.hide($password);
        }

    });

    /* 密码验证*/
    $password.blur(function(){
        flag_password = MT.validate.password();
        MT.tip.fn(flag_password,$password);
    })
    .focus(function(){
        MT.tip.hide($(this));

    });
};




MT.tip = {

    hide: function(el){
        el.parents('.item').find('.tip').hide();
    },

    show: function(el){
        el.parents('.item').find('.tip').show();
        el.parents('.item').find('.icon-yes').remove();
        el.parents('.item').find('.des').show();
    },

    show_yes:function(el){
        var html = '<i class="icon icon-yes"></i>',
            $des = el.parents('.item').find('.des');
        $des.css('display','none');
        if(!el.parents('.item').find('.icon-yes')[0]){
            $des.before(html)
        }
        el.parents('.item').find('.icon-yes').css('display','inline-block');
    },

    text: function(el,t){
        el.parents('.item').find('.tip .error').html(t);
    },

    fn: function(flag, el, flag_text){
        if(flag){

            var text = (typeof(flag_text) == 'undefined' || flag_text == '') ? MT.code[flag] : flag_text;

            MT.tip.text(el, text);
            MT.tip.show(el);
        }else{
            MT.tip.hide(el);
            this.show_yes(el);
        }
    } 

};

MT.ajax = function (option) {
    if (option.btn) {
        if (option.btn.hasClass(option.cls)) {
            return;
        }
        option.btn.addClass(option.cls)
    };

    var async = true;

    if(typeof option.async != 'undefined'){

        async = option.async;
    }

    $.ajax({
        url: option.url,
        data: option.data || {},
        type: option.type || 'post',
        async: async,
        dataType: option.dataType || 'json',
        success: function (data) {

            if (option.btn) option.btn.removeClass(option.cls);

            if (data) {

                if(data.status=='ok'){

                    option.success(data);

                } else if (data.status == 10001) {
               
                   //未登录
                   location.href = 'http://id.meitu.com/';

                } else if(data.status == 10004){

                    location.href = data.redirect_uri;

                    return false;

                }else{

                    if(!option.failure)  return false;
                    if(!data.status || !MT.code[data.status]){

                        data.status = 10000;

                    }else{

                        if(data.status==10000){

                            MT.code[10000] = MT.code[11111] +'<br/>('+(data.error_code ? data.error_code : '未知错误')+')';
                        }

                        if(data.error){ //有传error优先使用error

                            MT.code[data.status] = data.error;

                        }

                    }
                    
                    option.failure(data);

                }

            }else{

                window.alert(MT.code[10000]);

                return false;
            }
            
        },
        error: function (data) {
            if (option.error) {

                option.error(data);

            }else{

               new MT.Dialog({

                    content: MT.code[10000],

                    title: '出错了'
                });
            }
            if (option.btn) option.btn.removeClass(option.cls);
        }
    });
};

MT.validate = {

    phone: function(el){

        var el = el || $('#username'),
            value = $.trim(el.val()),
            length = value.length,
            reg = /^1[34578]\d{9}$/,
            placeholder = $.trim(el.attr('placeholder'));

        if (length == 0 || value == placeholder) {
            return 22196;
        };

        if (!reg.test(value)) {
            return 22197;
        };

        if(this._account(value)){
            return 20745;
        };
        

        return false;
    },

    mail: function(el){
       var el = el || $('#username'),
            value = $.trim(el.val()),
            length = value.length,
            reg = /^[\w\-\.]+@[\w\-]+(\.[\w\-]+)+$/i,
            placeholder = $.trim(el.attr('placeholder'));

        if (length == 0 || value == placeholder) {
            return 22131;
        };

        if (!reg.test(value)) {
            return 20725;
        };

        if (length > 50) {
            return 22132;
        };

        if(this._account(value)){
            return 20749;
        }

        return false;
    },

    name: function(el){
       var el = el || $('#name'),
            value = $.trim(el.val()),
            length = value.length,
            byte_length = byteLength(value),
            reg = /^([\u4E00-\uFA29]|[\uE7C7-\uE7F3]|[a-zA-Z0-9]|_|-|)*$/,
            placeholder = $.trim(el.attr('placeholder'));

        if (length == 0 || value == placeholder) {
            return {'code':22125};
        };

        if(byte_length<4){
            return {'code': 22126};
        }

        if (byte_length > 20) {
            return {'code': 22127};
        };

        if(value.indexOf('@')!=-1 || value.indexOf(":")!=-1 || value.indexOf("：")!=-1 || value.indexOf(" ")!=-1 || value.indexOf("'")!=-1 || value.indexOf('"')!=-1){
            return {'code': 22128};
        }

        var code = false,error = false;

        $.ajax({
            url: MT.api.isNameAvailable,
            data: { name: value },
            type: 'get',
            dataType: 'json',
            async: false,
            success: function (data) {
                if (data.error_code) {
                    code = data.error_code; //昵称已经存在
                    error = data.error;
                }
            }
        });

        return {'code':code, 'error':error};
    },

    gender: function(el){

        var el = el || $('input:radio[name="gender"]:checked'),

            value = el.val();
        
        if(value){
            return false;
        }

        return 22150;
    },

    birthday:function(){

        var $year = $('#year'),
            $month = $('#month'),
            $day = $('#day'),
            y = $year.val(),
            m = $month.val(),
            d = $day.val();
        if(y == 0 || m == 0 || d == 0){
        
            return 22151;
        }

        return false;

    },

    local: function(){

        var $province = $('#province'),
            $city = $('#city'),
            province = $province.val(),
            city =$city.val();

        if(province==0 || city ==0 ){

            return 22152
        }

        return false;


    },

    account: function(el,a){

        var el = el || $('#username'),
            value = $.trim(el.val()),
            length = value.length,
            reg = /^[\w\-\.]+@[\w\-]+(\.[\w\-]+)+$/i,
            reg_phone = /^1[34578]\d{9}$/,
            placeholder = $.trim(el.attr('placeholder')),
            a = a || 1;
        if (length == 0 || value == placeholder) {
            return 22134;
        };

        if (!reg.test(value) && !reg_phone.test(value)) {
            return 22135;
        };

        if(a==3){  //用于第三方初次登录时的设置帐号

            if(this._account(value)){
                return 20749;
            }
        }

        return false;
    },

    password: function(el){
        var el = el || $('#password'),
            value = el.val(),
            length = value.length,
            reg = /^[\@A-Za-z0-9\!\@\#\$\%\^\&\*\.\~\/\\\{\}\|\(\)\'\"\?\>\<\,\.\`\+\-\=\_\[\]\:\;]+$/,
            placeholder = $.trim(el.attr('placeholder'));

        if(length == 0 || value == placeholder) {
            return 20742;
        }

        if (length < 6) {
            return 22133;
        }

        if (length > 16) {
            return 22122;
        }

        if (!reg.test(value)) {
            return 22123;
        }
        
        return false;
    },

    re_password: function(el){
        var el = el || $('#re_password'),
            value = el.val(),
            length = value.length;
        if(length == 0){
            return 20743;
        }

        if(value != $('#password').val()){
            return 20744;
        }
    },

    verifycode: function(el){
        var el = el || $('#verifycode'),
            value = $.trim(el.val()),
            length = value.length,
            placeholder = $.trim(el.attr('placeholder'));

        if (length == 0 || value == placeholder) {
            return 20765;
        };

        // var code = false;
        // $.ajax({
        //     url: MT.api.verifycode,
        //     data: { value: value },
        //     type: 'post',
        //     dataType: 'json',
        //     async: false,
        //     success: function (data) {
        //         if (data.error_code == "50043") { //验证码输入错误
        //             code = 20766;
        //         }
        //     }
        // });

        // return code;

        return false;
    },

    _account : function(value){
        var code = false;
        $.ajax({
            url: MT.api.account,
            data: { username: value },
            type: 'get',
            dataType: 'json',
            async: false,
            success: function (data) {
                if (data.error_code) {
                    code = true;
                }
            }
        });

        return code;
    }
};

//sso login logout
function sso_log_in_out(urls,goto_url,flag){

    var arr = urls.split('|'),
        len = arr.length;
	if($.trim(urls)==''){
		location.href = goto_url;
		return false;
	}
    var imgs = [];
    for(var i=0; i<len; i++){
        imgs[i] = new Image();
        (function(i){
            isComplete(imgs[i],function(){

                
                if(i==len-1){
                    setTimeout(function(){
                        
                        if(flag){
                            location.href = goto_url;
                        }else{

                            top.location.href = goto_url;

                        }


                    },100);
                }
            });
        })(i);
        imgs[i].src = arr[i];
    }
    
    function isComplete(img,callback){

        // if ($.browser.msie){      //ie
            
        //     img.onreadystatechange = function () {
        //         alert('ready')
        //         if (img.readyState == "complete"){
        //             alert(1)
        //             callback.call();
        //         }else{

        //             setTimeout(function(){
        //                 isComplete(img,callback)
        //             },200);
        //         }
        //     };
        // } else {
        //    //firefox
        //     img.onload = function () {

        //         if (img.complete == true){
        //            callback.call();
        //         }else{

        //              setTimeout(function(){
        //                 isComplete(img,callback)
        //             },200);
        //         }
        //     }
        // }
    
        if(img.complete || img.width>0){
                callback.call();
            } else{
            setTimeout(function(){
                isComplete(img,callback)
            },200);
        }
        
    }
};


function saveSuccess(t,btn){

    var html = '<span class="save-success" id="msg-success">'+ t +'</span>',
        $btn = btn || $('#btn');
    if(!$('#msg-success')[0]){

        $btn.after(html);
        
    }

    $('#msg-success').fadeIn(200,function(){

        setTimeout(function(){$('#msg-success').fadeOut();},2000);
        
    });
};

/*
function birthDay(y,m,d){
	var $day = $("#day"),
	$month = $("#month"),   
	$year = $("#year"); 

	var now = new Date(),
		cur_year = now.getFullYear(),
		str="",
		y = y || 0,
		m = m || 0,
		d = d || 0;
	for(var i=cur_year-50;i<cur_year+1;i++)
	{
		if(i==y){
			str="<option value="+i+" selected=true>"+i+"</option>";
		}else{
			str="<option value="+i+">"+i+"</option>";
		}
		$year.append(str);
	}

	for(var i=1;i<=12;i++){

		if(i==m)
		{
			str="<option value="+i+" selected=true>"+i+"</option>";
		}else{
			str="<option value="+i+">"+i+"</option>";
		}
		$month.append(str);
	}
	changeDay(y,m,d);
	
	//现改由PHP输出年月日

}*/
	
	
	function getDaysInMonth(m, y) {
		var daysInMonth = new Date(y, m, 0);
		return daysInMonth.getDate();
	};
	function changeDay(y,m,d) {
		var now = new Date(),
			days = getDaysInMonth(m, y),
			d = d || 0,
			$day= $('#day');
		$day.html('<option value="0"> 日 </option>'); 

		for (var i = 1; i <= parseInt(days); i++) {

            var di = i<10 ? ('0'+i) : i, str;

			if(i==d){
                
				str="<option value="+di+" selected=true> "+i+" </option>";
			}else{

				str="<option value="+di+"> "+i+" </option>";
			}
			$day.append(str);
		}
	};

    function byteLength(str){
        if(typeof str == "undefined"){
            return 0;
        }
        var aMatch = str.match(/[^\x00-\x80]/g);
        return (str.length + (!aMatch ? 0 : aMatch.length));
    };




/*
    
    * 验证弹窗
    * 用于邮箱验证、和手机验证的
    * 帐号管理页面 、 第三方平台初次登录帐号设置页
*/

function verifyMail(data){

    var username = data.username,
        captcha = data.captcha || '',

        d = data.dialog || function(){},

        cb = data.callback || function(){},

        fcb = data.fcallback || function(){},

        api_url = MT.api.set_username_password,

        title = '验证邮箱',

        ajax_data = data.ajax_data ||  { username : username,captcha:captcha}; //传ajax_data的情况只在 第三方平台初次登录时设置帐号用

    if(data.action_type == 'verify'){ //验证邮箱,区分于设置邮箱

        api_url = MT.api.send_verify_email_to_current_email;

        title = '验证邮箱' ;

    }


    if(data.old_password){  //用于更改邮箱、更改手机的情况

        ajax_data.old_password = data.old_password;
    }

    $.post( api_url, ajax_data ,

        function(data){

            cb();

            if( data && !data.error_code){

                if(d.close){

                    d.close();
                }

                var mail_url = '请到您的邮箱中查看邮件';

                if(data.url){

                    mail_url = '<a href="'+ data.url +'" class="d-btn d-ok" id="btn" target="_blank" style="padding:8px 18px;">点击查看邮箱</a>'
                }


                var h = '<div class="dialog-content-inner" id="dialog-content-inner" style="line-height:24px;">验证邮件已发送至你的邮箱'+ username +'，<br/>点击邮件里的激活链接即可验证美图帐号。\
                    <p style="margin-top:12px;">'+ mail_url +'</p>\
                    <p style="margin-top:15px"><span></span></p>\
                    </div>';
                

                var vbox = new MT.Dialog({

                    content: h,

                    title: title,

                    width: 400
                });
                

            }else{

                fcb(MT.code[data.error_code]);

            }
        },

        'json'
    );

}

/*
 *niubility system
*/

function verifyPhone(data){

    var username = data.username,

        d = data.dialog || function(){},

        cb = data.callback || function(){},

        fcb = data.fcallback || function(){},

        send_phone_api_url = MT.api.set_username_password,

        title = '验证手机',

        send_phone_ajax_data = data.ajax_data ||  { username : username}, //传ajax_data的情况只在 第三方平台初次登录时设置帐号用;

        sure_btn_submit_url = MT.api.verify_phone,  //点确定按钮，提交到服务的url

        sure_btn_additional_data = {},

        data_action_type  = data.action_type || '';



    if(data_action_type == 'verify'){ //验证手机,区分于设置手机

        send_phone_api_url = MT.api.send_verify_code_to_current_phone;
        title = '验证手机';
    } else if (data_action_type == 'logged_change_password') {
        title = '修改密码';
        send_phone_api_url = MT.api.send_verify_code_to_current_phone + '?type=logged_change_password';
        sure_btn_additional_data = data.submit_additional_data;
        sure_btn_submit_url = data.submit_url;
    }

    if(data.old_password){
        send_phone_ajax_data.old_password = data.old_password;
    }


    $.post( send_phone_api_url, send_phone_ajax_data,

        function(data){

            cb();

            if( data && !data.error_code){

                if(d.close){

                    d.close();
                }

                var h = '<div class="dialog-content-inner" id="dialog-content-inner" style="line-height:24px;">已向您的手机'+ username +'发送了短信验证码，输入<br/>验证码后即可验证手机号。\
                    <p style="margin-top:12px;">验证码：<input type="text" id="d-verifycode" class="textbox"/> <a href="javascript:;" class="d-btn d-ok" id="d-btn">确定</a></p>\
                    <p><span class="error"></span></p>\
                    <p>您如果没有收到短信<button class="btn-send" style="padding:6px 8px;margin-left:6px;" disabled>再次发送(60)</button></p></div>';

                var vbox = new MT.Dialog({

                    content: h,

                    title: title,

                    width: 400,

                    init: function(){

                        var $verifycode = $('#d-verifycode'),

                            $content = $('#dialog-content-inner'),

                            $err = $content.find('.error'),

                            $send = $content.find('.btn-send'),

                            $btn  = $('#d-btn');

                        /* 60秒后 重新发送按钮*/
                        var s=60, i = s;
                        timer();

                        $verifycode.focus(function(){

                            $err.html('');

                        }).keyup(function(e){

                            if(e.keyCode == 13) {

                               $btn.click();
                            }

                        });

                        //提交按钮
                        $btn.click(function(){

                            var verifycode = $.trim($verifycode.val());

                            if(verifycode == '' || $btn.hasClass('disable') ) return false;

                            $btn.addClass('disable');

                            sure_btn_additional_data.verify_code = verifycode;

                            $.post( sure_btn_submit_url,

                                sure_btn_additional_data
                                ,

                                function(data){

                                    $btn.removeClass('disable');

                                    if(data && !data.error_code){

                                        vbox.close();


                                        new MT.Dialog({

                                            content:   (data_action_type == 'logged_change_password')  ? '密码修改成功': '手机验证成功!'

                                        });

                                        setTimeout(function(){

                                            location.reload();

                                            return false;

                                        },2000);

                                    } else {
                                        var error = data.error ? data.error : MT.code[data.error_code];
                                        $err.html(error);

                                    }

                                },

                                'json'
                            );

                        });

                        
                        
                        function timer(){
                            if(i<=0){
                                $send.html('再次发送').removeAttr('disabled');
                                return false;
                            }else{

                                $send.html('再次发送('+i+')').attr('disabled',true);
                            }
                            i--;
                            setTimeout(timer,1000);
                        }
                        
                        $send.click(function(){

                            var $this = $(this);

                            if($this.attr('disabled')) return false;

                            $this.attr('disabled',true);

                             $.post(send_phone_api_url, send_phone_ajax_data, function(data){

                                i=s;

                                timer();
                                var str = '发送成功!';
                                if(data && data.error_code){

                                    str = data.error ? data.error : MT.code[data.error_code];

                                }
                                new MT.Dialog({
                                    content:str
                                })
                             },'json');
                        });
                    }
                });

            } else {

                var error = data.error ? data.error : MT.code[data.error_code];

                 fcb(error);

            }
        },

        'json'
    );

}


MT.Dialog = (function ($, MT) {
    var dialog = function (opa) {
        this._opa = {
            title: null,
            content: null,
            masterplate: null,
            ok: null,
            cancel: null,
            close: null,
            time: 1500,
            width: 300,
            offsetTop: 0,
            zIndex: 9
        };
        this._init(opa)._create()._event()._position();
    };
    dialog.prototype = {
        _init: function (opa) {

            $.extend(this._opa, opa);

            var btn = {
                ok: this._opa.ok,
                cancel: this._opa.cancel
            },
            txt = {
                ok: '确定',
                cancel: '取消',
                title: '提示'
            }, isObj = function (obj) {
                return obj !== null && typeof obj === 'object';
            },
            isFn = function (obj) {
                return typeof obj === 'function';
            };


            if (isObj(btn.ok) && !btn.ok.value) {
                this._opa.ok.value = txt.ok;
            } else if (isFn(btn.ok)) {
                this._opa.ok = {
                    value: txt.ok,
                    fn: btn.ok
                };
            };

            if (isObj(btn.cancel) && !btn.cancel.value) {
                this._opa.cancel.value = txt.cancel;
            } else if (isFn(btn.cancel)) {
                this._opa.cancel = {
                    value: txt.cancel,
                    fn: btn.cancel
                };

            };

            if ((btn.ok || btn.cancel) && !this._opa.title) {
                this._opa.title = txt.title;
            }

            return this;
        },
        _create: function () {
            var t = [], id = new Date().getTime(), hasTitle = this._opa.title, hasOk = this._opa.ok, hasCancel = this._opa.cancel;
            this._id = id;
            t.push('<div id="l' + id + '" class="dialog-layout" style="z-index:' + this._opa.zIndex + '"></div>');
            t.push('<div id="d' + id + '" class="dialog bounceInDown" style="width:' + parseInt(this._opa.width, 10) + 'px;z-index:' + (this._opa.zIndex + 1) + '">');
            if (hasTitle) {
                t.push('<div id="t' + id + '" class="d-title" unselectable="on">');
                t.push('<span>' + this._opa.title + '</span>');
                t.push('<a id="c' + id + '" class="d-close" href="javascript:;" title="关闭"></a>');
                t.push('</div>');
            };
            t.push('<div class="d-content d-bg">');
            if (this._opa.content) {
                t.push('<div class="d-c-p">' + this._opa.content + '</div>');
            } else if (this._opa.masterplate) {
                t.push(this._opa.masterplate);
            };
            t.push('</div>');
            if (hasOk || hasCancel) {
                t.push('<div class="d-bottom d-bg">');
                if (hasOk) {
                    t.push('<a id="ob' + id + '" href="###" class="d-ok d-btn" title="' + this._opa.ok.value + '">' + this._opa.ok.value + '</a>');
                };
                if (hasCancel) {
                    t.push('<a id="cb' + id + '" href="###" class="d-cancle d-btn" title="' + this._opa.cancel.value + '">' + this._opa.cancel.value + '</a>');
                }
                t.push('</div>');
            };
            t.push('</div>');
            $(document.body).append(t.join(''));
            return this;
        },
        _position: function () {
            var $win = MT.win, $doc = MT.doc, $dialog = $('#d' + this._id),
                left = ($win.width() - $dialog.width()) / 2,
                top = ($win.height() - $dialog.height()) / 2,
                sTop = $doc.scrollTop(),
                sLeft = $doc.scrollLeft(),
                top = top + sTop - this._opa.offsetTop;
            $dialog.css({ left: left + sLeft, top: top > 0 ? top : 0 });
            var init = this._opa.init;
            if (init && typeof init === 'function') {
                init();
            };
        },
        _event: function () {
            var self = this, id = this._id, hasTitle = this._opa.title, hasOk = this._opa.ok, hasCancel = this._opa.cancel;
            var btnok = null, btncancel = null;
            if (hasTitle) {
                new MT.Drag('t' + id);
                this._close = function () {
                    $(this).unbind('click');
                    if (hasOk) {
                        btnok.unbind('click')
                    };
                    if (hasCancel) {
                        btncancel.unbind('click')
                    };
                    self._remove();
                };
                $('#c' + id).click(self._opa.close ? self._opa.close : self._close);
            } else {
                setTimeout(function () {
                    self._remove();
                }, self._opa.time);
            };
            if (hasOk) {
                btnok = $('#ob' + id).click(function () {
                    if (self._opa.ok.fn) {
                        self._opa.ok.fn();
                    }
                    return false;
                });
            };
            if (hasCancel) {
                btncancel = $('#cb' + id).click(function () {
                    if (self._opa.cancel.fn) {
                        self._opa.cancel.fn();
                    }
                    return false;
                });
            };
            return this;
        },
        _remove: function () {
            var id = this._id,
             l = document.getElementById('l' + id),
             d = document.getElementById('d' + id);

            if (d) {
                document.body.removeChild(d);
            }
            if (l) {
                document.body.removeChild(l);
            }
        },
        close: function () {
            if (this._close) {
                this._close.call(document.getElementById('c' + this._id));
            };
        }
    };
    return dialog;
})(jQuery, MT);

MT.Drag = (function ($, MT) {
    var drag = function (id) {
        this.instance = document.getElementById(id);
        if (this.instance) {
            this.point = { offsetX: 0, offsetY: 0, left: 0, top: 0, l: 0, t: 0, offset: 8 };
            this.dialog = this.instance.parentNode;
            this.instance = $(this.instance);
            this._mousedown()._mouseup();
        }
    };
    drag.prototype = {
        _mousedown: function () {
            var self = this, $win = MT.win, $dia = $(self.dialog);
            self.instance.mousedown(function (e) {
                var point = self.point;
                point.l = $win.width() - $dia.width() - point.offset + $win.scrollLeft();
                point.t = $win.height() - $dia.height() - point.offset + $win.scrollTop();
                point.offsetX = e.clientX - self.dialog.offsetLeft;
                point.offsetY = e.clientY - self.dialog.offsetTop;
                MT.doc.mousemove(self._move).mouseup(self._dmouseup);
            });
            this._move = function (e) {
                var point = self.point;
                point.left = e.clientX - point.offsetX;
                point.top = e.clientY - point.offsetY;
                point.left = point.left > point.l ? point.l : point.left < 0 ? 0 : point.left;
                point.top = point.top > point.t ? point.t : point.top < 0 ? 0 : point.top;
                self.dialog.style.left = point.left + 'px';
                self.dialog.style.top = point.top + 'px';
            };
            return this;
        },
        _mouseup: function () {
            var self = this;
            this._dmouseup = function () {
                MT.doc.unbind('mousemove', self._move)
                           .unbind('mouseup', self._dmouseup);
            };
            return this;
        }
    };
    return drag;
})(jQuery, MT);

;(function($) {
    function Placeholder(input) {
        this.input = input;
        if (input.attr('type') == 'password') {
            this.handlePassword();
        }
        // Prevent placeholder values from submitting
        $(input[0].form).submit(function() {
            if (input.hasClass('placeholder') && input[0].value == input.attr('placeholder')) {
                input[0].value = '';
            }
        });
    }
    Placeholder.prototype = {
        show : function(loading) {
            // FF and IE saves values when you refresh the page. If the user refreshes the page with
            // the placeholders showing they will be the default values and the input fields won't be empty.
            if (this.input[0].value === '' || (loading && this.valueIsPlaceholder())) {
                if (this.isPassword) {
                    try {
                        this.input[0].setAttribute('type', 'text');
                    } catch (e) {
                        this.input.before(this.fakePassword.show()).hide();
                    }
                }
                this.input.addClass('placeholder');
                this.input[0].value = this.input.attr('placeholder');
            }
        },
        hide : function() {
            if (this.valueIsPlaceholder() && this.input.hasClass('placeholder')) {
                this.input.removeClass('placeholder');
                this.input[0].value = '';
                if (this.isPassword) {
                    try {
                        this.input[0].setAttribute('type', 'password');
                    } catch (e) { }
                    // Restore focus for Opera and IE
                    this.input.show();
                    this.input[0].focus();
                }
            }
        },
        valueIsPlaceholder : function() {
            return this.input[0].value == this.input.attr('placeholder');
        },
        handlePassword: function() {
            var input = this.input;
            input.attr('realType', 'password');
            this.isPassword = true;
            // IE < 9 doesn't allow changing the type of password inputs
            if ($.browser.msie && input[0].outerHTML) {
                var fakeHTML = $(input[0].outerHTML.replace(/type=(['"])?password\1/gi, 'type=$1text$1'));
                this.fakePassword = fakeHTML.val(input.attr('placeholder')).addClass('placeholder').focus(function() {
                    input.trigger('focus');
                    $(this).hide();
                });
                $(input[0].form).submit(function() {
                    fakeHTML.remove();
                    input.show()
                });
            }
        }
    };
    var NATIVE_SUPPORT = !!("placeholder" in document.createElement( "input" ));
    $.fn.placeholder = function() {
        return NATIVE_SUPPORT ? this : this.each(function() {
            var input = $(this);
            var placeholder = new Placeholder(input);
            placeholder.show(true);
            input.focus(function() {
                placeholder.hide();
            });
            input.blur(function() {
                placeholder.show(false);
            });

            // On page refresh, IE doesn't re-populate user input
            // until the window.onload event is fired.
            if ($.browser.msie) {
                $(window).load(function() {
                    if(input.val()) {
                        input.removeClass("placeholder");
                    }
                    placeholder.show(true);
                });
                // What's even worse, the text cursor disappears
                // when tabbing between text inputs, here's a fix
                input.focus(function() {
                    if(this.value == "") {
                        var range = this.createTextRange();
                        range.collapse(true);
                        range.moveStart('character', 0);
                        range.select();
                    }
                });
            }
        });
    }
})(jQuery);

$('input[placeholder][type=text]').placeholder();




