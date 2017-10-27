# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# 分页模块
from django.core.paginator import Paginator
# Create your views here.

from myadmin.models import Types,Goods

# 导入图片操作的模块（需要安装PIL）
from PIL import Image

import time,json,os




# ===================商品类别管理=========================

# 浏览商品类别
def typesindex(request):
	# 执行数据查询，并放置到模板中
    list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    # 遍历查询结果，为每个结果对象追加一个pname属性，目的用于缩进标题
    for ob in list:
        ob.pname ='. . . '*(ob.path.count(',')-1)
        print(list[0].__dict__)
    context = {"typeslist":list}
    return render(request,'myadmin/type/index.html',context)


# 添加商品类别表单
def typeadd(request,tid):
	# 获取父类别信息，如没有父类别 默认跟类别0
    if tid == '0':
        context = {'pid':0,'path':'0,','name':'根类别'}
    else:
        ob = Types.objects.get(id=tid)
        context = {'pid':ob.id,'path':ob.path+str(ob.id)+',','name':ob.name}
    return render(request,'myadmin/type/add.html',context)



# 执行类别添加
def typeinsert(request):
	try:

		tob = Types()
		tob.name = request.POST['typename']
		tob.pid = request.POST['pid']
		tob.path = request.POST['path']
		tob.save()
		context = {"info":"添加成功！"}
	except:
		context = {"info":"添加失败！"}

	return render(request,"myadmin/info.html",context)


# 删除类别
def typedel(request,tid):
	row = Types.objects.filter(pid = tid).count()
	# 判断pid 被删除的信息是否有数据
	if row > 0:
		context = {"info":"此类别下还有子类别，无法失败！"}
		return render(request,"myadmin/info.html",context)
	ob = Types.objects.get(id = tid)
	ob.delete()
	context={"info":"删除成功"}

	return render(request,"myadmin/info.html",context)


# 编辑类别
def typeedit(request,tid):
	try:

		ob = Types.objects.get(id = tid)
		context = {"type":ob}
		return render(request,"myadmin/type/edit.html",context)
	except:
		context = {"info":"没有找到要编辑的信息!"}
	return render(request,"myadmin/type/edit.html",context)

# 更新类别
# def typeupdate(request,tid):
# 	try:

# 		ob = Types.objects.get(id = tid)
# 		ob.name = request.POST['typename']
# 		ob.save()
# 		context = {"info":"修改成功！"}
# 	except:
# 		context = {"info":"删除失败！"}
# 	return render(request,"myadmin/info.html",context)


# 更新类别
def typeupdate(request,tid):
	try:

		ob = Types.objects.get(id = tid)
		ob.name = request.POST['typename']
		ob.save()
		context = {"info":"修改成功！"}
		# return HttpResponse('<h1>修改成功111</h1>')
	except:
		context = {"info":"修改失败！"}
	return render(request,"myadmin/info.html",context)


# ===================商品信息管理=========================
# 如果删除或则修改 了类别，或则删除了二级类别，在浏览商品信息 会报找不到数据的错误，因为类别下还有商品，需要将商品删除

# 显示商品信息
def goodsindex(request,pIndex):
	# 执行数据查询，并放置到模板中
    # list = Goods.objects.all()
    list = Goods.objects.all()
    # 遍历查询结果，为每个结果对象追加一个pname属性，目的用于缩进标题
    # 商品信息中的类别id = 类别表id
    for ob in list:
        ty = Types.objects.get(id = ob.typeid)
        # 类别想对象，存放新建的类别对象中，提前台调用显示
        ob.typename = ty.name


    #分页显示用户
    p = Paginator(list,6)
    if pIndex == "":
        pIndex = '1'
    pIndex  = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range

    return render(request,"myadmin/goods/index.html",{'goodslist':list2,'pIndex':pIndex,'plist':plist})
    # context = {"goodslist":list}
    # return render(request,'myadmin/goods/index.html',context)

# 打开 添加商品信息表单
def goodsadd(request):
	# 获取类别信息
    list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
    context = {"typelist":list}
    return render(request,"myadmin/goods/add.html",context)

# 添加商品信息操作
def goodsinsert(request):
    try:

        # 判断并执行图片上传，缩放等处理
        myfile = request.FILES.get("pic", None)
        if not myfile:
            return HttpResponse("没有上传文件信息！")
        # 获取文件名称后缀
        # filehouzui = myfile.name.split('.').pop()
        # 以时间戳命名一个新图片名称
        filename= str(time.time())+"."+myfile.name.split('.').pop()
        # 存放文件 到指定目录
        # print(filename)
        destination = open(os.path.join("./static/goodsimg/",filename),'wb+')
        for chunk in myfile.chunks():      # 分块写入文件  
            destination.write(chunk)  
        destination.close()

        # 图片缩放1 75x375
        im = Image.open("./static/goodsimg/"+filename)
        # 缩放大小
        im.thumbnail((375, 375))
        # 保存图片
        im.save("./static/goodsimg/"+filename)
        
        # 图片缩放2 220x220
        im.thumbnail((220,220))
        im.save("./static/goodsimg/m_220X220"+filename)

        # 图片缩放2 80x80
        im.thumbnail((80,80))
        im.save("./static/goodsimg/s_80X80"+filename)


        # 获取商品信息并执行添加
        ob = Goods()
        ob.goods = request.POST['goodsname']
        ob.typeid = request.POST['typeid']
        print("==============:"+request.POST['typeid'])
        ob.company = request.POST['company']
        ob.price = request.POST['price']
        ob.store = request.POST['store']
        ob.descr = request.POST['descr']
        ob.picname = filename
        ob.state = 1
        # 获取的是时间戳
        # ob.addtime = time.time()
        # 获取当前时间格式化成字符串

        # print(time.localtime())
        # print(type(time.localtime()))  #<class 'time.struct_time'>
        # print(type(time.time())) #浮点型 <class 'float'>

        ob.addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # print(addtime)
        # print(type(addtime))
        ob.save()



        context = {"info":"添加成功！"}
    except:
        context = {"info":"添加失败！"}
    return render(request,"myadmin/info.html",context)


# 打开要编辑商品 表单
def goodsedit(request,gid):
    try:
        # 获取要编辑的商品信息
        obedit = Goods.objects.get(id = gid)
        # 获取商品的类别信息
        list = Types.objects.extra(select = {'_has':'concat(path,id)'}).order_by('_has')
        
        context = {"goods":obedit,"typelist":list}
        return render(request,"myadmin/goods/edit.html",context)
    except:
        context = {"info":"没有找到要修改的商品信息"}
    return render(request,"myadmin/info.html",context)



# 提交修改信息
def goodsupdate(request,gid):
    try:
        # 
        b = False
        # 获取旧图片，前台隐藏域
        oldpicname = request.POST['oldpicname']
        # 判断如果 有新上传图片后的处理
        if None != request.FILES.get("pic"):
            myfile = request.FILES.get("pic", None)
            if not myfile:
                return HttpResponse("没有上传文件信息！")
            # 以时间戳命名一个新图片名称
            filename = str(time.time())+"."+myfile.name.split('.').pop()
            destination = open(os.path.join("./static/goodsimg/",filename),'wb+')
            for chunk in myfile.chunks():      # 分块写入文件  
                destination.write(chunk)  
            destination.close()
            # 执行图片缩放
            im = Image.open("./static/goodsimg/"+filename)
            # 缩放到375*375:
            im.thumbnail((375, 375))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goodsimg/"+filename, 'jpeg')
            # 缩放到220*220:
            im.thumbnail((220, 220))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goodsimg/m_220X220"+filename, 'jpeg')
            # 缩放到220*220:
            im.thumbnail((80, 80))
            # 把缩放后的图像用jpeg格式保存:
            im.save("./static/goodsimg/s_80X80"+filename, 'jpeg')
            b = True
            picname = filename
        else:
            # 没有上传新图片，就使用就图片名称
            picname = oldpicname
        # 修改其它信息
        ob = Goods.objects.get(id=gid)
        ob.goods = request.POST['goodsname']
        ob.typeid = request.POST['typeid']
        ob.company = request.POST['company']
        ob.price = request.POST['price']
        ob.store = request.POST['store']
        ob.descr = request.POST['descr']
        ob.picname = picname
        ob.state = request.POST['state']
        ob.save()
        context = {'info':'修改成功！'}
        # 有新图片 删除旧图
        if b:
            os.remove("./static/goodsimg/m_220X220"+oldpicname) #执行老图片删除  
            os.remove("./static/goodsimg/s_80X80"+oldpicname) #执行老图片删除  
            os.remove("./static/goodsimg/"+oldpicname) #执行老图片删除  
    except:
        context = {'info':'修改失败！'}
        # 如果没有编辑成功，删除新上传的图
        if b:
            os.remove("./static/goodsimg/m_220X220"+picname) #执行新图片删除  
            os.remove("./static/goodsimg/s_80X80"+picname) #执行新图片删除  
            os.remove("./static/goodsimg/"+picname) #执行新图片删除  
    return render(request,"myadmin/info.html",context)






# 删除商品信息
def goodsdel(request,gid):
    try:

        ob = Goods.objects.get(id = gid)
        # 删除商品对应的图片
        os.remove("./static/goodsimg/m_220X220"+ob.picname)
        os.remove("./static/goodsimg/s_80X80"+ob.picname)
        os.remove("./static/goodsimg/"+ob.picname)
        ob.delete()
        context = {"info":"删除成功"}
    except:
        context = {"info":"删除失败"}
    return render(request,"myadmin/info.html",context)
