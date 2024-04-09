# organizer/views.py

# from django.shortcuts import render
# from django.http.response import Http404, HttpResponse
# from django.shortcuts import get_object_or_404

# from .models import Tag

# def homepage(request):
#     tag_list = Tag.objects.all()
#     context = {'tag_list':tag_list}
#     return render(request, 'organizer/tag_list.html', context)


# def tag_detail(request, slug):
#     try:
#         tag = Tag.objects.get(slug__iexact=slug)
#     except Tag.DoesNotExist:
#         raise Http404
#     tag = Tag.objects.get(slug__iexact=slug)
#     context = {'tag': tag}
#     return render(request, 'organizer/tag_detail.html', context)

from django.shortcuts import (
    get_object_or_404, render)

from .models import Tag


def homepage(request):
    return render(
        request,
        'organizer/tag_list.html',
        {'tag_list': Tag.objects.all()})


def tag_detail(request, slug):
    tag = get_object_or_404(
        Tag, slug__iexact=slug)
    return render(
        request,
        'organizer/tag_detail.html',
        {'tag': tag})


def tag_list(request):
    tag_list = Tag.objects.all()
    data = {'tag_list':tag_list}
    return render(request, 'organizer/tag_list.html', data)