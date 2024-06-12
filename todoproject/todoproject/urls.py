from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from todoproject.views import *
from todoproject.userviews import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signupPage/',signupPage,name="signupPage"),
    path('',signinPage,name="signinPage"),
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
    path('searchTask/',searchTask,name="searchTask"),
    
    path('editTask/<str:myid>',editTask,name="editTask"),
    path('finishedTask/<str:myid>',finishedTask,name="finishedTask"),
    path('deleteTask/<str:myid>',deleteTask,name="deleteTask"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
