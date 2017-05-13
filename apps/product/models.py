# _*_encoding:utf8_*_

from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
# Create your models here.


class Category(models.Model):
    # 商品分类
    name = models.CharField(max_length=200, verbose_name=u"分类名")

    class Meta:
        verbose_name = u"商品分类"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_products(self):
        return self.product_set.all()

    def get_property(self):
        return self.property_set.all()


class Property(models.Model):
    # 属性
    name = models.CharField(max_length=200, verbose_name=u"属性")
    category = models.ForeignKey(Category, verbose_name=u"分类")

    class Meta:
        verbose_name = u"属性"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_property_value(self):
        return self.propertyvalue_set.all()


class Product(models.Model):
    # 产品表
    name = models.CharField(max_length=200, verbose_name=u"产品")
    subTitle = models.CharField(max_length=500, verbose_name=u"小标题")
    orignalPrice = models.FloatField(verbose_name=u"原始价格")
    promoteprice = models.FloatField(verbose_name=u"优惠价格")
    stock = models.FloatField(verbose_name=u"库存")
    createDate = models.DateTimeField(verbose_name=u"创建时间", default=datetime.now)
    category = models.ForeignKey(Category, verbose_name=u"分类")
    saleCount = models.IntegerField(verbose_name=u"销售数量")

    class Meta:
        verbose_name = u"产品表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_product_image(self):
        return self.productimage_set.all()

    def get_property_value(self):
        return self.propertyvalue_set.all()

    def get_review(self):
        return self.review_set.all()


class PropertyValue(models.Model):
    # 属性值
    value = models.CharField(max_length=200, verbose_name=u"属性值")
    property = models.ForeignKey(Property, verbose_name=u"属性名")
    product = models.ForeignKey(Product, verbose_name=u"所属商品")

    class Meta:
        verbose_name = u"属性值"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.value


class ProductImage(models.Model):
    # 产品图片，包括标题图和详情图
    type = models.CharField(choices=(("type_single", u"标题"), ("type_detail", u"详情")), max_length=100, verbose_name= u"图片类型")
    product = models.ForeignKey(Product, verbose_name=u"所属商品")
    image = models.ImageField(upload_to="produceImage/%Y/%m", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"产品图片"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.product.name


class Review(models.Model):
    # 产品评价
    content = models.TextField(verbose_name=u"评价内容")
    createDate = models.DateTimeField(verbose_name=u"创建时间")
    product = models.ForeignKey(Product, verbose_name=u"所属商品")
    user = models.ForeignKey(UserProfile, verbose_name=u"所属用户")

    class Meta:
        verbose_name = u"产品评价"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content

