from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Library, Book
from django.contrib.auth.decorators import user_passes_test

def book_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .models import UserProfile

@user_passes_test(lambda user: hasattr(user, 'userprofile') and user.userprofile.role == 'Admin')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(lambda user: hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(lambda user: hasattr(user, 'userprofile') and user.userprofile.role == 'Member')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

