from django.db import models

class Category(models.Model):
    description = models.CharField(max_length=200, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description

class Author(models.Model):
    name = models.CharField(max_length=200, null=False)
    birth_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    description = models.TextField()
    release_date = models.DateField()
    isbn_number = models.CharField(max_length=50)
    category = models.ForeignKey(Category, null=False, on_delete=models.RESTRICT)
    author = models.ForeignKey(Author, null=False, on_delete=models.RESTRICT)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} - {self.description}"