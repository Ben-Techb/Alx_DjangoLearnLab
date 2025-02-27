from django.shortcuts import render
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

def raise_exception(request):
    raise ValueError("Something went wrong!")
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm

@permission_required('books.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('books.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            description = form.cleaned_data['description']
            Book.objects.create(title=title, author=author, description=description)
            return redirect('book_list')
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/create_book.html', {'form': form})

