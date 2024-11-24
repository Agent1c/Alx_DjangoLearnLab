from django import forms
from .models import Book
from django.shortcuts import render


class BookForm(forms.ModelForm):
    
    class Meta:
         fields = ('title', 'author')

# In your view
def search_books(request):
    form = BookForm(request.GET or None)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Book.objects.filter(title__icontains=query)
        return render(request, 'search_results.html', {'results': results})
    return render(request, 'search.html', {'form': form})