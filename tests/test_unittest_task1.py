import unittest
from unittest.mock import patch
from parameterized import parameterized
import neto_test_source as nts



class TestFunc(unittest.TestCase):

    def test_check_document_existence(self):
        '''Тест функции, кот. проверяет, существует ли документ'''
        target = '10006'
        self.assertTrue(nts.check_document_existence(target))

    @patch('builtins.input', lambda *args: '11-2')
    def test_get_doc_owner_name(self):
        '''Тест функции, кот. получает имя владельца документа по его номеру'''
        target = 'Геннадий Покемонов'
        self.assertEqual(nts.get_doc_owner_name(), target)

    def test_get_all_doc_owners_names(self):
        '''Тест функции, кот. получает полный перечень имен владельцев документов'''
        target_set = {'Василий Гупкин', 'Аристарх Павлов', 'Геннадий Покемонов'}
        self.assertEqual(nts.get_all_doc_owners_names(), target_set)

    def test_remove_doc_from_shelf(self):
        '''Тест функции, кот. удаляет документ с полки'''
        doc_number = '5455 028765'
        self.assertNotIn(doc_number, nts.remove_doc_from_shelf(doc_number))

    def test_add_new_shelf(self):
        '''Тест функции, кот. добавляет новую полку'''
        # 1. Полка уже существует
        existing_shelf = '2'
        self.assertFalse(nts.add_new_shelf(existing_shelf)[1])
        # 2. Новая полка
        new_shelf = '10'
        self.assertIn(new_shelf, nts.add_new_shelf(new_shelf)[2])

    @parameterized.expand([
        ('11-2', '3'),
        ('10006', '30'),
        ('256-256-256', '2'),
        ('128-128-128', '40')
    ])
    def test_append_doc_to_shelf(self, doc_number, shelf_number):
        '''Тест функции, кот. добавляет документ на полку.
        В параметрах теста - сочетания существующих и несуществующих номеров документов и полок'''
        self.assertIn(doc_number, nts.append_doc_to_shelf(doc_number, shelf_number)[shelf_number])

    @patch('builtins.input', lambda *args: '10006')
    def test_get_doc_shelf(self):
        '''Тест функции, кот. получает номер полки по номеру документа'''
        target = '2'
        self.assertEqual(nts.get_doc_shelf(), target)


if __name__ == '__main__':
    unittest.main()








