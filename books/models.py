from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
import time



class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pages = models.IntegerField(default=49,
        validators=[
            MaxValueValidator(400),
            MinValueValidator(49)
        ])
    image  = models.FileField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})

class Passenger(models.Model):
    name = models.CharField(max_length=150)
    survived = models.BooleanField()
    ticket_class = models.PositiveSmallIntegerField(default=1,
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1)
        ])

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    creation_date = time.asctime( time.localtime(time.time()) )


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
