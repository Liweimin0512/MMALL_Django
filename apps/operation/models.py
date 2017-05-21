#_*_encoding:utf8_*_

from __future__ import unicode_literals

from datetime import datetime

from django.db import models

from users.models import UserProfile
from product.models import *
# Create your models here.


class Order(models.Model):
    orderCode = models.CharField(max_length=100, verbose_name=u"订单号")
    address = models.CharField(max_length=100, verbose_name=u"收货地址")
    post = models.CharField(max_length=100, verbose_name=u"邮政编码")
    receiver = models.CharField(max_length=100, verbose_name=u"收货人信息")
    mobile = models.CharField(max_length=100, verbose_name=u"手机号码")
    userMessage = models.CharField(max_length=100, verbose_name=u"用户备注信息")
    createDate = models.DateTimeField(verbose_name=u"创建日期", default=datetime.now)
    payDate = models.DateTimeField(verbose_name=u"支付日期", default=datetime.now)
    deliveryDate = models.DateTimeField(verbose_name=u"发货日期", default=datetime.now)
    confirmDate = models.DateTimeField(verbose_name=u"确认收货日期", default=datetime.now)
    status = models.CharField(choices=(("waitPay", u"等待支付"),
                                       ("waitDelivery", u"等待发货"),
                                       ("waitConfirm", u"等待收货"),
                                       ("waitReview", u"等待评价"),
                                       ("finish", u"交易完成"),
                                       ("delete", u"订单删除"),
                                       ), default="waitPay",
                              max_length=100, verbose_name=u"订单状态")
    user = models.ForeignKey(UserProfile, verbose_name=u"用户")

    class Meta:
        verbose_name = u"订单"
        verbose_name_plural = verbose_name

    def get_order_item(self):
        return self.orderitem_set.all()

    def get_order_count(self):
        return self.orderitem_set.all().count()


class OrderItem(models.Model):
    number = models.IntegerField(verbose_name=u"购买数量")
    product = models.ForeignKey(Product, verbose_name=u"产品")
    order = models.ForeignKey(Order, verbose_name="订单", null=True, blank=True) # 没有订单时为-1
    user = models.ForeignKey(UserProfile, verbose_name="用户")

    class Meta:
        verbose_name = u"订单项"
        verbose_name_plural = verbose_name

