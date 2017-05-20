# _*_coding:utf-8_*_
__author__ = 'hetao'
__date__ = '2017/5/20 16:23'

from django import forms


class OrderForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea)
    post = forms.CharField()
    receiver = forms.CharField(required=True)
    mobile = forms.CharField(required=True)
    userMessage = forms.CharField(widget=forms.Textarea)
