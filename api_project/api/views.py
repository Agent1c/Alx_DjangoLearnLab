from django.shortcuts import get_list_or_404
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.
# Book View

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users

    def book_all(self, request):
        # book list
        serializer = BookSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        book = get_list_or_404(self.queryset, pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    # @action(detail=False, methods=['get'])
    # def items_not_done(self, request):
    #     user_count = Book.objects.filter(done=False).count()

    #     return Response(user_count)
