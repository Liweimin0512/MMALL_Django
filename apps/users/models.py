#_*_ encoding:utf-8 _*_
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50,verbose_name=u"昵称",default="")
    birday = models.DateField(verbose_name=u"生日",null=True,blank=True)
    gender = models.CharField(max_length=6,choices=(("mule",u"男"),("femule",u"女"),("unknow",u"保密")),default="unknow")
    address = models.CharField(max_length=100,default=u"")
    mobile = models.CharField(max_length=11,null=True,blank=True)
    image = models.ImageField(upload_to="image/%Y/%m",default=u"image/default.png",max_length=100)

    class Meta:
        verbose_name = u"用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username



#邮箱验证码
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=8,verbose_name=u"验证码")
    email = models.EmailField(max_length=50,verbose_name=u"邮箱")
    send_type = models.CharField(choices=(("register",u"注册"),("forget",u"找回密码")),max_length=10,default="register",verbose_name=u"验证码类型")
    send_time = models.DateTimeField(default=datetime.now,verbose_name=u"发送时间")

    class Meta:
        verbose_name= u"邮件验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return '{0}({1})'.format(self.code, self.email)