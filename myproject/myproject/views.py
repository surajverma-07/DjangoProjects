from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
           'title': 'Home Page',
           'head':'This is the home page dynamically genrated',
           'Slist':['cpp','js','react','c','css','html'],
           'team_details':[
               {'name':'suraj kumar verma', 'phone':'6266939975'},
               {'name':'Palak Verma', 'phone':'9301202706'}
           ]
      }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Welcome to Suraj Kumar Verma's Profile")

def skills(request):
    return HttpResponse("sab aata hai mereko ha ha ")

def skillDetails(request,courseID):
    return HttpResponse(courseID)