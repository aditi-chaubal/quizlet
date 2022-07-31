from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("home/", views.homePage, name = "home page"),
    ##path("create/", views.create, name = "create flashcard")
]