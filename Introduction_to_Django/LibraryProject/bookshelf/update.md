from bookshelf.models import Book

try:
    book_to_update = Book.objects.get(title="1984")
    book_to_update.title = "Nineteen Eighty-Four"
    book_to_update.save()
    print(f"{book_to_update.title}, {book_to_update.author}, {book_to_update.publication_year}")
except Book.DoesNotExist:
    print("The book is not in the database.")

# Expected Output: 
# Nineteen Eighty-Four, George Orwell, 1949

