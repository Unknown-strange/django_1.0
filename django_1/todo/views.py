from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.

def home(request):
    
    queryData = Task.objects.get(id=3)
    
    contexts = {'tasks': queryData}
    
    
    return render(request,'index.html',context=contexts)

def registration(request):
    return render(request,'register.html')

def my_login(request):
    return render(request,'my_login.html')






 