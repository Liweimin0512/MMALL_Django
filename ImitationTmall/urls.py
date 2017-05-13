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
from django.conf.urls import url,include
from django.views.generic import TemplateView
import xadmin

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView
from product.views import ClassificationView, IndexView

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),

    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^captcha/', include('captcha.urls')),

    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^reset/(?P<reset_code>.*)/$', ResetView.as_view(), name="reset_pwd"),
    url(r'^modify_pwd/$', ModifyPwdView.as_view, name="modify_pwd"),

    url(r'^forget/$', ForgetPwdView.as_view, name="forget_pwd"),

    url(r'^classification/$', TemplateView.as_view(template_name="classification.html"), name="classification"),

    url(r'^base/$', TemplateView.as_view(template_name="base.html"), name="base"),

    # 商品相关url
    url(r'^product', include('product.urls'), name="product"),

]
