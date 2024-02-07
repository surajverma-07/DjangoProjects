from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
           'title': 'Home Page'
      }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("Welcome to Suraj Kumar Verma's Profile")

def skills(request):
    return HttpResponse("sab aata hai mereko ha ha ")

def skillDetails(request,courseID):
    return HttpResponse(courseID)