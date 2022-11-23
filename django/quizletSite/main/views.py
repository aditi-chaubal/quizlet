from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import createNewFlashcard
from .models import Flashcard, Item

# Create your views here.

def index(response, id):
    fc = Flashcard.objects.get(id = id)
    return render(response, "main/flashcard.html", {"fc":fc})

def homePage(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = createNewFlashcard(response.POST)

        if form.is_valid():
            n = form.cleaned_data["setName"]
            f = Flashcard(name = n)
            f.save()
        
        return HttpResponseRedirect("/%i" %f.id)

    else:
        form = createNewFlashcard()
    return render(response, "main/create.html", {"form": form})