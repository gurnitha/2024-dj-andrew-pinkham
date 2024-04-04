# suorganizer/urls.py
from django.contrib import admin
from django.urls import path

from organizer.views import homepage

urlpatterns = [
    path("admin/", admin.site.urls),

    # url(r'^$', homepage), # Django 1.x
    path("", homepage), # Since Django 2
]