# _*_encoding:utf8_*_
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

import datetime
import random

from product.models import Product
from .models import OrderItem, Order
from .forms import OrderForm
# Create your views here.


class ForeProductView(View):
    def get(self, request):
        # 获取商品、数量
        item_id = request.GET.get("pid", "")
        num = request.GET.get("num", "")
        item = Product.objects.get(id=int(item_id))
        user_id = request.user.id

        all_oi = OrderItem.objects.filter(user_id=user_id, order_id__isnull=True)
        found = False
        for oi in all_oi:
            if oi.product.id == item.id:
                oi.number += int(num)
                oi.save()
                found = True

        if not found:
            oi = OrderItem()
            oi.number = num
            oi.product_id = item_id
            oi.user_id = user_id
            oi.save()

        all_order_item = OrderItem.objects.filter(user_id=user_id, order_id__isnull=True)
        all_unit = 0
        for oi in all_order_item:
            unit = oi.product.promoteprice * oi.number
            all_unit += unit

        return render(request, "order_settlement.html", {
            "all_order_item": all_order_item,
            "all_unit": all_unit,
        })

    def post(self, request):
        pass


class AddCartView(View):
    def get(self, request):
        item_id = request.GET.get("pid", "")
        num = request.GET.get("num", "")
        # item = Product.objects.get(id=item_id)

        user = request.user
        found = False

        all_oi = OrderItem.objects.filter(user_id=user.id, order_id__isnull=True)
        for oi in all_oi:
            if oi.product.id == item_id:
                oi.number += int(num)
                oi.save()
                found = True
        if not found:
            oi = OrderItem()
            oi.user = user
            oi.number = num
            oi.product = Product.objects.get(id=item_id)
            oi.save()
        # 给js发送一个字符串表示成功加入购物车
        return HttpResponse("success", content_type='text')


class ForeCatView(View):
    def get(self, request):
        user = request.user
        ois = OrderItem.objects.filter(user_id=user.id, order_id__isnull=True)
        return render(request, "user_forecart.html", {
            "all_order_item": ois,

        })


# 创建订单
class CreateOrderView(View):
    def get(self, request):
        pass

    def post(self, request):
        order_form = OrderForm(request.POST)
        user_id = request.user
        if order_form.is_valid():
            address = request.POST.get("address", "")
            post = request.POST.get("post", "")
            receiver = request.POST.get("receiver", "")
            mobile = request.POST.get("mobile", "")
            userMessage = request.POST.get("userMessage", "")

            order = Order()
            order.address = address
            order.post = post
            order.receiver = receiver
            order.mobile = mobile
            order.userMessage = userMessage
            order.status = "waitPay"
            order.user_id = request.user.id

            order.orderCode = int(datetime.datetime.now().strftime('%y%m%d%H%M%S')) * 10000 + random.randint(0,
                                                                                                             9999)
            order.save()
            all_oi = OrderItem.objects.filter(order_id__isnull=True, user_id=user_id)
            all_unit = 0
            for oi in all_oi:
                oi.order = order
                oi.save()
                unit = oi.product.promoteprice * oi.number
                all_unit += unit
            return render(request, "order_payment.html", {
                "all_unit": all_unit,
                "order": order,
            })
        else:
            return HttpResponse("妈的，出问题了，赶紧查查CreateOrderView", content_type='text')


# 点击确认支付，跳转到支付成功页面
class PayedView(View):
    def get(self, request):
        oid = request.GET.get("oid", "")
        order = Order.objects.get(id=oid)
        order.status = "waitDelivery"
        order.payDate = datetime.datetime.now()
        order.save()

        sum_unit = 0
        all_order_item = order.get_order_item()
        for oi in all_order_item:
            unit = oi.product.promoteprice * oi.number
            sum_unit += int(unit)
        return render(request, "order_paymentSuccess.html", {
            "order": order,
            "sum_unit": sum_unit,
        })


# 我的订单页
class MyOrderView(View):
    def get(self, request):
        user = request.user
        os = Order.objects.filter(user_id=user.id).exclude(status="delete")
        return render(request, "order_myOrder.html", {
            "orders": os,
        })


# 评价页面
class ReviewView(View):
    def get(self, request):
        item_id = request.GET.get("pid", "")
        item = Product.objects.get(id=item_id)
        return render(request, "order_review.html", {
            "item": item,
        })

    def post(self, request):
        pass