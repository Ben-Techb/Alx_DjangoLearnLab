from django.urls import path,include
from .views import list_books
from . import views
from django.contrib import admin
urlspatterns = [
        path= ('book'/ , views. boook_list, name = 'book_list'),
         path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
         path('relationship', include('relationship_app.urls')),
        ]
