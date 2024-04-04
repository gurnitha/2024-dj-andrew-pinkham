from django.shortcuts import render

from .models import Tag

def homepage(request):
    tag_list = Tag.objects.all()
    context = {'tag_list':tag_list}
    return render(request, 'organizer/tag_list.html', context)


def tag_detail(request):
    return HttpResponse()