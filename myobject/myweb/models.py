# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

#=======用户表===========================

#用户信息模型
class Users(models.Model):
    username = models.CharField(max_length=32)
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
    sex = models.IntegerField(default=1)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    state = models.IntegerField(default=1)
    # addtime = models.IntegerField()
    addtime = models.CharField(max_length=32)
    class Meta:
        db_table = "myweb_users"
    def userDict(self):
        return {'id':self.id,'username':self.username,'name':self.name,'address':self.address,'email':self.email,'phone':self.phone,'code':self.code}



#=====商品类别表===============================

class Types(models.Model):
    name = models.CharField(max_length=32)
    pid = models.IntegerField(default=0)
    path = models.CharField(max_length=255)
    class Meta:
        db_table = "myweb_types"


#======商品管理================================


#商品信息模型
class Goods(models.Model):
    typeid = models.IntegerField()
    goods = models.CharField(max_length=32)
    company = models.CharField(max_length=50)
    descr = models.TextField()
    price = models.FloatField()
    picname = models.CharField(max_length=255)
    state = models.IntegerField(default=1)
    store = models.IntegerField(default=0)
    num = models.IntegerField(default=0)
    clicknum = models.IntegerField(default=0)
    # addtime = models.IntegerField()
    addtime = models.CharField(max_length=32)
    def toDict(self):
        return {'id':self.id,'goods':self.goods,'picname':self.picname,'price':self.price,'store':self.store,'m':1}



# 订单模型
class Orders(models.Model):
    uid = models.IntegerField()
    linkman = models.CharField(max_length=32)
    address = models.CharField(max_length=255)
    code = models.CharField(max_length=6)
    phone = models.CharField(max_length=16)
    # addtime = models.IntegerField()
    addtime = models.CharField(max_length=32)
    total = models.FloatField()
    status = models.IntegerField()
    class Meta:
        db_table = "myweb_orders"




# 订单记录
class Detail(models.Model):
    orderid = models.IntegerField()
    goodsid = models.IntegerField()
    name = models.CharField(max_length=32)
    price = models.FloatField()
    num = models.IntegerField()
    class Meta:
        db_table = "myweb_detail"