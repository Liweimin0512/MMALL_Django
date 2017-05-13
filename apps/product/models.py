#_*_encoding:utf8_*_

from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
# Create your models here.


#商品分类
class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name=u"分类名")

    class Meta:
        verbose_name = u"商品分类"
        verbose_name_plural = verbose_name


#属性
class Property(models.Model):
    name = models.CharField(max_length=200,verbose_name=u"属性")
    Category = models.ForeignKey(Category,verbose_name=u"分类")

    class Meta:
        verbose_name = u"属性"
        verbose_name_plural = verbose_name


#产品表
class Product(models.Model):
    name = models.CharField(max_length=200,verbose_name=u"产品")
    subTitle = models.CharField(max_length=500,verbose_name=u"小标题")
    orignalPrice = models.FloatField(verbose_name=u"原始价格")
    promoteprice = models.FloatField(verbose_name=u"优惠价格")
    stock = models.FloatField(verbose_name=u"库存")
    createData = models.DateTimeField(verbose_name=u"创建时间",default=datetime.now)
    Category = models.ForeignKey(Category,verbose_name=u"分类")

    class Meta:
        verbose_name = u"产品表"
        verbose_name_plural = verbose_name


#属性值
class PropertyValue(models.Model):
    value = models.CharField(max_length=200,verbose_name=u"属性值")
    property = models.ForeignKey(Property,verbose_name=u"属性名")
    Product = models.ForeignKey(Product,verbose_name=u"所属商品")

    class Meta:
        verbose_name = u"属性值"
        verbose_name_plural = verbose_name


#产品图片，包括标题图和详情图
class ProductImage(models.Model):
    type = models.CharField(choices=(("title",u"标题"),("details",u"详情")),max_length=100,verbose_name=u"图片类型")
    Product = models.ForeignKey(Product,verbose_name=u"所属商品")

    class Meta:
        verbose_name = u"产品图片"
        verbose_name_plural = verbose_name


#产品评价
class Review(models.Model):
    content = models.TextField(verbose_name=u"评价内容")
    createDate = models.DateTimeField(verbose_name=u"创建时间")
    Product = models.ForeignKey(Product,verbose_name=u"所属商品")
    user = models.ForeignKey(UserProfile,verbose_name=u"所属用户")

    class Meta:
        verbose_name = u"产品评价"
        verbose_name_plural = verbose_name