from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View
class First(View):
    def get(self,request):
        if (request.method == 'GET'):
            return HttpResponse("First page")

class Second(View):
    def get(self,request):
        if(request.method=='GET'):
            return HttpResponse("Second page")