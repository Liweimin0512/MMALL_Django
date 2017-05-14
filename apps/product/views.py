# _*_encoding:utf8_*_
from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Product, ProductSingleImage, ProductDetailImage

# Create your views here.


class ClassificationView(View):
    # 分类页面
    def get(self, request, class_id):
        # 取出对应id的分类
        class_item = Category.objects.filter(id=int(class_id))
        all_product = Product.objects.filter(category_id=int(class_id))

        return render(request, "classification.html", {
            "all_product": all_product
        })


class IndexView(View):
    # 首页
    def get(self, request):
        all_category = Category.objects.all()
        all_product = Product.objects.all()
        all_single_image = ProductSingleImage.objects.all()

        return render(request, "index.html", {
            "all_category": all_category,
            "all_product": all_product,
        })

    def post(self, request):
        pass


class ItemView(View):
    # 商品页面
    def get(self, request, item_id):
        # item_page = 'item'
        item = Product.objects.get(id=int(item_id))
        return render(request, "item.html", {
            "item": item
        })
