from pyexpat import model
from attr import field, fields
from rest_framework import serializers
from books.models import Book

class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ("title", "subtitle", "author", "isbn")

