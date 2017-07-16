# _*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/5/20 16:23'
import re

from django import forms

from product.models import Review
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["address", "post", "receiver", "mobile", "userMessage"]

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        p = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}')
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError(u' 手机号码非法', code='mobile_inval')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["content", "product", "user"]

