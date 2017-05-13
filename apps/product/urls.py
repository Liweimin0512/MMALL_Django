# _*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/5/13 14:17'

from django.conf.urls import url

from .views import ClassificationView, ItemView

urlpatterns = [
    url(r'^ClassificationView/', ClassificationView.as_view, name='classification'),
    url(r'item/$', ItemView.as_view(), name='item')

]
