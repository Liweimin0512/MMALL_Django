# _*_encoding:utf8_*_
from django.shortcuts import render
from django.views.generic.base import View

from product.models import Product
from .models import OrderItem, Order
# Create your views here.


class ForeProductView(View):
    def get(self, request, item_id):
        # 获取商品、数量
        item = Product.objects.get(id=int(item_id))
        num = request.GET.get("num", "")
        # 获取用户
        user = request.user
        all_order_item = OrderItem.objects.filter(order_id=-1)
        # 遍历所有订单项，将order_id=-1的订单项取出来，找到商品相同的，只添加数量。
        if all_order_item:
            for oi in all_order_item:
                if oi.product_id == item.id:
                    oi.number += num
                    oi.save()
        else:
            oi = OrderItem()
            oi.user_id = user.id
            oi.number = num
            oi.product_id = item.id
            oi.order_id = -1
            oi.save()
            # all_unit = float(oi.number) * Product.objects.get(id=int(oi.product_id)).promoteprice
        # all_order_item = OrderItem.objects.filter(order_id=-1)

        return render(request, "Settlement.html", {
            "all_order_item": all_order_item,
            'item': item,
            # "all_unit": all_unit,
        })
