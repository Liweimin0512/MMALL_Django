# _*_encoding:utf8_*_
from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Product

# Create your views here.


class ClassificationView(View):
    def get(self, request):
        return render(request, "classification.html")


class IndexView(View):
    # 首页
    def get(self, request):
        all_category = Category.objects.all()
        all_product = Product.objects.all()
        return render(request, "index.html", {
            "all_category": all_category,
            "all_product": all_product
        })
    def post(self,request):
        pass