from django.contrib import admin
from django.urls import path
from todoproject.views import *

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

]
