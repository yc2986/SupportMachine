from django.shortcuts import render
from django.http import JsonResponse, Http404

# index
def index(request):
    return render(request, 'RegiHandler/index.html')
