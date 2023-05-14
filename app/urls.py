from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("link1/", views.link1, name="link1"),
    path("link2/", views.link2, name="link2"),
]
