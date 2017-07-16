# _*_encoding:utf8_*_
__author__ = 'hetao'
__date__ = '2017/4/22 16:42'

import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin
from xadmin.layout import Fieldset, Main, Side, Row

from django.utils.translation import ugettext as _

from .models import EmailVerifyRecord, UserProfile


class UserProfileAdmin(UserAdmin):
    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'username', 'password',
                             css_class='unsort no_title'
                             ),
                    Fieldset(_('Personal info'),
                             Row('first_name', 'last_name'),
                             'email'
                             ),
                    Fieldset(_('Permissions'),
                             'groups', 'user_permissions'
                             ),
                    Fieldset(_('Important dates'),
                             'last_login', 'date_joined'
                             ),
                ),
                Side(
                    Fieldset(_('Status'),
                             'is_active', 'is_staff', 'is_superuser',
                             ),
                )
            )
        return super(UserAdmin, self).get_form_layout()


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
    list_filter = ('code', 'email', 'send_type', 'send_time',)
    model_icon = 'fa fa-address-book-o'
    # readonly_fields = ['code', 'email']
    # exclude = ('send_type',)

# class UserProfileAdmin(object):
#     list_display = ('id', 'username', 'birday', 'gender', 'address', 'mobile', 'image')
#     search_fields = ('nick_name', 'birday', 'gender', 'address', 'mobile', 'image')
#     list_filter = ('nick_name', 'birday', 'gender', 'address', 'mobile', 'image')


# from django.contrib.auth.models import User
# xadmin.site.unregister(User)
xadmin.sites.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
# xadmin.site.register(UserProfile, UserProfileAdmin)

xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

