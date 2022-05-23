from pyexpat import model
from attr import field, fields
from rest_framework import serializers
from books.models import Book

class BookListserializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'