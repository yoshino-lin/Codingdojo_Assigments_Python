from django.shortcuts import render, HttpResponse, redirect
from apps.The_Wall_app.models import *
from django.contrib import messages

def index(request):
    context={
    }
    return render(request,'Login_and_Registration_app/index.html',context)
