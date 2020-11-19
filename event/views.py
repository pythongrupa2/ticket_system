from django.shortcuts import render


def event_list(request):
    return render(request, 'event/event_list.html', {})


def front_page(request):
    return render(request, 'front_page.html', {})
