# _*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/5/20 15:53'
from django.conf.urls import url

from .views import BuyOneView, BuyView, AddCartView, ShoppingCatView, PayedView, MyOrderView, ConfirmPayView, ReviewView

urlpatterns = [
    # 立即购买
    url(r'^buyOne/$', BuyOneView.as_view(), name="buyOne"),
    # 结算页面
    url(r'^buy/$', BuyView.as_view(), name="buy"),
    # 加入购物车
    url(r'^addCart/$', AddCartView.as_view(), name="addCart"),
    url(r'^shoppingCat/$', ShoppingCatView.as_view(), name="shoppingCat"),

    # 支付页面，支付成功页
    url(r'^payed/$', PayedView.as_view(), name="payedSuccess"),
    # 我的订单
    url(r'^myOrder/$', MyOrderView.as_view(), name="myOrder"),
    # 确认收货
    url(r'^confirmPay/$', ConfirmPayView.as_view(), name="confirmPay"),

    # 评价页面
    url(r'^review/$', ReviewView.as_view(), name="review"),
]
