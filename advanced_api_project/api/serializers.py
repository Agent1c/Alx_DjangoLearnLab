from rest_framework import serializers
from .models import Book


# BookSerializer that serializes all fields of the Book model
class BookSerializer(serializers.ModelSerializer):
    # Define the nested serializer for related books
    queryset = = Book.objects.all()
    related_books = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    
    class Meta:
        model = Book
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name']