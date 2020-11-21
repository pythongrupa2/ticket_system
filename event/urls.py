from django.urls import path

from . import views

app_name = "event"

urlpatterns = [
    path("", views.front_page, name="front_page"),
    path("event_list", views.event_list, name="event_list"),
]
