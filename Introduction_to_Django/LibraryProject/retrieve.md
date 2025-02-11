from bookshelf.models import Book
try:
    retrieved_book = Book.objects.get(title="1984")
    print(f"{retrieved_book.title}, {retrieved_book.author}, {retrieved_book.publication_year}")
except Book.DoesNotExist:
    print("The book with the title '1984' does not exist.")
# Expected Output: 1984, George Orwell, 1949

