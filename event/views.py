from django.shortcuts import render
from django.views import View


def event_list(request):
    return render(request, 'event/event_list.html', {})


def front_page(request):
    return render(request, 'event/front_page.html', {})