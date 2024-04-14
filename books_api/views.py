from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from books import models
from books_api import serializers
from rest_framework import generics
from django_filters import rest_framework as filters


class ListCreateBookAPIView(generics.ListCreateAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('year', 'book_type')


class RetriveUpdateDeleteBookAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer


class ListCreateCategoryAPIView(generics.ListCreateAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer
