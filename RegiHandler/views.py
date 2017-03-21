from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# rest related
# serializer
from RegiHandler.serializers import DolbyUserSerializer
# tool
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# token getter
@ensure_csrf_cookie
def token(request):
    return JsonResponse({})

# index
def index(request):
    return render(request, 'RegiHandler/index.html')

# registration
# remove this csrf_exempt later
"""
user registration api
status code: {
    201: success creating user
    400: bad request/invalid input data
    403: record already exist/csrf validation error
}
"""
def registration(request):
    # registration
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DolbyUserSerializer(data = data)
        if serializer.is_valid():
            data, status = serializer.create(serializer.validated_data)
            return JsonResponse(data, status = status)
        return JsonResponse({
            'message': 'invalid input data',
        }, status = 400)
    return JsonResponse({
        'message': 'bad request type',
    }, status = 400)

# user authentication and login
"""
user authentication api
status code: {
    200: login success
    400: bad request
    401: login failed
    403: csrf validation error
}
"""
def login_user(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'message': 'user already logged in',
        }, status = 400)
    # authentication
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            username = data.get('username'), 
            password = data.get('password'),
        )
        if user is not None:
            login(request, user)
            return JsonResponse({
                'message': 'login success',
                'username': user.username,
            }, status = 200)
        else:
            return JsonResponse({
                'message': 'login failed',
            }, status = 401)
    return JsonResponse({
        'message': 'bad request type',
    }, status = 400)

# logout
"""
user logout api
status code: {
    200: logout success
}
"""
@csrf_exempt
def logout_user(request):
    logout(request)
    return JsonResponse({
        'message': 'logout success'
    }, status = 200)

# update user profile
"""
user profile update api
status code: {
    200: success updating user
    400: bad request
    404: user does not exist
}
"""
def update_profile(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DolbyUserSerializer(data = data)
        # this update request is fired with login status
        # this ensures record existence
        # but for safety use does not exist is also checked
        try:
            user = User.objects.get(username = data.get('username'))
        except User.DoesNotExist:
            return JsonResponse({
                'message': 'record does not exist',
            }, status = 404)
        if serializer.is_valid():
            data, status = serializer.update(user, serializer.validated_data)
            return JsonResponse(data, status = status)
        return JsonResponse({
            'error': 'invalid input data',
        }, status = 400)
    return JsonResponse({
        'message': 'bad request type',
    }, status = 400)