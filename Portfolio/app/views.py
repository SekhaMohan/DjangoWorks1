from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
class AboutApiView(View):
    def get(self,request):
        data=[
            {'id':101,'Full Name':'Sekha Mohan','Title':'Portfolio','Dob':'25-05-2003','email':"sekha@2003",'contact':45676569,'loc':"ekm","git_url":"https://github.com/SekhaMohan",'linkedin':"sekha,mohan"}
        ]
        return JsonResponse(data,safe=False)

class EducationAPIView(View):
    def get(self,request):
        data=[
            {'id':201,'institution':"CEA","Course":"Btech","University":"KTU","location":"Adoor","start_yr":"01/05/2022","End_yr":"25/05/2026","grade":"A","description":"Good"}
        ]
        return JsonResponse(data, safe=False)

class ProjectAPIView(View):
    def get(self,request):
        data=[
            {'id':301,"project_name":"Skill_Link","description":"A decentralized skill workers platform","technologies":"python,Vite,polygon,metaMask","duration":"6 months","LiveUrl":"https://skilllink.com"}
        ]
        return JsonResponse(data, safe=False)