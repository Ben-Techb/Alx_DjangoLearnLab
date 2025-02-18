from django.shortcuts import render
from . models import Book
def book_list(request):
    book= Book.object.all()
    return render(request, 'book_list.html', {'books': books})
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Library, Book

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'

