from django.http import HttpResponse
from django.shortcuts import render

def home(request):
 return render(request,"index.html")
def signupF(request):
 return render(request,"signup.html")
def signupC(request):
 return render(request,"signup_ewaste.html")
def signuplogV(request):
 return render(request,"Vsignuplogin.html")
def loginE(request):
 return render(request,"login_ewaste.html")

def loginC(request):
 ans = ""
 try:
#   name = request.GET['username']
#   passw = request.GET['password']
  name = request.GET.get('username')
  passw = request.GET.get('password')
  ans = name+passw
 except:
  pass  
 return render(request,"loginc.html",{'output':ans})

def recycleD(request):
 return render(request,"recycle_dashboard.html")
def status(request):
 return render(request,"status.html")
def orderC(request):
 return render(request,"orderconfirm.html")
def Home(request):
 return render(request,"home.html")
def Form(request):
 return render(request,"form.html")
def Submit(request):
 return render(request,"submit.html")
def Info(request):
 return render(request,"information.html")
def Near(request):
 return render(request,"nearest1.html")
def Credit(request):
 return render(request,"credit.html")
def Vdash(request):
 return render(request,"voldashboard.html")
 