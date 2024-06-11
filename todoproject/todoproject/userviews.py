from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from todoproject.forms import *
from todoapp.models import *

def addTask(request):
    if request.method == 'POST':
        formdata = TaskForm(request.POST)
        
        if formdata.is_valid():
            formdata.save()
            
            return redirect('inbox')
    else:
        formdata = TaskForm(request.POST)
    return render(request,'myuser/addtask.html',{'formdata':formdata})

def inbox(request):
    taskdata=TaskModel.objects.all()
    
    return render(request,'myuser/inbox.html',{'taskdata':taskdata})

def deleteTask(request,myid):
    taskdata = TaskModel.objects.get(id=myid)
    taskdata.delete()
    return redirect('inbox')