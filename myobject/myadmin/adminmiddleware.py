from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse

# 正则
import re

# 自定义后台中间件类
class AdminiMiddleware(object):

	def __init__(self,get_response):
	    # One-time configuration and initialization.
        #print("AdminMiddleware")
		self.get_response = get_response


	def __call__(self,request):
		#定义网站后台不用登陆也可以访问路由url
		#			登录、登录操作、			
		urllist = ['/myadmin/login','/myadmin/dologin','/myadmin','/myadmin/showcode']
		#获取当前请求路径
		path = request.path
		#判断当前请求是否访问的是后台(带/myadmin请求都是后台请求)，并且请求路径不在urllistz中
		if re.match("/myadmin",path) and (path not in urllist):
			#判断当前用户是否没有登录，在session中检测 管理员信息是否在缓存中，如果没有，重定向到登录页面
			if "adminuser" not in request.session:
				#执行登录界面跳转
				return redirect(reverse('myadmin_login'))

		response = self.get_response(request)



        # Code to be executed for each request/response after
        # the view is called.

		return response
