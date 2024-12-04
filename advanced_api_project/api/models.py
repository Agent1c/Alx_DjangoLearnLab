from django.db import models

# Create your models here.

#  Authors Model
class Author(models.Model):
    name = models.CharField(_("name"), max_length=50)
    
    def __str__(self) -> str:
        return self.name

# Book Model
class Book(models.Model):
    name = models.CharField(_("name"), max_length=50)
    title = models.CharField(max_length=50)
    publication_year = models.IntegerField("2024-05-24")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# class Book(models.Model):
#     title = models.CharField(max_length=200)
#     related_books = models.ManyToManyField('self', blank=True)

#     def __str__(self):
#         return self.title