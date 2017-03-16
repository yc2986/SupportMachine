from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# rest related
# serializer
from RegiHandler.serializers import DolbyUserSerializer
# tool
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

# index
def index(request):
    return render(request, 'RegiHandler/index.html')

# registration
@csrf_exempt
def registration(request):
    # registration
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DolbyUserSerializer(data = data)
        if serializer.is_valid():
            serializer.create_or_update(serializer.validated_data)
            return JsonResponse(serializer.data, status = 200)
        return JsonResponse(serializer.errors, status = 400)
    return JsonResponse({'error': 'request failed.'}, status = 404)