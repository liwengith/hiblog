# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 10:48
# @Author  : zzw
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url,include
from django.contrib import admin
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^article/(?P<article_id>[0-9]+)$',views.article_page,name='article_page'),
    url(r'^edit/$',views.edit_page,name="edit_page"),
    url(r'^edit/action$',views.edit_action,name="edit_action"),
]