from django.conf.urls import url

from . import views,viewsusers,viewsorders


urlpatterns = [


	# 首页
	url(r'^$', views.index,name = "index"),
	# 列表页
	url(r'^list$',views.phonelist,name = "phonelist"),
	# 带参数列表页
	url(r'^list/(?P<tid>[0-9]+)$',views.phonelist,name = "phonelist2"),
	# 详情页
	url(r'^detail/(?P<gid>[0-9]+)$', views.detail, name="detail"),


	# 首页轮播图跳转 主打手机的详情预览页
	url(r'^info$', views.phoneinfo, name="phoneinfo"),

# ==================================

	# 登录 表单
	url(r'^login$',views.login,name = "login"),



    # 登录验证码
    url(r'^showcode$',viewsusers.showcode,name = "showcode"),

	# 登录操作
	url(r'^dologin$',viewsusers.dologin,name = "dologin"),

    #退出
    url(r'^loginout$',viewsusers.loginout,name = "loginout"),

	# 注册表单
	url(r'^register$',views.register,name = "register"),

	# 注册操作
	url(r'^userinsert$',viewsusers.userinsert,name = "userinsert"),
	


# ==================================
# 购物车
	# 打开购物车页面
	url(r'shopcar$',viewsorders.shopcar,name = "shopCar"),

	# 添加到购物车
	url(r'shopcaradd/(?P<sid>[0-9]+)$',viewsorders.shopcaradd,name = "shopCaradd"),

	# 清空购物车
	url(r'shopcarclear$',viewsorders.shopcarclear,name = "shopcarClear"),
	
	# 删除购物车指定商品
	url(r'shopcardel/(?P<sid>[0-9]+)$',viewsorders.shopcardel,name = "shopcarDel"),
	
	# +
	url(r'shopcartchange$',viewsorders.shopcartchange,name = "shopcartchange"),

# ====================================
# 订单
	# 打开订单页面  将购物车的内容生成订单
	url(r'^ordersform$', viewsorders.orders,name='orders'), 

	# 订单确认 购买页面
    url(r'^ordersconfirm$', viewsorders.ordersconfirm,name='ordersconfirm'), 

    #执行订单添加
    url(r'^ordersinsert$', viewsorders.ordersinsert,name='ordersinsert'),

    # #订单信息提交成功后显示页面 
    # url(r'^ordersinfo$', viewsorders.ordersinfo,name='ordersinfo'), 


	# 个人中心
	url(r'^mycenter/(?P<uid>[0-9]+)$',viewsusers.mycenter,name = "mycenter"),

	# 查看订单
	url(r'^myorder/(?P<userid>[0-9]+)$',viewsusers.myorder,name = "myorder"),

	# 查看订单详情
	url(r'^myorderDetail/(?P<oid>[0-9]+)$',viewsusers.myorderDetail,name = "myorderDetail"),

]
 