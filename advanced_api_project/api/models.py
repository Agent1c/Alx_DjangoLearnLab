from django.db import models

# Create your models here.

#  Authors Model
class Author(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self) -> str:
        return self.name

# Book Model
class Book(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField("2024-05-24")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} by {self.author} {self.publication_year}"

