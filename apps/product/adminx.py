#_*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/4/22 17:43'

import xadmin
from .models import Product,ProductImage,PropertyValue,Property,Review,Category

class ProductAdmin(object):
    pass

class CategoryAdmin(object):
    pass

class PropertyAdmin(object):
    pass

class PropertyValueAdmin(object):
    pass

class ProductImageAdmin(object):
    pass

class ReviewAdmin(object):
    pass


xadmin.site.register(Review,ReviewAdmin)
xadmin.site.register(ProductImage,ProductImageAdmin)
xadmin.site.register(PropertyValue,PropertyAdmin)
xadmin.site.register(Property,ProductAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Product,ProductAdmin)
