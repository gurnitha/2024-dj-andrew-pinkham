# organizer/urls.py

from django.urls import path

from .views import homepage, tag_detail

urlpatterns = [
    path("", homepage),
    path("tag/<slug>/",tag_detail, name='organizer_tag_detail')
]