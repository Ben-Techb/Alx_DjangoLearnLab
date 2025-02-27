from bookshelf.models import Book

try:
    book = Book.objects.get(title="1984")
    book.delete()
    print(f"The book with title '1984' has been deleted.")
except Book.DoesNotExist:
    print("The book is not in the database.")

# Expected Output:
# The book with title '1984' has been deleted.

