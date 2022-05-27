from django.shortcuts import render
from rest_framework import generics

from books.models import Book
from .serializers import Bookserializers


class BookAPIListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers

class BookAPIDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers