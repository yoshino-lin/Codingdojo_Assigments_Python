from django.shortcuts import render, HttpResponse, redirect
from apps.Login_and_Registration_app.models import *
from django.contrib import messages

def index(request):
    context={
    }
    return render(request,'Login_and_Registration_app/index.html',context)

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),email=request.POST.get('email'),password=pw_hash,birthday=request.POST.get('birthday'))
    return redirect('/')

def login(request):
    if 'first_name' not in request.session:
        errors = User.objects.basic_validator_2(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            user = User.objects.get(email=request.POST['email_login'])
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            context={
                "username": request.session['first_name']+" "+request.session['last_name']
            }
            return render(request,'Login_and_Registration_app/success.html',context)
    else:
        context={
            "username": request.session['first_name']+" "+request.session['last_name']
        }
        return render(request,'Login_and_Registration_app/success.html',context)
def logout(request):
    del request.session['first_name']
    del request.session['last_name']
    return redirect('/')
