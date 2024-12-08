from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.


# User Model
class User(models.Model):
    name = models.CharField(max_length=40)
    # email = models.EmailField(max_length=100)
    # password = models.CharField(max_length=100)
    def __str__(self) -> str:
        return f'{self.name}'

# Post Model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

    def __str__(self) -> str:
        return f'{self.title} {self.content} {self.published_date}'
    
class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date', 'author']
    
    