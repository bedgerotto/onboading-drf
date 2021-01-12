import factory
from faker import Faker
from .models import Category, Author, Book

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    description = Faker().text(200)

class AuthorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Author

    name = Faker().name()
    birth_date = Faker().date()

class BookFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Book
    
    title = Faker().text(25)
    description = Faker().text(200)
    release_date = Faker().date()
    isbn_number = Faker().random_int()
    category = CategoryFactory.create()
    author = AuthorFactory.create()
