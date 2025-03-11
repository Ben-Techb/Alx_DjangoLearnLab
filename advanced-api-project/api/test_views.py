from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        self.book = Book.objects.create(title="Test Book", author="Test Author", publication_year=2023)
        
        self.client.login(username='testuser', password='testpass')
        
    def test_list_books(self):
        response = self.client.get("/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_retrieve_book(self):
        response = self.client.get(f"/books/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_create_book(self):
        data = {"title": "New Book", "author": "New Author", "publication_year": 2024}
        response = self.client.post("/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
    def test_update_book(self):
        data = {"title": "Updated Book", "author": "Updated Author", "publication_year": 2025}
        response = self.client.put(f"/books/update/{self.book.id}/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_delete_book(self):
        response = self.client.delete(f"/books/delete/{self.book.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

