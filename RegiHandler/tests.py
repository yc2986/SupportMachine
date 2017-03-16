from django.test import TestCase

import json
# rest framework
from RegiHandler.serializers import DolbyUserSerializer
from rest_framework.test import APIClient

client = APIClient()

# Create your tests here.
class DolbyUserSerializerTest(TestCase):
    def setUp(self):
        data = {
            # basic info
            'username': 'abcd',
            'password': '123456',
            'email': 'abcd@gmail.com',
            # profile info
            'company': 'foo',
            'registration_code': '123456',
            'phone_number': '1234567890',
        }
        response = client.post('/register/', data, format = 'json')

    def test_create_user_success(self):
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
    
    def test_create_user_invalid_data(self):
        data = {
            # basic info
            'username': 'abc',
            'password': '123456',
            # profile info
            'company': 'abc',
            'registration_code': '123456',
            'phone_number': '1234567890',
        }
        response = client.post('/register/', data, format = 'json')
        # check invalid data
        self.assertEqual(response.status_code, 400)
    
    def test_create_user_bad_request(self):
        data = {
            # basic info
            'username': 'abc',
            'password': '123456',
            'email': 'abc@gmail.com',
            # profile info
            'company': 'abc',
            'registration_code': '123456',
            'phone_number': '1234567890',
        }
        response = client.get('/register/', data, format = 'json')
        self.assertEqual(response.status_code, 404)
        response = client.put('/register/', data, format = 'json')
        self.assertEqual(response.status_code, 404)
        response = client.patch('/register/', data, format = 'json')
        self.assertEqual(response.status_code, 404)
        response = client.delete('/register/', data, format = 'json')
        self.assertEqual(response.status_code, 404)
        response = client.head('/register/', data, format = 'json')
        self.assertEqual(response.status_code, 404)
        response = client.options('/register/', data, format = 'json')
        self.assertEqual(response.status_code, 404)
    
    def test_create_user_already_exist(self):
        data = {
            # basic info
            'username': 'abcd',
            'password': '123456',
            'email': 'abcd@gmail.com',
            # profile info
            'company': 'foo',
            'registration_code': '123456',
            'phone_number': '1234567890',
        }
        response = client.post('/register/', data, format = 'json')
        # check duplicate registration
        self.assertEqual(response.status_code, 301)
    
    def test_update_user_success(self):
        data = {
            # basic info
            'username': 'abcd',
            'password': '123456',
            'email': 'cdef@gmail.com',
            # profile info
            'company': 'bar',
            'registration_code': '123',
            'phone_number': '234',
        }
        response = client.post('/update/', data, format = 'json')
        response_data = json.loads(response.content)
        # check success update
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response_data.get('email'), 'cdef@gmail.com')
        self.assertEqual(response_data.get('company'), 'bar')
        self.assertEqual(response_data.get('registration_code'), '123')
        self.assertEqual(response_data.get('phone_number'), '234')