# _*_encoding:utf8_*_
__author__ = 'hetao'
__date__ = '2017/4/22 16:42'

import xadmin
from .models import *
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = u"仿天猫后台管理系统"
    site_footer = u"奇维科技"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ('code', 'email', 'send_type', 'send_time',)
    search_fields = ('code', 'email', 'send_type',)
    list_filter = ('code', 'email','send_type', 'send_time',)
xadmin.sites.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)


class UserProfileAdmin(object):
    list_display = ('id', 'username', 'birday', 'gender', 'address', 'mobile', 'image')
    search_fields = ('nick_name', 'birday', 'gender', 'address', 'mobile', 'image')
    list_filter = ('nick_name', 'birday', 'gender', 'address', 'mobile', 'image')
xadmin.site.register(UserProfile, UserProfileAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)