from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path("api/books", views.BookList.as_view(), name="book_list_create"),
]