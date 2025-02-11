from django.db import models
class book(modules.module):
    title= modules.charfield(max_length= 200)
    author= modules.charfield(max_length= 100)
    publication_year = modules.interfield()
    def __str__(self):
        return self.title
