from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
import datetime
from todoproject.forms import *
from todoapp.models import *

def addTask(request):
    if request.method == 'POST':
        formdata = TaskForm(request.POST)
        
        if formdata.is_valid():
            task = formdata.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('inbox')
    else:
        formdata = TaskForm(request.POST)
    return render(request,'myuser/addtask.html',{'formdata':formdata})

def editTask(request,myid):
    taskdata = get_object_or_404(TaskModel,id=myid)
    if request.method == 'POST':
        edittaskinfo = TaskForm(request.POST, instance=taskdata)
        edittaskinfo.save()
        return redirect('inbox')
    else:
        edittaskinfo = TaskForm(instance=taskdata)

    return render(request,'myuser/edittask.html',{'edittaskinfo':edittaskinfo})
        

def inbox(request):
    current_user = request.user
    today = datetime.datetime.now()
    taskdata=TaskModel.objects.filter(Status = 'OnGoing', user = current_user)
    ongoing = TaskModel.objects.filter(DueDate = today, Status = 'OnGoing', user = current_user).count()
    finished = TaskModel.objects.filter(Status = 'Finished', user = current_user).count()
    upcomming = TaskModel.objects.filter(~Q(DueDate=today),Status = 'OnGoing',user=current_user).count()
    context = {
        'taskdata':taskdata,
        'ongoing':ongoing,
        'finished':finished,
        'upcomming':upcomming,
        }
    return render(request,'myuser/inbox.html',context)

def deleteTask(request,myid):
    taskdata = TaskModel.objects.get(id=myid)
    taskdata.delete()
    return redirect('inbox')

def todayTaskList(request):
    today = datetime.datetime.now()
    current_user = request.user
    taskdata = TaskModel.objects.filter(DueDate = today, Status = 'OnGoing', user = current_user)
    
    return render(request,'myuser/todaytasklist.html',{'taskdata':taskdata})

def upcommingTaskList(request):
    today = datetime.datetime.now()
    current_user = request.user
    taskdata = TaskModel.objects.filter(~Q(DueDate=today),Status = 'OnGoing',user=current_user)
    
    return render(request,'myuser/upcommingtasklist.html',{'taskdata':taskdata})

def finishedTask(request,myid):
    taskdata = get_object_or_404(TaskModel, id=myid)
    taskdata.Status = 'Finished'
    today = datetime.datetime.now()
    taskdata.CompletedDate=today
    taskdata.save()
    
    return redirect('finishedTaskList')

def finishedTaskList(request):
    current_user = request.user
    taskdata = TaskModel.objects.filter(Status = 'Finished',user=current_user)
    
    
    return render(request,'myuser/finishedtask.html',{'taskdata':taskdata})

def searchTask(request):
    try:
        if request.method == 'GET':
            query = request.GET.get("searchquery")
            
            search = TaskModel.objects.filter(
                Q(TaskName__icontains = query)|
                Q(DueDate__icontains = query)|
                Q(Created_at__icontains = query)
            )
            context = {
                'query':query,
                'search':search,
            }
        else:
            context={}
            print("Else work")
    except:
        context={}
    return render(request,'myuser/searchtask.html',context)

