from django.contrib import admin
from django.urls import path
from todoproject.views import *
from todoproject.userviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signupPage,name="signupPage"),
    path('signinPage/',signinPage,name="signinPage"),
    path('dashboard/',dashboard,name="dashboard"),
    path('logoutPage/',logoutPage,name="logoutPage"),
    
    path('addCategory/',addCategory,name="addCategory"),
    path('categoryList/',categoryList,name="categoryList"),
    path('editcategory/<str:myid>',editcategory,name="editcategory"),
    path('deletecategory/<str:myid>',deletecategory,name="deletecategory"),
    
    path('addTask/',addTask,name="addTask"),
    path('inbox/',inbox,name="inbox"),
    path('todayTaskList/',todayTaskList,name="todayTaskList"),
    path('upcommingTaskList/',upcommingTaskList,name="upcommingTaskList"),
    path('finishedTaskList/',finishedTaskList,name="finishedTaskList"),
    path('editTask/<str:myid>',editTask,name="editTask"),
    path('finishedTask/<str:myid>',finishedTask,name="finishedTask"),
    path('deleteTask/<str:myid>',deleteTask,name="deleteTask"),

]
