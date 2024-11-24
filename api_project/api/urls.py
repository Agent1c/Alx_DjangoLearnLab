from django.urls import path, include
from . import views
from .views import BookViewSet
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

# Router

router = DefaultRouter()
router.register(r'books_all', BookViewSet)

urlpatterns = [
    # Maps to the BookList view
    path("books/", views.BookList.as_view(), name="book_list"),

    # Include the router URLs for BookViewSet (all CRUD operations)

    path('', include(router.urls)),  # This includes all routes registered with the router
]
