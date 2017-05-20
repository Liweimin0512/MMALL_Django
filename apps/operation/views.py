# _*_encoding:utf8_*_
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

        all_oi = OrderItem.objects.filter(order_id__isnull=True)
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

        all_order_item = OrderItem.objects.filter(order_id__isnull=True)
        all_unit = 0
        for oi in all_order_item:
            unit = oi.product.promoteprice * oi.number
            all_unit += unit

        return render(request, "Settlement.html", {
            "all_order_item": all_order_item,
            "all_unit": all_unit,
        })

    def post(self, request):
        order_form = OrderForm(request.POST)
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

            order.orderCode = int(datetime.datetime.now().strftime('%y%m%d%H%M%S'))*10000 + random.randint(0, 9999)
            order.save()
            all_oi = OrderItem.objects.filter(order_id__isnull=True)
            all_unit = 0
            for oi in all_oi:
                oi.order = order
                oi.save()
                unit = oi.product.promoteprice * oi.number
                all_unit += unit
            return render(request, "payment.html", {
                "all_unit": all_unit,
            })
        else:
            return render(request, "Settlement.html", {

            })


class CreateOrderView(View):
    def get(self, request):
        pass

    def post(self, request):
        pass


class MyOrderView(View):
    def get(self, request):
        return render(request, "myOrder.html", {

        })
