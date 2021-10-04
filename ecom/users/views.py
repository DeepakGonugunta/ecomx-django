
from django.shortcuts import render,redirect
from.forms import register_user,login_user,aform
from django.contrib.auth.forms  import UserCreationForm
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from .models import *
from .utils import *
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.


def register(request):
    form=register_user()

    context={
        'form':form
    }
    return render(request,'users/register.html',context)


def login(request):
    form=login_user()
    context={
        'form':form
    }
    return render(request,'users/login.html',context)

def create(request):
    username=request.POST.get('username')
    email=request.POST.get('email')
    password1=request.POST.get('password1')
    password2=request.POST.get('password2')
    if User.objects.filter(email=email).exists():
        messages.info(request,"email already taken")
    elif len(password1)<10:
        messages.info(request,"password length must be at least 10 characters")
    else:
        user=User.objects.create_user(username=username,email=email,password=password1)
        user.save()
        print("ok")
        return redirect('user_login')
    return redirect('user_register')
      
def login_authentication(request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request,user)
        print(user)
        return redirect('home')
        
    else:
        messages.info(request,'check the credentials')
        return redirect('user_login')
        

def loggout(request):
    logout(request)
    print("logout success")
    return redirect('home')



def addsave(request):
    form=aform()
    context={
        'form': form,
    }
    return render(request,'users/address.html',context)

def showadd(request):
    user=request.user
    a=address.objects.filter(user=user)
    context={
        'ad':a,
    }
    return render(request,'users/show.html',context)



def main_view(request):
    men=female=0
    p=payment2.objects.all()
    for x in p:
        if x.parent == 'men':
            men+=1
        else:
            female+=1
    
    
    chart=bar(p)
    chart2=get_plot(men,female)
    chart3=fbar(p)
    chart4=payment_type(p)
    context={
        'chart':chart,
        'chart2':chart2,
        'chart3':chart3,
        'chart4':chart4

    }
    return render(request,'users/show.html',context)
    