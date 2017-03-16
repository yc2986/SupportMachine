from django.test import TestCase
from RegiHandler.serializers import DolbyUserSerializer
# rest framework
from rest_framework.test import APIClient

client = APIClient()

# Create your tests here.
class DolbyUserSerializerTest(TestCase):
    def test_create_user_full_data(self):
        data = {
            # basic info
            'username': 'yc2986',
            'password': '123456',
            'email': 'chengyuzhou1992@gmail.com',
            # profile info
            'company': 'dolby laboratories',
            'registration_code': '123456',
            'phone_number': '1234567890',
        }
        response = client.post('/register/', data, format = 'json')
        # check successful registration
        self.assertEqual(response.status_code, 200)