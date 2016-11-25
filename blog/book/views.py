from django.shortcuts import render

from book.models import Book


def book(request):
    books = Book.objects.all()
    return render(request, 'book/book.html' , {'books':books})



# Create your views here.
