from django.contrib.auth import authenticate, login
from django.shortcuts import render
from os import name
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User


# Create your views here.

def adminlogin(request):
    return render(request,'adminlogin.html')


def listall(request):
    name1=request.POST.get ('user_name')
    password1=request.POST.get('user_pass')
    admin = authenticate(username=name1,password=password1)

    if admin is  not None:  
        if admin.is_superuser:
            login(request,admin)
            users = User.objects.all()
            return render(request ,'showlist.html',{"users":users})

         
            
        else:
            return redirect(adminlogin)

    else:
        return render(request,'adminlogin.html')

# def search(request):
#       if 'q' in request.GET:
#           q=request.GET['q']
#           data= User.objects.filter(username=q)
#           return render(request,'showlist.html',{'data':data})

def deactivate(request,id):
    print(id)
    user = User.objects.get(id = id)
    print(user)
    user.is_active = False
    user.save()
    users = User.objects.all().order_by('id'    )
    return render(request,'showlist.html',{"users":users})



def activate(request,id):
    print(id)
    user = User.objects.get(id = id)
    print(user)
    user.is_active = True
    user.save()
    users = User.objects.all().order_by('id')
    return render(request,'showlist.html',{"users":users})
   
def delete(request,id ):
     u = User.objects.get(id = id)
     u.delete()
     users = User.objects.all().order_by('id')
     return render(request,'showlist.html',{"users":users})


     
def search(request):
    if  'search' in request.GET:
        search= request.GET['search']
        users=User.objects.filter( username=search)
        return render (request,'search.html',{'users':users})
 
   


   
      

    