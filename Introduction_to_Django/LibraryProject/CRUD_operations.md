# CRUD Operations in Django Shell

## 1. Create Operation
from bookshelf.models import Book
book_to_create = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Book created: {book_to_create.title}, {book_to_create.author}, {book_to_create.publication_year}")

## Expected Output:
Book created: 1984, George Orwell, 1949
## 2. Retrieve Operation
from bookshelf.models import Book

try:
    retrieved_book = Book.objects.get(title="1984")
    print(f"{retrieved_book.title}, {retrieved_book.author}, {retrieved_book.publication_year}")
except Book.DoesNotExist:
    print("The book with the title '1984' does not exist.")

## Expected Output:
1984, George Orwell, 1949
## Update Operation
from bookshelf.models import Book

try:
    book_to_update = Book.objects.get(title="1984")
    book_to_update.title = "Nineteen Eighty-Four"
    book_to_update.save()
    print(f"Book updated: {book_to_update.title}, {book_to_update.author}, {book_to_update.publication_year}")
except Book.DoesNotExist:
    print("The book with the title '1984' does not exist.")
## Expected Output:
Book updated: Nineteen Eighty-Four, George Orwell, 1949
##Delete Operation
from bookshelf.models import Book

try:
    book_to_delete = Book.objects.get(title="1984")
    book_to_delete.delete()
    print("The book has been deleted.")
except Book.DoesNotExist:
    print("The book with the title '1984' does not exist.")
##Expected Output:
The book has been deleted.

