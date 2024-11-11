# query_samples

from relationship_app.models import Author, Book, Library

# Query all books by a specific author

def book_by_author(author_name):
    try:
        # retrieve Author
        author = Author.objects.get(nam=author_name)
        # retrieve book by author
        books = Book.objects.filter(author_name)
        return books
    except Author.DoesNotExist:
        return ()
