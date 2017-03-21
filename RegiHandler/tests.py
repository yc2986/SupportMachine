from django.test import TestCase
from django.contrib.auth.models import User

import json
# rest framework
from RegiHandler.serializers import DolbyUserSerializer
from rest_framework.test import RequestsClient

#client = APIClient()
client = RequestsClient()

def csrf():
    return client.get('http://testserver/token/').cookies['csrftoken']

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
        response = client.post(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )

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
        response = client.post(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check successful registration
        self.assertEqual(response.status_code, 201)
    
    def test_create_user_incomplete_data(self):
        data = {
            # basic info
            'username': 'abc',
            'password': '123456',
            # profile info
            'company': 'abc',
            'registration_code': '123456',
            'phone_number': '1234567890',
        }
        response = client.post(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check invalid input
        self.assertEqual(response.status_code, 400)
    
    def test_create_user_invalid_email(self):
        data = {
            # basic info
            'username': 'abcde',
            'password': '123456',
            'email': 'abcdgmail.com',
            # profile info
            'company': 'dolby laboratories',
            'registration_code': '123456',
            'phone_number': '1234567890',
        }
        response = client.post(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check invalid input
        self.assertEqual(response.status_code, 400)
    
    def test_create_user_duplicated_email(self):
        data = {
            # basic info
            'username': 'abcde',
            'password': '123456',
            'email': 'abcd@gmail.com',
            # profile info
            'company': 'dolby laboratories',
            'registration_code': '123456',
            'phone_number': '1234567890',
        }
        response = client.post(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check already exist record
        self.assertEqual(response.status_code, 403)
    
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
        response = client.get(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
        response = client.put(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
        response = client.patch(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
        response = client.delete(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
        response = client.head(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
        response = client.options(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
    
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
        response = client.post(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check duplicate registration
        self.assertEqual(response.status_code, 403)
    
    def test_create_user_no_csrf(self):
        data = {
            # basic info
            'username': 'abcdef',
            'password': '123456',
            'email': 'abcdef@gmail.com',
            # profile info
            'company': 'foo',
            'registration_code': '123456',
            'phone_number': '1234567890',
        }
        response = client.post(
            'http://testserver/register/', 
            json = data, 
        )
        # check failed csrf validation
        self.assertEqual(response.status_code, 403)
    
    def test_update_user_success(self):
        data = {
            # basic info
            'username': 'abcd',
            'password': '123456',
            'email': 'cdef@gmail.com',
            # profile info
            'company': 'foo',
            'registration_code': '123456',
            'phone_number': '234',
        }
        response = client.post(
            'http://testserver/update/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        response_data = json.loads(response.content)
        # check success update
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response_data.get('email'), 'cdef@gmail.com')
        self.assertEqual(response_data.get('phone_number'), '234')
    
    def test_update_user_incomplete_data(self):
        data = {
            # basic info
            'username': 'abcd',
            'password': '123456',
            # profile info
            'company': 'bar',
            'registration_code': '123',
            'phone_number': '234',
        }
        response = client.post(
            'http://testserver/update/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check invalid input
        self.assertEqual(response.status_code, 400)

    def test_update_user_invalid_email(self):
        data = {
            # basic info
            'username': 'abcd',
            'password': '123456',
            'email': 'abcdgmail.com',
            # profile info
            'company': 'bar',
            'registration_code': '123',
            'phone_number': '234',
        }
        response = client.post(
            'http://testserver/update/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check invalid input
        self.assertEqual(response.status_code, 400)

    def test_update_user_bad_request(self):
        data = {
            # basic info
            'username': 'abcd',
            'password': '123456',
            'email': 'ayhg@gmail.com',
            # profile info
            'company': 'bar',
            'registration_code': '123',
            'phone_number': '234',
        }
        response = client.get(
            'http://testserver/update/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
        response = client.put(
            'http://testserver/update/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
        response = client.patch(
            'http://testserver/update/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
        response = client.delete(
            'http://testserver/update/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
        response = client.head(
            'http://testserver/update/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
        response = client.options(
            'http://testserver/update/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        self.assertEqual(response.status_code, 400)
    
    def test_update_user_no_csrf(self):
        data = {
            # basic info
            'username': 'abcd',
            'password': '123456',
            'email': 'cdefg@gmail.com',
            # profile info
            'company': 'bar',
            'registration_code': '123',
            'phone_number': '234',
        }
        response = client.post(
            'http://testserver/update/', 
            json = data, 
        )
        # check failed csrf validation
        self.assertEqual(response.status_code, 403)
    
    def test_user_group_client(self):
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
        response = client.post(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check successful registration
        self.assertEqual(response.status_code, 201)
        # check client group
        username = json.loads(response.content).get('username')
        user = User.objects.get(username = username)
        self.assertTrue(user.groups.filter(name = 'client').exists())
        self.assertFalse(user.is_staff)

    def test_user_group_admin(self):
        data = {
            # basic info
            'username': 'yc2986',
            'password': '123456',
            'email': 'yuzhou.cheng@dolby.com',
            # profile info
            'company': 'dolby laboratories',
            'registration_code': '123456',
            'phone_number': '1234567890',
        }
        response = client.post(
            'http://testserver/register/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check successful registration
        self.assertEqual(response.status_code, 201)
        # check client group
        username = json.loads(response.content).get('username')
        user = User.objects.get(username = username)
        self.assertTrue(user.groups.filter(name = 'admin').exists())
        self.assertTrue(user.is_staff)
    
    def test_user_login_success(self):
        data = {
            'username': 'abcd',
            'password': '123456',
        }
        response = client.post(
            'http://testserver/login/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check successful authentication
        self.assertEqual(response.status_code, 200)
    
    def test_user_login_fail(self):
        data = {
            'username': 'abcd',
            'password': '1234',
        }
        response = client.post(
            'http://testserver/login/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check failed authentication
        self.assertEqual(response.status_code, 401)

    def test_user_login_invalid_input(self):
        data = {}
        response = client.post(
            'http://testserver/login/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check failed authentication
        self.assertEqual(response.status_code, 401)

    def test_user_login_exists(self):
        data = {
            'username': 'abcd',
            'password': '123456',
        }
        # first login
        response = client.post(
            'http://testserver/login/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check successful authentication
        self.assertEqual(response.status_code, 200)
        # second login
        response = client.post(
            'http://testserver/login/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check duplicate authentication
        self.assertEqual(response.status_code, 400)

    def test_user_login_no_csrf(self):
        data = {
            'username': 'abcd',
            'password': '1234',
        }
        response = client.post(
            'http://testserver/login/', 
            json = data, 
        )
        # check csrf missing
        self.assertEqual(response.status_code, 403)
    
    def test_user_logout_success_with_csrf(self):
        data = {
            'username': 'abcd',
            'password': '123456',
        }
        # login
        response = client.post(
            'http://testserver/login/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check successful authentication
        self.assertEqual(response.status_code, 200)
        # logout
        response = client.post(
            'http://testserver/logout/',
            headers = {'X-CSRFToken': csrf()}
        )
        # check successful logout
        self.assertEqual(response.status_code, 200)
    
    def test_user_logout_success_without_csrf(self):
        data = {
            'username': 'abcd',
            'password': '123456',
        }
        # login
        response = client.post(
            'http://testserver/login/', 
            json = data, 
            headers = {'X-CSRFToken': csrf()}
        )
        # check successful authentication
        self.assertEqual(response.status_code, 200)
        # logout
        response = client.post(
            'http://testserver/logout/',
        )
        # check successful logout
        self.assertEqual(response.status_code, 200)