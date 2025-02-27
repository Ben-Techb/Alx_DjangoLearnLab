from django.contrib import admin
from .models import Book  # Import your Book model

# Create a custom admin class for Book
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title', 'author', 'publication_year')  # Customize the columns

    # Add filters to filter by author and publication year
    list_filter = ('author', 'publication_year')  # Add filters for author and publication year

    # Enable search functionality in the admin interface
    search_fields = ('title', 'author', 'publication_year')  # Allow search by title, author, and year

# Register the Book model with the custom admin
admin.site.register(Book, BookAdmin)

