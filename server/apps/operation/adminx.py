#_*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/4/22 17:52'

import xadmin
from .models import Order,OrderItem

class OrderItemInline(object):
    model = OrderItem
    extra = 0


class OrderAdmin(object):
    readonly_fields = ["orderCode", "address", "post",
                       "receiver", "mobile", "userMessage",
                       "createDate", "payDate", "confirmDate",
                       "user"]
    inlines = [OrderItemInline]


class OrderItemAdmin(object):
    pass



xadmin.site.register(Order, OrderAdmin)
xadmin.site.register(OrderItem, OrderItemAdmin)


