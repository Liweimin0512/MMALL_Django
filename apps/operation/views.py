# _*_encoding:utf8_*_
from django.shortcuts import render
from django.views.generic.base import View

from product.models import Product
from .models import OrderItem, Order
# Create your views here.


class ForeProductView(View):
    def get(self, request):
        # 获取商品、数量
        item_id = request.GET.get("pid", "")
        num = request.GET.get("num", "")
        item = Product.objects.get(id=item_id)
        user = request.user

        oi = OrderItem()
        oi.number = num
        oi.product_id = item_id
        oi.user_id = user
        oi.order_id = -1
        oi.save()

        return render(request, "Settlement.html", {
            "item": item,
            "order_item": oi,
        })
