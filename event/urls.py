from django.urls import path, include
from . import views

app_name = "event"

from event.views import frontpage #Anna

urlpatterns = [
    path("",frontpage, name="frontpage"), #Anna
    path("", views.event_list, name="event_list"),
]
