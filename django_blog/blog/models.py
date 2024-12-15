from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager



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

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        self.name

# Implement Profile Management
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.author.username}: {self.content[:20]}"
    
