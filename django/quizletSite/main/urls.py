from django.urls import path
from . import views

urlpatterns = [
    path("", views.homePage, name = "home page"),
    path("v1/", views.v1, name = "view one"),
    path("create/", views.create, name = "create flashcard")
]