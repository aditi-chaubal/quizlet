from django.db import models

# Create your models here.
class Flashcard(models.Model):
    name = models.CharField(max_length = 300)

    def __str__(self):
        return self.name

class Item(models.Model):
    flashcard = models.ForeignKey(Flashcard, on_delete = models.CASCADE)
    text = models.CharField(max_length = 300)

    def __str__ (self):
        return self.text