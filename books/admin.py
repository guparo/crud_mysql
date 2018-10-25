from django.contrib import admin
from books.models import Book
from books.models import Passenger
from .models import Contact

admin.site.register(Book)
admin.site.register(Passenger)
admin.site.register(Contact)