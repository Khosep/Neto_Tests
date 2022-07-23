import unittest
import requests

# !!! Вставить свой токен от API Яндекс Диска
yd_token = ''

URL = 'https://cloud-api.yandex.net/v1/disk/resources/'
HEADERS = {'Content-Type': 'application/json',
           'Authorization': f'OAuth {yd_token}'}
PATH_TO_DISK = 'Test_folder'

class TestYandexCreateFolder(unittest.TestCase):

    def tearDown(self):
        """Удаление созданной на ЯДиске папки"""
        params = {'path': PATH_TO_DISK}
        requests.delete(URL, headers=HEADERS, params=params)

    def test_status_code_201(self):
        """201 - Ok"""
        target = 201
        self.assertEqual(target, create_folder())

    def test_status_code_401(self):
        """401 - не авторизован"""
        target = 401
        headers = {'Content-Type': 'application/json',
                   'Authorization': f'OAuth wrong token'}
        self.assertEqual(target, create_folder(headers=headers))

    def test_status_code_404(self):
        """404 - не удалось найти запрошенный ресурс"""
        target = 404
        non_existent_url = 'https://cloud-api.yandex.net/v1/disk/non-existent_url/'
        self.assertEqual(target, create_folder(url=non_existent_url))

    def test_status_code_409(self):
        """409 - папка уже существует"""
        target = 409
        create_folder()
        self.assertEqual(target, create_folder())


def create_folder(path=PATH_TO_DISK, url=URL, headers=None):
    """ Create a new folder on Yandex disk """
    if headers is None:
        headers = HEADERS
    params = {'path': path}
    res = requests.put(url, headers=headers, params=params)
    return res.status_code


if __name__ == '__main__':
    unittest.main()
