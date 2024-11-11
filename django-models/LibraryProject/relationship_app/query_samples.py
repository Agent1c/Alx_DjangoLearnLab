# query_samples

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author

def book_by_author(author_name):
    try:
        # retrieve Author
        author = Author.objects.get(nam=author_name)
        # retrieve book by author
        books = Book.objects.filter(author_name)
        return books
    except Author.DoesNotExist:
        return []  #return an empty list if the auhpr doesn't exist

"Library.objects.get(name=library_name)", "books.all()"

def book_in_library(library_id):
    try:
        #retrieve the library books
        library = Library.objects.get(id=library_id)

        books = Library.books.all()
        #listing all books
        return books
    except Library.DoesNotExist:
        return [] #return an empty list if the library doesn't exist
    
def librarian_for_library(library_id):
    try:
        # Retrieve the Library object
        library = Librarian.objects.get(library=library_id)
        return library
    except Librarian.DoesNotExist:
        return None # return None if the library doesn't exist