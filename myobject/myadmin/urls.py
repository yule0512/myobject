from django.conf.urls import url

from . import views,viewsgoods,viewsorders

urlpatterns = [

# ===============================
	# 后台管理主页
    url(r'^$', views.index,name = "myadmin_index"),

    # ==========后台管理============
    # 登陆模板
    url(r'^login$',views.login,name = "myadmin_login"),
    # 登陆操作
    url(r'^dologin$',views.dologin,name = "myadmin_dologin"),
    #退出
    url(r'^logout$',views.logout,name = "myadmin_logout"),

    # 登录验证码
    url(r'^showcode$',views.showcode,name = "myadmin_showcode"),



# ===============会员管理================
    # 浏览分页用户
    url(r'^users/(?P<pIndex>[0-9]*)/$',views.usersindex,name = "myadmin_usersindex"),

    # 添加用户表单显示
    url(r'^usersadd$',views.useradd,name = "myadmin_useradd"),

    # 添加用户
    url(r'^usersinsert$',views.userinsert,name = "myadmin_userinsert"),

    # 删除
    url(r'^userdel/(?P<uid>[0-9]*)$',views.userdel,name = "myadmin_userdel"),

    # 编辑
    url(r'^useredit/(?P<uid>[0-9]*)$',views.useredit,name = "myadmin_useredit"),

    # 修改编辑信息
    url(r'^userupdate/(?P<uid>[0-9]*)$',views.userupdate,name = "myadmin_userupdate"),





# ===============商品类别管理================
    # 分页浏览类别
    # url(r'^types/(?P<pIndex>[0-9]*)/$',viewsgoods.typesindex,name = "myadmin_typesindex"),

    # 浏览类别
    url(r'^types$',viewsgoods.typesindex,name="myadmin_typesindex"),

    # 添加类别 表单
    url(r'^typeadd/(?P<tid>[0-9]*)/$',viewsgoods.typeadd,name = "myadmin_typeadd"),
    # 执行添加类别
    url(r'^typeinsert/$',viewsgoods.typeinsert,name = "myadmin_typeinsert"),

    #删除类别
    url(r'^typedel/(?P<tid>[0-9]*)/$',viewsgoods.typedel,name = "myadmin_typedel"),

    # 编辑类别名称
    url(r'^typeedit/(?P<tid>[0-9]*)/$',viewsgoods.typeedit,name = "myadmin_typeedit"),

    # 修改后 更新类别名称
    url(r'^typeupdate/(?P<tid>[0-9]*)/$',viewsgoods.typeupdate,name = "myadmin_typeupdate"),


# ===============商品信息管理================
    
    # 显示商品信息
    url(r'^goods/(?P<pIndex>[0-9]*)/$',viewsgoods.goodsindex,name="myadmin_goodsindex"),


    # 添加商品信息
    url(r'^goodsadd$',viewsgoods.goodsadd,name="myadmin_goodsadd"),

    # 添加商品信息 操作
    url(r'^goodsinsert$',viewsgoods.goodsinsert,name="myadmin_goodsinsert"),

    # 删除商品信息
    url(r'^goodsdel/(?P<gid>[0-9]*)/$',viewsgoods.goodsdel,name="myadmin_goodsdel"),

    # 编辑商品信息 打开表单
    url(r'^goodsedit/(?P<gid>[0-9]*)/$',viewsgoods.goodsedit,name="myadmin_goodsedit"),

    # 提交编辑
    # url(r'^goodsupdate/(?P<gid>[0-9]*)/$',viewsgoods.goodsupdate,name="myadmin_goodsupdate"),
    url(r'^goodsupdate/(?P<gid>[0-9]*)/$',viewsgoods.goodsupdate,name="myadmin_goodsupdate"),

# ===================订单管理====================
    # 查看订单
    # url(r'^orders$',viewsorders.orders,name="myadmin_orders"),

    # 分页查看所有订单
    url(r'^orderindex/(?P<pIndex>[0-9]+)/$',viewsorders.orderindex,name = "myadmin_orderindex"),

    # 查看订单详情
    url(r'^orderDetail/(?P<oid>[0-9]+)/$',viewsorders.orderDetail,name = "myadmin_orderDetail"),

    # 修改订单状态
    # url(r'^ordereditstatu/(?P<oid>[0-9]+)/$',viewsorders.ordereditstatu,name = "myadmin_ordereditstatu"),
    
    # 更新订单状态 
    url(r'^ordereditstatu$',viewsorders.ordereditstatu,name = "myadmin_ordereditstatu"),


]
