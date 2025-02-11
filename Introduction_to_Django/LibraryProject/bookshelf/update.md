from bookshelf.models import Book
try:
    book_to_update = Book.objects.get(title="1984")
    book_to_update.title = "Nineteen Eighty-Four"
    book_to_update.save()
    print(f"Book updated: {book_to_update.title}, {book_to_update.author}, {book_to_update.publication_year}")
except Book.DoesNotExist:
    print("The book with the title '1984' does not exist.")
# Expected Output: Book updated: Nineteen Eighty-Four, George Orwell, 1949

