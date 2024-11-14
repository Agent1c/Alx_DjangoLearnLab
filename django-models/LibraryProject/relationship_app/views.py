from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book
from  relationship_app import query_samples

# Create your views here.
def book_list(book_by_author):
    """A class-based view for displaying details of a specific book.""" 
    model = Book
    template_name = "book_list.html"

    def get_context_data(self, **kwargs):
        """Injects additional context data specific to the book."""
        context = super().get_context_data(**kwargs)

        book = Book.objects.get()# Retrieve the current book instance
        context["book_by_author"] = book.book_by_author()
        return context
    
def index(request):
    return HttpResponse("Test, Test")

def about(request):
    return HttpResponse("Test, in About Section Test")
# class HelloView(Tempd view rendering a template named 'hello.html'."""
#     template_name = 'hello.html'lateView):
#     """A class-base