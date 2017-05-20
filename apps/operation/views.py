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
        user_id = request.user.id

        all_oi = OrderItem.objects.filter(order_id__isnull=True)
        found = False
        for oi in all_oi:
            if oi.product.id == item.id:
                oi.number = int(num) + oi.number
                oi.save()
                found = True

        if (not found):
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
