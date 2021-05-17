from django.urls import path
from .views import MyView

name_apps = "credit"

urlpatterns = [
    path("", MyView.as_view(), name="credit"),
]
