from rest_framework import serializers
from library.models import Category, Author, Book

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['description', 'created_at', 'updated_at']

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ['name', 'birth_date', 'created_at', 'updated_at']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    category_id = serializers.IntegerField()
    author_id = serializers.IntegerField()
    class Meta:
        model = Book
        fields = ['title', 'description', 'isbn_number', 'release_date', 'category', 'author', 'category_id', 'author_id']
        read_only_fields = ['category', 'author']
    