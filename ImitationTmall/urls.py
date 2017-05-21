# _*_encoding:utf8_*_
"""ImitationTmall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.views.generic import TemplateView
import xadmin

from django.views.static import serve #处理静态文件

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView
from product.views import IndexView
from ImitationTmall.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),

    # 注册登陆
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name="login"),

    # 退出登录
    url(r'^logout/$', LogoutView.as_view(), name="logout"),

    # 验证码相关
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name="forget_pwd"),
    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name="reset_pwd"),  # 修改密码
    url(r'^modify_pwd/$', ModifyPwdView.as_view(), name="modify_pwd"),  # 修改密码,没有参数防止报错

    # 模板页面测试
    url(r'^base/$', TemplateView.as_view(template_name="base.html"), name="base"),
    url(r'^base02/$', TemplateView.as_view(template_name="base02.html"), name="base02"),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    # 用户相关URL
    url(r'users/', include('users.urls', namespace="users")),

    # 商品相关url
    url(r'^product', include('product.urls', namespace="product")),

    # 订单相关url
    url(r'^operation', include('operation.urls', namespace="operation")),

]

# 全局 404 页面配置（django 会自动调用这个变量）
handler404 = 'users.views.page_not_found'
handler500 = 'users.views.page_error'