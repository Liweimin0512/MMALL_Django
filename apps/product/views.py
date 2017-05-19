# _*_encoding:utf8_*_
from django.shortcuts import render
from django.views.generic.base import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Category, Product

# Create your views here.


class CategoryView(View):
    # 分类页面
    def get(self, request, class_id):
        # 取出对应id分类下的所有商品
        all_product = Product.objects.filter(category_id=int(class_id))
        # 获取参数sort
        sort = request.GET.get('sort', '')

        # 排序方法
        if sort:
            if sort =='review':
                all_product = all_product.order_by("review")  # 如何获取评论数量？
            elif sort =='date':
                all_product = all_product.order_by("createDate")
            elif sort =='sale_count':
                all_product = all_product.order_by("saleCount")
            elif sort =='price':
                all_product = all_product.order_by("promoteprice")
            elif sort =='alls':
                all_product = all_product.order_by("id")

        return render(request, "category.html", {
            "all_product": all_product,
            "sort": sort,
        })


class IndexView(View):
    # 首页
    def get(self, request):
        all_category = Category.objects.all()
        all_product = Product.objects.all()

        return render(request, "index.html", {
            "all_category": all_category,
            "all_product": all_product,
        })

    def post(self, request):
        pass


class ItemView(View):
    # 商品页面
    def get(self, request, item_id):
        item = Product.objects.get(id=int(item_id))
        all_review = item.get_review()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        objects = ['john', 'edward', 'josh', 'frank']

        # 对评论进行分页
        p = Paginator(all_review, 5, request=request)

        reviews = p.page(page)

        return render(request, "item.html", {
            "item": item,
            "all_review": reviews,
        })
