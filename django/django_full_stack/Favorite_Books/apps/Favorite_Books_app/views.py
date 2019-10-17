from django.shortcuts import render, HttpResponse, redirect
from apps.Favorite_Books_app.models import *
from django.contrib import messages
import time
import datetime

def index(request):
    context={
    }
    return render(request,'The_Wall_app/login.html',context)

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
            request.session['user_id'] = user.id
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name
            context={
                "username": request.session['first_name']+" "+request.session['last_name'],
                "all_comment":Comment.objects.all(),
                "all_message":Message.objects.all(),
                "user_id":request.session['user_id'],
            }
            return render(request,'The_Wall_app/index.html',context)
    else:
        context={
            "username": request.session['first_name']+" "+request.session['last_name'],
            "all_comment":Comment.objects.all(),
            "all_message":Message.objects.all(),
            "user_id":request.session['user_id'],
        }
        return render(request,'The_Wall_app/index.html',context)
def message_post(request):
    the_user = User.objects.get(id=request.session['user_id'])
    Message.objects.create(user=the_user,messages=request.POST['message_text'])
    return redirect('/success')

def comment_post(request,message_id):
    the_user = User.objects.get(id=request.session['user_id'])
    the_message = Message.objects.get(id=message_id)
    Comment.objects.create(user=the_user,message=the_message,comment=request.POST['comment_text'])
    return redirect('/success')

def delete_message(request,message_id):
    the_message = Message.objects.get(id=message_id)
    time_dif = datetime.datetime.now() - the_message.created_at
    if time_dif.seconds > 1800:
        the_message.delete()
    return redirect('/success')

def logout(request):
    del request.session['first_name']
    del request.session['last_name']
    del request.session['user_id']
    return redirect('/')
