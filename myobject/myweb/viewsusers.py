from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse,JsonResponse
from django.core.urlresolvers import reverse

from myweb.models import Users,Types,Orders,Detail,Goods

import time

# 公共信息加载数据 pid=0 获取一级的商品类型,每个需要显示类别菜单的页面都调用该函数
def loadContext(request):
    context={}
    context['typelist'] = Types.objects.filter(pid=0)
    return context


# 登录
def dologin(request):
	# try:
	# 验证码验证 获取验证码 
	verifycode = request.session['verifycode']
	yanzheng = request.POST['yanzheng']
	if yanzheng == "":
		context = {"infocheck":"验证码不能为空！"}
		return render(request,"myweb/login.html",context)
	if verifycode != yanzheng:
		context = {"infocheck":"请输入正确的验证码！"}
		return render(request,"myweb/login.html",context)

	# 查询用户名
	user = Users.objects.get(username = request.POST['username'])
	
	# 检测密码
	# 获取输入的密码并MD5
	import hashlib
	m = hashlib.md5()
	m.update(bytes(request.POST['password'],encoding="utf8"))
	pwd = m.hexdigest()
	if user.password == pwd:
		# isuser = {
		# 	"username":user.username,
		# 	"name":user.name,
		# 	"address":user.address,
		# 	"code":user.code,
		# 	"email":user.email,
		# 	"phone":user.phone,
		# 	"sex":user.sex,
		# }
		# 将登陆的用户信息放入session
		# request.session['user'] = {'username':user.username,'name':user.name,"address":user.address,"code":user.code,"email":user.email,"phone":user.phone,"sex":user.sex}
		request.session['user'] = user.userDict()
		# 重定向到主页
		return redirect(reverse('index'))
	else:
		# 密码错误
		context = {"infocheck":"请输入正确密码！"}
	# except:
		# context = {"infocheck":"请输入有效账户"}

	return render(request,"myweb/login.html",context)

# 退出
def loginout(request):
	# 清除user缓存
	del request.session['user']

	# 清除购物车缓存

	return render(request,"myweb/index.html")
# 注册
def userinsert(request):
	try:
		ob = Users()
		ob.username = request.POST['username']

		# 获取密码  并 md5
		import hashlib
		m = hashlib.md5()
		m.update(bytes(request.POST['password'],encoding="utf8"))
		# print(m.hexdigest())
		
		ob.password = m.hexdigest()
		#ob.password = request.POST['password']

		ob.username = request.POST['username']
		ob.email = request.POST['email']
		# 状态默认1 启用
		ob.state = 1
		# 设置当前时间
		ob.addtime = time.time()

		ob.save()
		context = {"info":"注册成功成功！","label":"立即登录"}
	except:
		context = {"info":"注册失败！"}

	return render(request,"myweb/info.html",context)




# 登录验证码
def showcode(request):
    #引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定义变量，用于画面的背景色、宽、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (222,244,247)
    width = 100
    height = 25
    #创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    #创建画笔对象
    draw = ImageDraw.Draw(im)
    #调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    #定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    #随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    #构造字体对象，ubuntu的字体路径为“/usr/share/fonts/truetype/freefont”

    font = ImageFont.truetype('static/STXIHEI.TTF', 22)

    #font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor1 = (255, random.randrange(0, 25), random.randrange(0, 255))
    fontcolor2 = (255, random.randrange(0, 255), random.randrange(0, 255))
    fontcolor3 = (255, random.randrange(0, 255), random.randrange(0, 255))
    #绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor1)
    draw.text((25, 0), rand_str[1], font=font, fill=fontcolor2)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor3)
    draw.text((75, 0), rand_str[3], font=font, fill=fontcolor2)
    #释放画笔
    del draw


    #存入session，用于做进一步验证
    request.session['verifycode'] = rand_str


    """
    python2的为
    # 内存文件操作
    import cStringIO
    buf = cStringIO.StringIO()
    """
    # 内存文件操作-->此方法为python3的
    import io
    buf = io.BytesIO()
    #将图片保存在内存中，文件类型为png
    im.save(buf, 'png')
    #将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(buf.getvalue(), 'image/png')






# 个人中心
# 根据传入的用户ID查询
def mycenter(request,uid):
	context = loadContext(request)
	# print(uid)
	user = Users.objects.get(id = uid)
	context['user'] = {"uname":user.username,"name":user.name,"phone":user.phone,"address":user.address,"email":user.email}

	return render(request,"myweb/mycenter.html",context)


# 查看订单
def myorder(request,userid):
	context = loadContext(request)
	# print(userid)
	# context['orders'] = Orders.objects.filter(uid = uid)
	#获取当前用户下的所有订单信息

	# 只查订单id  根据当前用户查询
    # 订单详情 查询 当前用户下的订单
	# odb = Orders.objects.only('id').filter(uid = userid)
 #    deb = Detail.objects.filter(orderid__in = Orders.objects.only('id').filter(uid = userid))
 #    # 存储订单详情中的商品ID
	# gob = []
 #    for debone in deb:
	# 	gob.append(debone.goodsid)
 #    # 根据ID 查询出当前用户购买的所有商品
 #    goodslist = Goods.objects.filter(id__in=gob)
 #    content = {'orderlist':odb,'detaillist':deb,'goodslist':goodslist}


    # 查询所有订单
	context['orders'] = Orders.objects.filter(uid = userid)
	return render(request,"myweb/myorder.html",context)


# def myorderDetail(request):
# 	context = loadContext(request)

#     deb = Detail.objects.filter(orderid__in = Orders.objects.only('id').filter(uid = request.session['user']['id']))
#     gob = []
#     for debone in deb:
#     	gob.append(debone.goodsid)
#     goodslist = Goods.objects.filter(id__in=gob)
#     context = {"goodslist":goodslist}
# 	return render(request,"myweb/myorderDetail.html",context)

def myorderDetail(request,oid):
    #获取当前用户下的所有订单信息
    odb = Orders.objects.filter(id = oid)
    # deb = Detail.objects.filter(orderid__in = Orders.objects.only("id").filter(uid = request.session['user']['id']))
    deb = Detail.objects.filter(orderid__in = Orders.objects.only("id").filter(id = oid))
    gob = []
    for debone in deb:
        gob.append(debone.goodsid)
    goodslist = Goods.objects.filter(id__in=gob)
    content = {'orderlist':odb,'detaillist':deb,'goodslist':goodslist}
    return render(request,'myweb/myorderDetail.html',content)