from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homePage(response):
    return HttpResponse("<h1>home page !!<h1>")

def v1(response):
    return HttpResponse("<h1>view one !!<h1>")

def create(response):
    return HttpResponse("<h1>create a new set<h1>")