# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse,JsonResponse
from django.core.urlresolvers import reverse

# 分页模块
from django.core.paginator import Paginator
# Create your views here.

from myadmin.models import Users

import time,json

# 返回主页
def index(request):
	return render(request,'myadmin/index.html')

# =======================
# 登陆
# 
# 1.跳转登录模板
def login(request):
	return render(request,"myadmin/login.html")

#2.登录操作  将登录信息添加进缓存  
#            验证码验证
def dologin(request):
	
	try:
		# 验证账号是否为空
		if request.POST['username'] == "":
			context= {"infocheckusername":"用户名不能为空"}
			return render(request,"myadmin/login.html",context)
		user = Users.objects.get(username = request.POST['username'])

		# 检测是否是管理员
		if user.state == 0:
			# 检测密码
			# 获取输入的密码并MD5
			import hashlib
			m = hashlib.md5()
			m.update(bytes(request.POST['password'],encoding="utf8"))
			pwd = m.hexdigest()

			if user.password == pwd:
				# 将查询到的用户信息存放到session 按需存放
				isuser = {
					# "id":request.POST['id'],
					"username":user.username,
					"name":user.name,
					"state":user.state,
					"email":user.email,
				}
				# request.session['adminuser'] = user.name
				request.session['adminuser'] = {'username':user.username,'name':user.name}
				# 登录无误，重定向到主页面
				return redirect(reverse('myadmin_index'))
			else:
				context = {"infocheckpwd":"密码有误！"}
		else:
			context= {"infocheckusername":"该账户不是管理员账户！"}

		# 获取随机生成 并且存在 缓存中的验证信息
		verifycode = request.session['verifycode']
		# 获取表单输入的验证码
		code = request.POST['code']
		if code == "":
			context = {"infocheckimg":"验证码不能为空！"}
			return render(request,"myadmin/login.html",context)
		if verifycode != code:
			context = {"infocheckimg":"请输入正确验证码！"}
			return render(request,"myadmin/login.html",context)
	except:
		context = {"infocheckusername":"账号有误！"}
	return render(request,"myadmin/login.html",context)




# 登陆成功，将登录信息放入session，并跳转首页
# 将登录着信息统计整理成json格式 放入session
# isuser = {
# 	'id':request.POST['id'],
# 	'username':request.POST['username'],
# 	'name':request.POST['name'],
# 	'address':request.POST['address'],
# 	'code':request.POST['code'],
# 	'phone':request.POST['phone'],
# 	'sex':request.POST['sex'],
# 	'state':request.POST['state'],
# 	'email':request.POST['email'],
# }

# 3.退出登陆  清除缓存中的登录信息
def logout(request):
	del request.session['adminuser']
	return render(request,"myadmin/login.html")




# ==================用户管理============================


# 浏览用户
def usersindex(request,pIndex):
	#分页显示用户
	list = Users.objects.filter()
	p = Paginator(list,5)
	if pIndex == "":
		pIndex = '1'
	pIndex  = int(pIndex)
	list2 = p.page(pIndex)
	plist = p.page_range
	#context = {'userlist':list2,'pIndex':pIndex,'plist':plist}
	#return render(request,"myadmin/users/index.html",context)
	return render(request,"myadmin/users/index.html",{'userlist':list2,'pIndex':pIndex,'plist':plist})

	#显示所有用户
    # list = Users.objects.all()
    # context = {"userlist":list}
    # return render(request,"myadmin/users/index.html",context)

# def userjia(request,pIndex):

# 	#分页显示用户
# 	list = Users.objects.filter()
# 	p = Paginator(list,5)
# 	if pIndex == "":
# 		pIndex = '1'
# 	pIndex  = int(pIndex)
# 	list2 = p.page(pIndex+1)
# 	plist = p.page_range
# 	context = {'userlist':list2,'pIndex':pIndex,'plist':plist}
# 	return render(request,"myadmin/users/index.html",context)






# 添加用户表单
def useradd(request):
	return render(request,'myadmin/users/add.html')

# 添加用户
def userinsert(request):
	try:
		ob = Users()
		ob.username = request.POST['username']

		# 获取密码  并 md5
		import hashlib
		m = hashlib.md5()
		m.update(bytes(request.POST['password'],encoding="utf8"))
		print(m.hexdigest())
		ob.password = m.hexdigest()

		#ob.password = request.POST['password']

		ob.name = request.POST['isname']
		ob.sex = request.POST['sex']
		ob.phone = request.POST['phone']
		ob.email = request.POST['email']
		ob.address = request.POST['address']
		ob.code = request.POST['code']	

		# 状态默认1 启用
		ob.state = 1
		# 设置当前时间
		# ob.addtime = time.time()
		ob.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
		print(ob.addtime)
		ob.save()
		context = {"info":"添加成功！"}
	except:
		context = {"info":"添加失败！"}
	return render(request,"myadmin/info.html",context)



# 删除
def userdel(request,uid):

	try:
		db = Users.objects.get(id = uid)
		db.delete()
		context = {"info":"删除成功！"}
	except:
		context ={"info":"删除失败！"}
	return render(request,"myadmin/info.html",context)


# 获取要编辑的信息，显示在编辑表单
def useredit(request,uid):

	theuser = Users.objects.get(id = uid)
	context = {"user":theuser}

	return render(request,"myadmin/users/edit.html",context)


# 修改编辑信息
def userupdate(request,uid):
	try:
		user = Users.objects.get(id = uid)
		user.name = request.POST['isname']
		user.sex = request.POST['sex']
		user.phone = request.POST['phone']
		user.email = request.POST['email']
		user.address = request.POST['address']
		user.code = request.POST['code']
		user.state = request.POST['state']
		user.save()
		context = {"info":"修改成功！"}
		return render(request,"myadmin/info.html",context)

	except:
		context = {"info":"修改失败！"}
		return render(request,"myadmin/info.html",context)


# 登录验证码
def showcode(request):
    #引入随机函数模块
    import random
    from PIL import Image, ImageDraw, ImageFont
    #定义变量，用于画面的背景色、宽、高
    #bgcolor = (random.randrange(20, 100), random.randrange(
    #    20, 100),100)
    bgcolor = (242,164,247)
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

    font = ImageFont.truetype('static/STXIHEI.TTF', 21)

    #font = ImageFont.load_default().font
    #构造字体颜色
    fontcolor1 = (255, random.randrange(0, 255), random.randrange(0, 255))
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
