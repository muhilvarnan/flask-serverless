"""
Unit test for service now
"""
import unittest
import mock
from modules import service_now
from mock_data import books


@mock.patch('modules.service_now.requests.get')
class ServiceNowTest(unittest.TestCase):
    def test_get_books(self, mock_get):
        """
        should return get books
        """
        mock_get.return_value.ok = True
        mock_get.return_value.json.return_value = books

        obj = service_now.Adapater("https://www.booknomads.com")

        self.assertEqual(obj.get_books(), [])
