# organizer/urls.py

from django.urls import path

from .views import homepage, tag_detail, tag_list

urlpatterns = [
    path("", homepage),
    path('tag/', tag_list, name='organizer_tag_list'),
    path("tag/<slug>/",tag_detail, name='organizer_tag_detail'),
]