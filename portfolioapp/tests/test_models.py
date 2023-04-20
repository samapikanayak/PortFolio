from django.test import TestCase
from ..models import User
from django.utils import timezone

class UserModelTest(TestCase):
    def create_user(self):
        '''user creation'''
        return User.objects.create(
            username="samapika@assurekit.com",
            email="samapika@assurekit.com",
            password="1234",
            name="samapka",
            home_address="bhubaneswar",
            phone_number="8754128",
            created_at=timezone.now()
        )
    def test_create_user(self):
        '''user creation testing'''
        w = self.create_user()
        self.assertTrue(isinstance(w, User))