from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.contrib.auth.models import User

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
    200: success creating user
    301: user already exist
    400: invalid input data
    404: bad request type
}
"""
def registration(request):
    # registration
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DolbyUserSerializer(data = data)
        if serializer.is_valid():
            status = serializer.create(serializer.validated_data)[1]
            return JsonResponse(serializer.data, status = status)
        return JsonResponse({'error': 'invalid input data'}, status = 400)
    return JsonResponse({'error': 'bad request'}, status = 404)

# update user profile
"""
user profile update api
status code: {
    201: success updating user
    400: invalid input data
    401: user does not exist
    404: bad request
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
            return JsonResponse({'error': 'user does not exist'}, status = 401)
        if serializer.is_valid():
            status = serializer.update(user, serializer.validated_data)[1]
            return JsonResponse(serializer.data, status = status)
        return JsonResponse({'error': 'invalid input data'}, status = 400)
    return JsonResponse({'error': 'bad request'}, status = 404)