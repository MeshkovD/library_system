from rest_framework import generics
from django.shortcuts import render

from books.models import Book
from books.serializers import BookSerializer


class BookAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
