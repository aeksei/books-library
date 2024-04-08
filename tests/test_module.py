import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # Arrange: подготавливаем данные для теста
        expected = True  # ожидаемое значение

        # Act: выполняем действие, которое тестируем
        actual = True  # фактическое значение

        # Assert: проверяем результат
        self.assertEqual(actual, expected)  # Проверка равенства фактического и ожидаемого значения


class TestDictionaryMethods(unittest.TestCase):
    def test_add_new_key(self):
        my_dict = {'a': 1, 'b': 2}
        
        # Добавляем новый ключ в словарь
        my_dict['c'] = 3
        # Сравниваем измененный словарь с ожидаемым результатом
        self.assertEqual(my_dict, {'a': 1, 'b': 2, 'c': 3})

    def test_contains_key_in_dict(self):
        my_dict = {'a': 1, 'b': 2}

        # Проверяем, что ключ 'a' существует в словаре
        self.assertTrue('a' in my_dict)

    def test_get_default_value(self):
        my_dict = {'a': 1, 'b': 2}

        # Проверяем, что метод get возвращает None для несуществующего ключа
        does_not_exists_key = 'c'
        result = my_dict.get(does_not_exists_key)
        self.assertIsNone(result)

    def test_key_error(self):
        my_dict = {'a': 1, 'b': 2}

        # Проверяем, что обращение к несуществующему ключу вызывает KeyError
        with self.assertRaises(KeyError):
            does_not_exists_key = 'c'
            _ = my_dict[does_not_exists_key]

    def test_contains_value(self):
        my_dict = {'a': 1, 'b': 2}

        # Проверяем вхождение значения в словарь
        self.assertIn(2, my_dict.values())