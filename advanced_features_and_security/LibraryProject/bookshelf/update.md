from bookshelf.models import Book

try:
    book = Book.objects.get(title="1984")
    book.title = "Nineteen Eighty-Four"
    book.save()
    print(f"{book.title}, {book.author}, {book.publication_year}")
except Book.DoesNotExist:
    print("The book is not in the database.")

# Expected Output: 
# Nineteen Eighty-Four, George Orwell, 1949

