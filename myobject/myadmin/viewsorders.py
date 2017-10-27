# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse,JsonResponse
from django.core.urlresolvers import reverse

# 分页模块
from django.core.paginator import Paginator
# Create your views here.

from myadmin.models import Users,Goods,Orders,Detail

import time,json


# def orders(request):
# 	orderlist = Orders.objects.all()
# 	context = {"orders":orderlist}
# 	return render(request,"myadmin/orders/index.html",context)


#分页显示所有订单
def orderindex(request,pIndex):
	list = Orders.objects.all()
	# context = {"orders":list}
	p = Paginator(list,6)
	if pIndex == "":
		pIndex = '1'
	pIndex  = int(pIndex)
	list2 = p.page(pIndex)
	plist = p.page_range

	context = {'orders':list2,'pIndex':pIndex,'plist':plist}
	return render(request,"myadmin/orders/index.html",context)

# 订单详情
def orderDetail(request,oid):
    #获取当前用户下的所有订单信息
    odb = Orders.objects.filter(id = oid)
    # deb = Detail.objects.filter(orderid__in = Orders.objects.only("id").filter(uid = request.session['user']['id']))
    deb = Detail.objects.filter(orderid__in = Orders.objects.only("id").filter(id = oid))
    gob = []
    for debone in deb:
        gob.append(debone.goodsid)
    goodslist = Goods.objects.filter(id__in=gob)
    content = {'orderlist':odb,'detaillist':deb,'goodslist':goodslist}
    return render(request,'myadmin/orders/orderDetail.html',content)


def ordereditstatu(request):
	# print('in')
	oid = int(request.GET.get("oid"))
	state = int(request.GET.get("ostatus"))
	print(state)
	orderob = Orders.objects.get(id = oid)
	orderob.status = 1
	print(orderob.status)
	# orderob.save()
	return render(request,"myadmin/orders/index.html")