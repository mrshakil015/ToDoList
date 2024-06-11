from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from todoapp.models import *

class CustomToDoUserForm(UserCreationForm):
    class Meta:
        model = CustomToDoUserModel
        fields = UserCreationForm.Meta.fields+("first_name","last_name","email","email","ProfilePic","UserType")

class CustomToDoUserAuthentationForm(AuthenticationForm):
    class Meta:
        model = CustomToDoUserModel
        fields = ("username","password")
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = ['CategoryName']
        
class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        fields = ['TaskName','TaskDescription','category','Priority','DueDate']
        exclude = ['CompletedDate']
        
        widgets = {
            'DueDate':forms.DateInput(attrs={
              'type'  :'date','class':'date-field'
            }),
            'CompletedDate':forms.DateInput(attrs={
                'type':'date'
            })
        }
        
        labels = {
            "TaskName":"Task Name",
            "TaskDescription":"Task Description",
            "DueDate":"Due Date",
        }
        
        