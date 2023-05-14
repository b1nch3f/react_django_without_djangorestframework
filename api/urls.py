from django.urls import path

from .views import IndexView

urlpatterns = [
    path("data/", IndexView.as_view()),
]
