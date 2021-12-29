"""week5 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from re import template
from django.urls import path
from .import views
from django.http import HttpResponse

urlpatterns = [
    path('',views.adminlogin),
    path('list/',views.listall, name='list'),
    path('Deactivate/<int:id>',views.deactivate,name="Deactivate"),
    path('Activate/<int:id>',views.activate,name="Activate"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('search',views.search,name="search"),
    # path ('search',views.search,name='search')


    # path('index',views.index,name='iregester_pagendex')
    
]
