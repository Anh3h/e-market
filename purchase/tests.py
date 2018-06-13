from django.test import TestCase
from django.urls import reverse


class BaseTest(TestCase):
    def test_login(self):
        url = reverse("login")
        reponse = self.client.get(url)
        self.assertEquals(reponse.status_code, 200)