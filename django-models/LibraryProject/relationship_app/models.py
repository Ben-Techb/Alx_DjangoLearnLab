from django.db import models
class Author(models.Model):
    name= models.CharField(max_length = 200)
    def __str__(self):
        return self.name
class Book(models.Model):
    title= models.CharField(max_length = 200)
    authors= models.ForeignKey(Author, on_delete= models.CASCADE, related_name= 'Book')
    def __str__(self):
        return self.name
class Library (models.Model):
    name= models.CharField(max_length= 200)
    books = models.ManyToManyField(Book, related_name= 'libraries')
    def __str__(self):
        return self.name
class Librarian (models.Model):
    name= models.CharField(max_length= 200)
    library = models.OneToOneField(Library, on_delete= models.CASCADE, related_name='librarian')
    def __str__(self):
        return self.name

