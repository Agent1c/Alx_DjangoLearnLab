from django.db import models

# Create your models here.

#Book Model

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50 )

    def __str__(self) -> str:
        return f'{self.title} {self.author}'