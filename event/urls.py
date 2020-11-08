from django.urls import path, include
from . import views

app_name = "event"

from event.views import front_page

urlpatterns = [
    path("", views.front_page, name="front_page"), #Anna
    path("event", views.event_list, name="event_list"),
]
