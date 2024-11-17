from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


from django.conf import settings
from django.contrib.auth.models import AbstractUs
# Create your models here.

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
# Book Model 
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title

# Extended Book Model with Custom Permissions
# Add custom permissions in the Book model by defining a Meta class with a permissions attribute.
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "can change book"),
            ("can_delete_book", "can delete book"),
        ]

    def __str__(self):
        return self.name
    
# Library Model
class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='library')

    def __str__(self):
        return self.name
    
# Librarian Model
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarians')

    def __str__(self):
        return self.name

# Extend the User Model with a UserProfile
class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

    # Sign to automatically create UserProfile on user creation
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.userprofile.save()
    
# creating a custome user model
class CustomeUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    
    def __str__(self):
        return self.username