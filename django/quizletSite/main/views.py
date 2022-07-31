from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def homePage(response):
    return render(response, "main/home.html", {})

def create(response):
    return HttpResponse("<h1>create a new set<h1>")