from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from todoproject.forms import *


def signupPage(request):
    if request.method == 'POST':
        signupform = CustomToDoUserForm(request.POST, request.FILES)
        print(signupform)
        
        if signupform.is_valid():
            signupform.save()
            
            messages.success(request,"Signup Successfully")
            return redirect('signinPage')
    else:
        signupform = CustomToDoUserForm()
    
    context = {
        'signupform':signupform
    }
    
    return render(request,'signup.html',context)

def signinPage(request):
    if request.method=='POST':
        signinform = CustomToDoUserAuthentationForm(request,data=request.POST)
        
        if signinform.is_valid():
            user = signinform.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        signinform = CustomToDoUserAuthentationForm()
    context = {
        'signinform':signinform
    }
    
    return render(request,'signin.html',context)

@login_required
def dashboard(request):
    
    return render(request,'dashboard.html')

def logoutPage(request):
    logout(request)
    
    return redirect('signinPage')