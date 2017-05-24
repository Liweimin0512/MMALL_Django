#_*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/4/22 17:52'

import xadmin
from .models import Order,OrderItem


class OrderAdmin(object):
    readonly_fields = ["orderCode", "address", "post",
                       "receiver", "mobile", "userMessage",
                       "createDate", "payDate", "confirmDate",
                       "user"]


class OrderItemAdmin(object):
    pass

xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(OrderItem, OrderItemAdmin)


