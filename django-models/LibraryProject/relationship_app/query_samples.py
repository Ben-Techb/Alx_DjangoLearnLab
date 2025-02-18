#Query all books by a specific author.

from relationship_app.models import Author, Book

author_name = "J.K. Rowling"
try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    for book in books:
        print(book.title)
except Author.DoesNotExist:
    print(f"No author found with the name {author_name}")
#List all books in a library.
from relationship_app.models import Library

library_name = "City Library"
try:
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)
except Library.DoesNotExist:
    print(f"No library found with the name {library_name}")
#Retrieve the librarian for a library.
from relationship_app.models import Library, Librarian

library_name = "City Library"
try:
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    print(f"Librarian of {library_name}: {librarian.name}")
except Library.DoesNotExist:
    print(f"No library found with the name {library_name}")
except Librarian.DoesNotExist:
    print(f"No librarian assigned to {library_name}")
#Query all books by a specific author.

from relationship_app.models import Author, Book

author_name = "J.K. Rowling"
try:
        author = Author.objects.get(name=author_name)
            books = Book.objects.filter(author=author)
                for book in books:
                            print(book.title)
except Author.DoesNotExist:
        print(f"No author found with the name {author_name}")
        #List all books in a library.
        from relationship_app.models import Library

        library_name = "City Library"
        try:
                library = Library.objects.get(name=library_name)
                    books = library.books.all()
                        for book in books:
                                    print(book.title)
        except Library.DoesNotExist:
                print(f"No library found with the name {library_name}")
                #Retrieve the librarian for a library.
                from relationship_app.models import Library, Librarian

                library_name = "City Library"
                try:
                        library = Library.objects.get(name=library_name)
                            librarian = Librarian.objects.get(library=library)
                                print(f"Librarian of {library_name}: {librarian.name}")
                except Library.DoesNotExist:
                        print(f"No library found with the name {library_name}")
                except Librarian.DoesNotExist:
                        print(f"No librarian assigned to {library_name}")
                        #Query all books by a specific author.

                        from relationship_app.models import Author, Book

                        author_name = "J.K. Rowling"
                        try:
                                author = Author.objects.get(name=author_name)
                                    books = Book.objects.filter(author=author)
                                        for book in books:
                                                    print(book.title)
                        except Author.DoesNotExist:
                                print(f"No author found with the name {author_name}")
                                #List all books in a library.
                                from relationship_app.models import Library

                                library_name = "City Library"
                                try:
                                        library = Library.objects.get(name=library_name)
                                            books = library.books.all()
                                                for book in books:
                                                            print(book.title)
                                except Library.DoesNotExist:
                                        print(f"No library found with the name {library_name}")
                                        #Retrieve the librarian for a library.
                                        from relationship_app.models import Library, Librarian

                                        library_name = "City Library"
                                        try:
                                                library = Library.objects.get(name=library_name)
                                                    librarian = Librarian.objects.get(library=library)
                                                        print(f"Librarian of {library_name}: {librarian.name}")
                                        except Library.DoesNotExist:
                                                print(f"No library found with the name {library_name}")
                                        except Librarian.DoesNotExist:
                                                print(f"No librarian assigned to {library_name}")
                                                
