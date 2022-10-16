from django.shortcuts import render
from django.http import HttpResponse
from .forms import createNewFlashcard

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def homePage(response):
    return render(response, "main/home.html", {})

def create(response):
    form = createNewFlashcard()
    return render(response, "main/create.html", {"form": form})