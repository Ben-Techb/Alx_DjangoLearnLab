from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Book
from django.contrib.auth.models import User

class BookAPITestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.book = Book.objects.create(title='Django Testing', author='John Doe', publication_year=2024)
        self.book_url = f'/books/{self.book.id}/'

    def test_create_book(self):
        data = {'title': 'New Book', 'author': 'Jane Doe', 'publication_year': 2023}
        response = self.client.post('/books/create/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
    
    def test_get_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)
    
    def test_get_book_detail(self):
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Django Testing')
    
    def test_update_book(self):
        data = {'title': 'Updated Title', 'author': 'John Doe', 'publication_year': 2024}
        response = self.client.put(f'/books/update/{self.book.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')
    
    def test_delete_book(self):
        response = self.client.delete(f'/books/delete/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    
    def test_unauthorized_access(self):
        self.client.logout()
        response = self.client.post('/books/create/', {'title': 'Unauthorized Book', 'author': 'Unknown', 'publication_year': 2023})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
