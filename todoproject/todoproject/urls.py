from django.contrib import admin
from django.urls import path
from todoproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',signupPage,name="signupPage"),
    path('signinPage/',signinPage,name="signinPage"),
    path('dashboard/',dashboard,name="dashboard"),

]
