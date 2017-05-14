# _*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/5/13 14:17'

from django.conf.urls import url

from .views import ClassificationView, ItemView

urlpatterns = [
    # 分类详情界面
    url(r'^classification/(?P<class_id>\d+)/$', ClassificationView.as_view(), name='classification'),
    url(r'^item/(?P<item_id>\d+)/$', ItemView.as_view(), name='item')

]
