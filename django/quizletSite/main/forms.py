from django import forms

class createNewFlashcard(forms.Form):
    title = forms.CharField(label = "title", max_length = 200)
    term = forms.CharField(label = "term", max_length  = 200)