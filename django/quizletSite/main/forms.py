from django import forms

class createNewFlashcard(forms.Form):
    setName = forms.CharField(label = "flashcard set name", max_length = 200)
    term = forms.CharField(label = "term", max_length  = 200)
    definition = forms.CharField(label = "defintion", max_length = 1000)