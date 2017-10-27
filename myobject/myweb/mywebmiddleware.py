from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse

# 正则
import re

# 自定义后台中间件类
class MywebMiddleware(object):

	def __init__(self,get_response):
		self.get_response = get_response


	def __call__(self,request):
		#定义网站后台不用登陆也可以访问路由url
		# 路径是进入购物车的时候，判断用户是否登录			
		urllist = ['/shopcar']
		#获取当前请求路径
		path = request.path
		#判断当前请求是否访问的是后台(带/myadmin请求都是后台请求)，并且请求路径不在urllistz中
		if path in urllist:
			#判断当前用户是否没有登录，在session中检测 管理员信息是否在缓存中，如果没有，重定向到登录页面
			if "user" not in request.session:
				#执行登录界面跳转
				context = {"info":"请先登录再查看购物车","label":"立即登录？"}
				return render(request,"myweb/info.html",context)
			# 判断购物车 如果购物车缓存 是{}空的  那就跳转到别的购物页面
			elif "shoplist" not in request.session or request.session['shoplist'] == {}:
				context = {"info":"购物车空空如也~~","info2":"去购物"}
				return render(request,"myweb/info.html",context)

		response = self.get_response(request)

		return response
