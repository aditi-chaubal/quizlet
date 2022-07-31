from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.index, name = "index"),
    path("", views.homePage, name = "home page"),
    path("create/", views.create, name = "create flashcard")
]