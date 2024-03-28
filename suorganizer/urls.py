# suorganizer/urls.py
from django.contrib import admin
from django.urls import path

from helloworld.views import greeting

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", greeting),
]