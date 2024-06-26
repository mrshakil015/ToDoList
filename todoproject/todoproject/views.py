from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from todoproject.forms import *
from todoapp.models import *
from todoproject.userviews import inbox


def signupPage(request):
    if request.method == 'POST':
        formdata = CustomToDoUserForm(request.POST, request.FILES)

        if formdata.is_valid():
            signupform = formdata.save(commit=False)
            signupform.UserType = 'Viewer'
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
            if user.UserType == 'Viewer':
                return redirect('inbox')
            else:
                return redirect('categoryList')
    else:
        signinform = CustomToDoUserAuthentationForm()
    context = {
        'signinform':signinform
    }
    
    return render(request,'signin.html',context)


def logoutPage(request):
    logout(request)
    
    return redirect('signinPage')

def addCategory(request):
    if request.method == 'POST':
        current_user = request.user
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = current_user
            category.save()
            return redirect('categoryList')
    else:
        form = CategoryForm()
    context = {
        'form':form
    }
    
    return render(request,'myadmin/addcategory.html',context)

def categoryList(request):
    categorydata = CategoryModel.objects.all()
    
    return render(request,'myadmin/categorylist.html',{'categorydata':categorydata})

def editcategory(request,myid):
    category = get_object_or_404(CategoryModel,id = myid)
    if request.method == 'POST':
        editform = CategoryForm(request.POST,instance=category)
        if editform.is_valid():
            editform.save()
            return redirect('categoryList')
    else:
        editform = CategoryForm(instance=category)
        
    return render(request,'myadmin/editcategory.html',{'editform':editform})

def deletecategory(request,myid):
    category = get_object_or_404(CategoryModel,id=myid)
    category.delete()
    return redirect('categoryList')
        
def userList(request):
    userdata = CustomToDoUserModel.objects.filter(UserType = "Viewer")
    
    context = {
        "userdata":userdata
    }    
    return render(request,'myadmin/userlist.html',context)

def deleteUser(request,myid):
    userdata = get_object_or_404(CustomToDoUserModel,id=myid)
    userdata.delete()
    return redirect('userList')
