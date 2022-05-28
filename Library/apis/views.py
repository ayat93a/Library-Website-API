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


class BookAPILCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers


class BookAPILUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers

class BookAPILAll(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers
    # update , delete , retrevie in one api

class BookAPILedit(generics.RetrieveUpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializers
     # update ,retrevie in one api

