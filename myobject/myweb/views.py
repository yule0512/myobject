from django.shortcuts import render

from myadmin.models import Types,Goods


# 公共信息加载数据 pid=0 获取一级的商品类型,每个需要显示类别菜单的页面都调用该函数
def loadContext(request):
    context={}
    context['typelist'] = Types.objects.filter(pid=0)
    return context

# 首页
def index(request):
	context = loadContext(request)

	# 首页加载数码 手机 商品  查询前四个商品
	context['goodsphone'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(1)+',')).all()[0:4]

	# 首页加载配件 商品  查询前四个商品
	context['goodspeijian'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(3)+',')).all()[0:4]
 
 	# 首页加载配件 商品  查询后四个商品
	context['goodspeijian2'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(3)+',')).all()[4:9]

	# 首页加载配件 礼品  查询前四个商品
	context['goodslipin'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(4)+',')).all()[0:4]

	return render(request,"myweb/index.html",context)

# 列表页   tid=0默认获取全部商品
def phonelist(request,tid = 0):
	context = loadContext(request)
	# 如果商品是顶级类型
	if tid == 0:
		# 获取所有商品信息
		context['goodslist'] = Goods.objects.all()
	else:
		# 获取子类别商品
		context['types'] = Types.objects.filter(pid = tid)
		# context['goodslist'] = Goods.objects.filter(typeid = tid)
		context['goodslist'] = Goods.objects.filter(typeid__in=Types.objects.only('id').filter(path__contains=','+str(tid)+','))
		
	return render(request,"myweb/phonelist.html",context)

# 详情页
def detail(request,gid):
	context = loadContext(request)

	print(gid)
	goodsinfo = Goods.objects.get(id = gid)

	# 点击量+1
	goodsinfo.clicknum +=1
	goodsinfo.save()

	# 存放该商品信息 命名goods
	context['goods'] = goodsinfo
	return render(request,"myweb/detail.html",context)


# 首页轮播图跳转 主打手机的详情预览页
def phoneinfo(request):
	context = loadContext(request)
	return render(request,"myweb/phoneInfo.html",context)

# 登录  登录是独立页面，不做base继承
def login(request):
	return render(request,"myweb/login.html")

# 注册 独立页面，不做base继承
def register(request):
	return render(request,"myweb/register.html")