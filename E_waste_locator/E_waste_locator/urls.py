"""
URL configuration for E_waste_locator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from E_waste_locator import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home),
    path("signup/",views.signupF),
    path("signup_ewaste/",views.signupC,name="signupE"),
    path("signuploginv/",views.signuplogV),
    path("login_ewaste/",views.loginE),
    path("loginc/",views.loginC),
    path("recycle_dashboard/",views.recycleD),
    path("status/",views.status),
    path("orderc/",views.orderC),
    path("home/",views.Home,name="home"),
    path("form/",views.Form),
    path("fsubmit/",views.Submit),
    path("information/",views.Info),
    path("nearest/",views.Near),
    path("credit/",views.Credit),
    path("voldashboard/",views.Vdash),
]
