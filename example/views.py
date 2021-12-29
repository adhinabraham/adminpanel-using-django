from os import name
from django import http
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.cache import cache_control


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logi(request):
    if request.user.is_authenticated:
        return redirect(checkval)
    else:
        return render(request,'login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)   
def checkval(request):
    if request.method == 'POST':
        name1 = request.POST.get("user_name")
        password1 = request.POST.get("user_pass")
        print(name1,password1)
        user = authenticate(username = name1, password = password1)
        if user is not None:
            login(request, user)
            return render(request,'index.html')
        else:
            return redirect(logi)
    if request.method == 'GET':
        if request.user.is_authenticated:
            return render(request,'index.html')
        else:
            return redirect(logi)


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def reg(request):
        return render(request,'regester.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def regdatabase(request):  
    name1=request.POST.get('name_ofuser')
    print(name1)
    mail1=request.POST.get('email_ofuser')
    passwrd1=request.POST.get('pass_ofuser')

    user=User.objects.create_user(username = name1,email = mail1, password = passwrd1)
    user.save()
    return redirect(logi)

def logoutee(request):
    logout(request)
    return redirect(logi)
    

