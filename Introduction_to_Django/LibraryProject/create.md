
## 1. Create Operation

**Python Command:**

from bookshelf.models import Book
book_to_create = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(f"Book created: {book_to_create.title}, {book_to_create.author}, {book_to_create.publication_year}")
# Expected Output: Book created: 1984, George Orwell, 1949

