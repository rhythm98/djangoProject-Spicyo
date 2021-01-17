from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def add(request):
    print("Hello World")
    return render(request,'add.html',{'name':'Rhythm'})

def addResult(request):
    num1=int(request.POST['num1'])
    num2=int(request.POST['num2'])
    return render(request,'addResult.html',{'result':num1+num2})