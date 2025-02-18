from django.shortcuts import render
from . models import Book
def book_list(request):
    book= Book.object.all()
    return render(request, 'book_list.html', {'books': books})

