# organizer/views.py

from django.shortcuts import render
from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404

from .models import Tag

def homepage(request):
    tag_list = Tag.objects.all()
    context = {'tag_list':tag_list}
    return render(request, 'organizer/tag_list.html', context)


def tag_detail(request, slug):
    try:
        tag = Tag.objects.get(slug__iexact=slug)
    except Tag.DoesNotExist:
        raise Http404
    tag = Tag.objects.get(slug__iexact=slug)
    context = {'tag': tag}
    return render(request, 'organizer/tag_detail.html', context)