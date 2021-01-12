from library.models import Category, Author, Book
from rest_framework import viewsets, permissions
from library.serializers import CategorySerializer, AuthorSerializer, BookSerializer
from django.views.decorators.csrf import csrf_protect

class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for categorys
    """
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint for authors
    """
    queryset = Author.objects.all().order_by('-created_at')
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

    

class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint for books
    """
    queryset = Book.objects.all().order_by('-release_date')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
