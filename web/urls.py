from django.urls import path, include

from event.views import AddView

app_name = "web"

urlpatterns = [
    path("", include("web.urls")),
]
