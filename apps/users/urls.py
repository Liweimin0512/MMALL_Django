#_*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/5/14 16:44'

from django.conf.urls import url
from .views import LogoutView

urlpatterns = [
    # 退出登录
    url(r'^signout/$', LogoutView.as_view(), name="logout"),
]