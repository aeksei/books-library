from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from books import models
from books_api import serializers


class ListCreateAPIView(APIView):
    def get(self, request, *args, **kwargs):
        """Список книг - /books/"""
        queryset = models.Book.objects.all()

        serializer = serializers.BookSerializer(
            instance=queryset, many=True,
        )

        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.BookSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class RetriveUpdateDeleteBookAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # pk = kwargs["pk"] заменено на **kwargs в get_object_or_404
        obj = get_object_or_404(models.Book, **kwargs)

        serializer = serializers.BookSerializer(obj)

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        obj = get_object_or_404(models.Book, **kwargs)

        serializer = serializers.BookSerializer(instance=obj, data=request.data)
        if serializer.is_valid():
            serializer.save()  # Обновление
            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCreateCategoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        """Список книг - /books/"""
        queryset = models.Category.objects.all()

        serializer = serializers.CategorySerializer(
            instance=queryset, many=True,
        )

        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = serializers.CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED,
            )

        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
