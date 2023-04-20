from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):
    ''' Test Setup '''

    def setUp(self):
        ''' Here we setup data for unit test '''
        self.register_url = reverse('signup')
        self.login_url = reverse('signin')
        self.user_data = {
            'username': 'admin',
            'password': 'admin',
            'email': 'admin@admin.com',
            "name":"admin",
            "home_address":"cuttack",
            "phone_number":"96325874",
        }
  