from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    
    class Meta:
         fields = ('title', 'author')
