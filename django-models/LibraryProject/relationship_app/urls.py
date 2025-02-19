from django.urls import path,include
from .views import list_books
from . import views
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from .views import register
urlspatterns = [
        path= ('book'/ , views. boook_list, name = 'book_list'),
         path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
         path('relationship', include('relationship_app.urls')),
         path('register'/, views.register, name = 'register'),
         path('login'/,LoginViews.as_views(template_name='relationship_app/login.html') name= 'login'),
         path('logout'/,LogoutViews.as_views(template_name='relationship_app/logout.html') name=' logout'),
        ]
