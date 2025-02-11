from django.db import models
class book(models.Model):
    title= models.charfield(max_length= 200)
    author= models.charfield(max_length= 100)
    publication_year = modules.interfield()
    def __str__(self):
        return self.title
