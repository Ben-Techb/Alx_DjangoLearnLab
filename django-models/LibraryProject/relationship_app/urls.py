from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, register, LibraryDetailView

urlpatterns = [
    path('book/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),  
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
]

