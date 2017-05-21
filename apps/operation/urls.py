# _*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/5/20 15:53'
from django.conf.urls import url

from .views import ForeProductView, CreateOrderView, MyOrderView, AddCartView, ForeCatView, PayedView, ReviewView

urlpatterns = [
    # 结算页面
    url(r'^settlement/$', ForeProductView.as_view(), name="settlement"),
    # 确认支付
    url(r'^createOrder/$', CreateOrderView.as_view(), name="createOrder"),
    # 我的订单
    url(r'^forebought/$', MyOrderView.as_view(), name="myOrder"),

    # 加入购物车
    url(r'^foreaddCart/$', AddCartView.as_view(), name="addCart"),
    # 查看购物车
    url(r'^forecat/$', ForeCatView.as_view(), name="foreCat"),
    # 支付成功页
    url(r'^forepayed/$', PayedView.as_view(), name="payedSuccess"),

    # 评价页面
    url(r'^reveiw/$', ReviewView.as_view(), name="review"),
]
