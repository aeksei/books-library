from django.test import TestCase

from books.models import Book


class TestBook(TestCase):
    def test_str(self):
        obj = Book(title="Название", year=2024, slug="nazvanie")

        expected_result = "Название"  # obj.title
        actual_result = str(obj)

        self.assertEqual(expected_result, actual_result)
