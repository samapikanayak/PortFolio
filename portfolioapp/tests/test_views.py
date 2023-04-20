from rest_framework import status
from .test_setup import TestSetUp
from django.urls import reverse


class TestUser(TestSetUp):
    def authentication(self):
        self.client.post(self.register_url, self.user_data, format="json")
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.client.credentials(
            HTTP_AUTHORIZATION=f"Bearer {res.data.get('access')}")

