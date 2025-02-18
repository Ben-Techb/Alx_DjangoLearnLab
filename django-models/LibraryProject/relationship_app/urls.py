from django.urls import path
from . import views
urlspatterns = [
        path= ('book'/ , views. boook_list, name = 'book_list'),
        ]
