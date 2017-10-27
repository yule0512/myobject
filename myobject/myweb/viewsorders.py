from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse,JsonResponse
from django.core.urlresolvers import reverse

# from myadmin.models import Types,Goods
from myweb.models import Types,Goods,Orders,Detail

import time

# 公共信息加载数据 pid=0 获取一级的商品类型,每个需要显示类别菜单的页面都调用该函数
def loadContext(request):
    context={}
    context['typelist'] = Types.objects.filter(pid=0)
    return context


# 购物车
def shopcar(request):
	context = loadContext(request)
	# 判断 缓存里面有没有商品信息，如果没有 设置一个空的shoplist用于存放商品
    # 购物车判断信息 在中间件里面操作

    # 中间件操作判断 购物车是否有信息
	# if 'shoplist' not in request.session:
	# 	request.session['shoplist'] = {}
        # context = {"info":"请先登录再查看购物车","label":"点击登录"}
        # return render(request,"myweb/info.html",context)
	return render(request,"myweb/shopCar.html",context)

def shopcaradd(request,sid):
    #获取要放入购物车中的商品信息
    goods = Goods.objects.get(id=sid)
    shop = goods.toDict();
    # 获取购买数量
    num = int(request.POST['m'])
    # 将数量放入缓存
    shop['m'] = num

    #从session获取购物车信息
    if 'shoplist' in request.session:
        shoplist = request.session['shoplist']
    else:
        shoplist = {}
    
    #判断此商品是否在购物车中
    if sid in shoplist:
        #商品数量加一
        shoplist[sid]['m']+=shop['m']
    else:
        #新商品添加
        shoplist[sid]=shop

    #将购物车信息放回到session
    request.session['shoplist'] = shoplist
    return redirect(reverse('shopCar'))

# 删除指定商品

def shopcardel(request,sid):

	# 获取购物车中所有信息
	shoplist =  request.session['shoplist']
	# 删除session 购物车中指定id的数据
	del shoplist[sid]
	# 删除后再将剩下的购物车信息放入session shoplist中
	request.session['shoplist'] = shoplist
	return redirect(reverse('shopCar'))

 

 # 清空
def shopcarclear(request):
	del request.session['shoplist']
	context = {"info":"购物车空空的，","info2":"去购物？"}
	return render(request,"myweb/info.html",context)


# +-
def shopcartchange(request):
    context = loadContext(request)
    shoplist = request.session['shoplist']
    #获取信息
    # 获取缓存中商品ID
    shopid = request.GET['sid']
    # print(shopid)
    # 获取商品数量
    num = int(request.GET['num'])
    # print(num)
    # 判断购买数量 不能小于1
    if num<1:
        num = 1
    # 设置新的商品数量
    shoplist[shopid]['m'] = num 
    # 重新放入session
    request.session['shoplist'] = shoplist
    return render(request,"myweb/shopCar.html",context)




# 打开订单的表单
# 这里没有处理 订单缓存，直接用的购物车缓存。。。
def orders(request):
    try:
        # 获取购物车中的商品信息
        shoplist = request.session['shoplist']

        # 直接计算session中商品  价格
        total = 0
        for sid in shoplist:
            # 商品数量
            num = shoplist[sid]['m']
            # 单价
            price = shoplist[sid]['price']
            result = int(num)*float(price)
            total +=result

            print(total)
        # 总金额放入session
        request.session['total'] = total
    except:
        context = {"info":"刷新购物车检查一下吧！"}
        return render(request,"myweb/info.html",context)
    return render(request,"myweb/order.html")



# 订单确认
def ordersconfirm(request):
    # 生成订单缓存
    return render(request,"myweb/buyit.html")



# 订单添加
def ordersinsert(request):
    orderob = Orders()
    orderob.uid = request.session['user']['id']
    orderob.linkman = request.POST['linkname']
    orderob.address = request.POST['address']
    orderob.phone = request.POST['phone']
    orderob.total = request.POST['total']
    # orderob.code = request.POST['code']
    # orderob.addtime = time.time()
    orderob.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    orderob.status = 0
    orderob.save()

    # 所以订单详情表 也用的购物车缓存直接添加
    # 循环获取缓存中的信息
    shopList = request.session['shoplist']
    for shop in shopList.values():
        # 订单详情表添加
        detail = Detail()
        # 详情的订单id编号 就是 订单的主id  +  当前时间戳
        # print(type(orderob.id))
        # print(type(time.time()))
        # 这样保存订单详情对吗？？？！！！
        detail.orderid = orderob.id
        # print(detail.orderid)
        detail.goodsid = shop['id']
        detail.name = shop['goods']
        detail.price = shop['price']
        detail.num = shop['m']
        detail.save()

    # 购买完后清除购物车缓存，但不喜欢这样的设置
    del request.session['shoplist']

    context = {"info":"订单提交成功！您的订单号是："+str(detail.orderid),"info2":"再逛逛吗？"}
    return render(request,"myweb/info.html",context)



# 显示订单信息

# def ordersinfo(request):
#     pass