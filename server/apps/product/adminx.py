# _*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/4/22 17:43'

import xadmin
from .models import Product,ProductSingleImage,ProductDetailImage,PropertyValue,Property,Review,Category


class SingleImageInline(object):
    model = ProductSingleImage
    extra = 0


class DetailImageInline(object):
    model = ProductDetailImage
    extra = 0


class ProductAdmin(object):
    list_display = ('name', 'subTitle', 'promoteprice', 'stock', 'createDate', 'saleCount')
    search_fields = ('name', 'subTitle', 'promoteprice', 'stock', 'createDate', 'saleCount')
    list_filter = ('name', 'subTitle', 'promoteprice', 'stock', 'createDate', 'saleCount')
    inlines = [SingleImageInline, DetailImageInline]


class CategoryAdmin(object):
    pass


class PropertyAdmin(object):
    pass


class PropertyValueAdmin(object):
    pass


# class ProductSingleImageAdmin(object):
#     pass
#
#
# class ProductDetailImageAdmin(object):
#     pass


class ReviewAdmin(object):
    pass


xadmin.site.register(Review, ReviewAdmin)
# xadmin.site.register(ProductSingleImage, ProductSingleImageAdmin)
# xadmin.site.register(ProductDetailImage, ProductDetailImageAdmin)
xadmin.site.register(PropertyValue, PropertyAdmin)
xadmin.site.register(Property, ProductAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Product, ProductAdmin)
