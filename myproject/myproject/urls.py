"""
URL configuration for myproject project.

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
from myproject import views

urlpatterns = [
    path('admin-me/', admin.site.urls),
    path('about-us/',views.aboutUs),
    path('skills/',views.skills),
    # path('skills/<int:courseID>/',views.skillDetails)
    # path('skills/<str:courseID>/',views.skillDetails)
    # path('skills/<slug:courseID>/',views.skillDetails)
    path('skills/<courseID>/',views.skillDetails),
    path('',views.homePage)
]
