# suorganizer/urls.py
from django.contrib import admin
from django.urls import path
# from django.conf.urls import include, url
from django.urls import re_path as url
from organizer.views import homepage, tag_detail

urlpatterns = [
    path("admin/", admin.site.urls),

    # url(r'^$', homepage), # Django 1.x
    path("", homepage), # Since Django 2
    # url(r'^tag/(?P<slug>[\w\-]+)/$',tag_detail,), # Django 1.x
    path("tag/<slug:str>/",tag_detail,), # Since Django 2
]