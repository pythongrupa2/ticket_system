from django.urls import path, include
from . import views

app_name = "web"

urlpatterns = [
    path("", views.base, name="front_page"),
    path("event_list", views.index, name="index_item"),
]
