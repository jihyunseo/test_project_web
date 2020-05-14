# from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello, Django!")

from django.http import JsonResponse
def home(request):
    name01 = request.GET['name']
    age02 = request.GET['age']
    # getRequestDict = request.GET;
    result= int(age02)+5
    requestDict={'result_response':result}
    return JsonResponse(requestDict)    