from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.

from django.views import View
class GoodMorningView(View):
    def get(self,request):
        data={"message":"Good Morning"}
        return JsonResponse(data)

from django.views import View
class GoodEveningView(View):
    def get(self,request):
        data={"message":"Good Evening"}
        return JsonResponse(data)

from django.views import View
class HelloWorldView(View):
    def get(self,request):
        data={"message":"Hello World"}
        return JsonResponse(data)

from django.views import View
class GoodNightView(View):
    def get(self,request):
        data={"message":"Good Night"}
        return JsonResponse(data)

class Userdetails(View):
    def get(self,request):
        data=[
            {'name':'Sekha','age':23,'place':'ekm'},
            {'name': 'Mekha', 'age': 25, 'place': 'Tvm'},
            {'name': 'lekha', 'age': 27, 'place': 'ekm'}
        ]
        return JsonResponse(data,safe=False)