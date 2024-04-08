from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

from books.models import Book


class TestListCreateBookAPIView(APITestCase):
    def test_books_list(self):
        Book.objects.create(title="Тестовое название", year=2024, slug="title-test")

        url = reverse("books_api:book-list")
        resp = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        expected_count = 1
        self.assertEqual(expected_count, len(resp.json()))

    def test_books_empty_list(self):
        url = reverse("books_api:book-list")
        resp = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, resp.status_code)

        empty_list = []

        resp_data = resp.json()
        self.assertEqual(empty_list, resp_data)

    def test_create_new_book(self):
        url = reverse("books_api:book-list")  # /api/v1/books/
        data = dict(title="Тестовое название", year=2024, slug="title-test")
        resp = self.client.post(url, data)

        self.assertEqual(status.HTTP_201_CREATED, resp.status_code)

        expected_count = 1
        self.assertEqual(expected_count, Book.objects.count())

    def test_create_book_with_duplicated_slug(self):
        book_data = dict(title="Тестовое название", year=2024, slug="title-test")
        Book.objects.create(**book_data)  # Book.objects.create(title="Тестовое название", year=2024, slug="title-test")

        url = reverse("books_api:book-list")  # /api/v1/books/
        resp = self.client.post(url, book_data)

        self.assertEqual(status.HTTP_400_BAD_REQUEST, resp.status_code)


class TestRetrieveUpdateAPIView(APITestCase):
    def test_get_book(self):
        book_data = dict(title="Тестовое название", year=2024, slug="title-test")
        book_pk = Book.objects.create(**book_data).pk

        url = reverse("books_api:book-detail", args=(book_pk,))  # /api/v1/books/1/
        # url = reverse("books_api:book-detail", kwargs={"pk": 1})  # /api/v1/books/1/
        resp = self.client.get(url)

        self.assertEqual(status.HTTP_200_OK, resp.status_code)

    def test_get__get_does_not_exists_book(self):
        does_not_exists_book_pk = 1
        url = reverse("books_api:book-detail", args=(does_not_exists_book_pk,))  # /api/v1/books/1/
        resp = self.client.get(url)

        self.assertEqual(status.HTTP_404_NOT_FOUND, resp.status_code)
