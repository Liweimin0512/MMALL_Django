#_*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/4/23 13:06'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)