from django.db import models
from django.urls import reverse

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.IntegerField()
    image  = models.FileField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})

class Passenger(models.Model):
    name = models.CharField(max_length=150)

    sex = models.CharField(max_length=15)
    survived = models.BooleanField()
    age = models.FloatField()
    ticket_class = models.PositiveSmallIntegerField()
    embarked = models.CharField(max_length=150)
