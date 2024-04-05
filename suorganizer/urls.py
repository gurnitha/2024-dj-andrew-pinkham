# suorganizer/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin
    path("admin/", admin.site.urls),
    # organizer
    path("", include('organizer.urls')), # Since Django 2
]