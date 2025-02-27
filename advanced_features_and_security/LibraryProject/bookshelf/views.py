from django.shortcuts import render
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def raise_exception(request):
    raise ValueError("Something went wrong!")

