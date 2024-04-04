from django.shortcuts import render

from .models import Tag

def homepage(request):
    tag_list = Tag.objects.all()
    context = {'tag_list':tag_list}
    return render(request, 'organizer/tag_list.html', context)


def tag_detail(request):
    # slug = ?
    tag = Tag.objects.get(slug__iexact=slug)
    context = {'tag': tag}
    return render(request, 'organizer/tag_detail.html', context)