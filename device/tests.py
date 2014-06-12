from django.test import TestCase
from django.test.client import Client

class SessionTest(TestCase):
    def test_session_get(self):
        self.client = Client()
        response = self.client.get('detail')
        self.assertEqual(response.status_code,200)
        