from rest_framework import serializers
from .models import Book, Author
from datetime import date


# BookSerializer that serializes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    # Define the nested serializer for related books

    class Meta:
        model = Book
        fields = '__all__'
    # Custom validation to ensure the publication year is not in the future.
    def validate_publication_year(self, publication_year):
        if publication_year > date.today().year:
            raise serializers.ValidationError("Publication year can not be in the future.")
        return publication_year

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name', 'books'] 