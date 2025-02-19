from django.urls import path,include
from .views import list_books
from . import views
from django.contrib import admin
urlspatterns = [
        path= ('book'/ , views. boook_list, name = 'book_list'),
         path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
         path('relationship', include('relationship_app.urls')),
         path('register'/, views.register, name = 'register'),
         path('login'/, auth.views.LoginViews.as_views() name= 'login'),
         path('logout'/,views.user_logout name=' logout'),
        ]
