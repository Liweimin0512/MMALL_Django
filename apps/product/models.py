# _*_encoding:utf8_*_

from __future__ import unicode_literals

# from datetime import datetime

from django.db import models
from django.utils import timezone

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

    def get_product_by_row(self):
        products = self.product_set.all()
        product_num_each_row = 8
        products_by_row = []
        for i in range(0, len(products), product_num_each_row):
            size = i + product_num_each_row
            if size > products.count():
                size = products.count()
            else:
                size = size
            for j in range(i, size):
                products_each_row = products[j]
                products_by_row.append(products_each_row)
        return products_by_row


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
    createDate = models.DateTimeField(verbose_name=u"创建时间", default=timezone.now)
    category = models.ForeignKey(Category, verbose_name=u"分类")
    saleCount = models.IntegerField(verbose_name=u"销售数量")


    class Meta:
        verbose_name = u"产品表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

    def get_title_image(self):
        if self.productsingleimage_set.all()[0]:
            return self.productsingleimage_set.all()[0]

    def get_single_image(self):
        return self.productsingleimage_set.all()

    def get_detail_image(self):
        return self.productdetailimage_set.all()

    def get_property_value(self):
        return self.propertyvalue_set.all()

    def get_review(self):
        return self.review_set.all()

    def get_subtitle(self):
        return self.subTitle.split(" ")[0]


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


class ProductSingleImage(models.Model):
    # 产品图片标题图
    product = models.ForeignKey(Product, verbose_name=u"所属商品")
    image = models.ImageField(upload_to="produceImage/Single", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"产品标题图片"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)


class ProductDetailImage(models.Model):
    # 产品图片详情图
    product = models.ForeignKey(Product, verbose_name=u"所属商品")
    image = models.ImageField(upload_to="produceImage/Detail", default=u"image/default.png", max_length=100)

    class Meta:
        verbose_name = u"产品详情图片"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return str(self.id)


class Review(models.Model):
    # 产品评价
    content = models.TextField(verbose_name=u"评价内容")
    createDate = models.DateTimeField(verbose_name=u"创建时间", default=timezone.now())
    product = models.ForeignKey(Product, verbose_name=u"所属商品")
    user = models.ForeignKey(UserProfile, verbose_name=u"所属用户")

    class Meta:
        verbose_name = u"产品评价"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.content

