from django.shortcuts import render
from django.views import View


def event_list(request):
    return render(request, 'event/event_list.html', {})
