# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, Django!")

from django.http import JsonResponse
def home(request):
    name = request.GET['name']
    age = request.GET['age']
    getRequestDict = request.GET;
    return JsonResponse(getRequestDict)    