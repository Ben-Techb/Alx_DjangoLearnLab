from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import book_list, register, LibraryDetailView
from relationship_app.admin_view import admin_view
from relationship_app.member_view import member_view
from relationship_app.librarian_view import librarian_view

urlpatterns = [
    path('book/', book_list, name='book_list'),
    path('app/', include('relationship_app.urls')),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', admin_view, name='admin_view'),
    path('librarian/', librarian_view, name='librarian_view'),
    path('member/', member_view, name='member_view'),
]

