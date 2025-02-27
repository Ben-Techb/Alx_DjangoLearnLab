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
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "date_of_birth", "profile_photo", "password1", "password2", "is_staff", "is_active"),
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)

