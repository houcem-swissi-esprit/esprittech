"""
URL configuration for rdiTest project.

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

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib.auth.views import LoginView
from rdiapp.views import *

urlpatterns = [
    path("", index, name="index"),
    #path("register", StudentCreate.as_view, name='StudentCreate.as_view()'),
    path('add-project', ProjectCreate.as_view(), name='Add Project'),
    path('projects', ProjectList.as_view(), name='Projects'),
    path('apply-project', ApplicationCreate.as_view(), name='Application'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='Project Details'),
    path('login/', LoginView.as_view(), name="login"),
    
    
]

urlpatterns = format_suffix_patterns(urlpatterns)