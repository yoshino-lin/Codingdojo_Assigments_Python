from django.shortcuts import render, HttpResponse, redirect
from apps.Favorite_Books_app.models import *
from django.contrib import messages
import time
import datetime

def index(request):
    context={
    }
    return render(request,'Favorite_Books_app/login.html',context)

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
                "user_id":request.session['user_id'],
                "all_books":Book.objects.all(),
                "this_user":User.objects.get(id=request.session['user_id'])
            }
            return render(request,'Favorite_Books_app/index.html',context)
    else:
        context={
            "username": request.session['first_name']+" "+request.session['last_name'],
            "user_id":request.session['user_id'],
            "all_books":Book.objects.all(),
            "this_user":User.objects.get(id=request.session['user_id'])
        }
        return render(request,'Favorite_Books_app/index.html',context)

def book_add(request):
    this_use = User.objects.get(id=request.session['user_id'])
    Book.objects.create(title=request.POST['title_of_the_book_to_add'],desc=request.POST["desc_of_the_book_to_add"],uploaded_by=this_use)
    this_book = Book.objects.get(title=request.POST['title_of_the_book_to_add'])
    this_book.users_who_like.add(this_use)
    return redirect('/success')

def book_edit(request,book_id):
    context={
        "this_user":User.objects.get(id=request.session['user_id']),
        "the_book":Book.objects.get(id=book_id),
    }
    return render(request,'Favorite_Books_app/edit.html',context)

def book_update(request,book_id):
    the_book = Book.objects.get(id=book_id)
    the_book.title=request.POST['book_new_title']
    the_book.desc=request.POST['book_new_desc']
    the_book.save()
    context={
        "this_user":User.objects.get(id=request.session['user_id']),
        "the_book":Book.objects.get(id=book_id),
    }
    return render(request,'Favorite_Books_app/edit.html',context)

def book_delete(request,book_id):
    c = Book.objects.get(id=book_id)
    c.delete()
    return redirect('/success')

def unfavorite(request,book_id):
    the_user=User.objects.get(id=request.session['user_id'])
    the_book=Book.objects.get(id=book_id)
    the_user.liked_books.remove(the_book)
    return redirect('/success')

def book_display(request,book_id):
    context={
        "this_user":User.objects.get(id=request.session['user_id']),
        "the_book":Book.objects.get(id=book_id),
    }
    return render(request,'Favorite_Books_app/info_display.html',context)

def addfavorite(request,book_id):
    the_user=User.objects.get(id=request.session['user_id'])
    the_book=Book.objects.get(id=book_id)
    the_user.liked_books.add(the_book)
    return redirect('/success')

def logout(request):
    del request.session['first_name']
    del request.session['last_name']
    del request.session['user_id']
    return redirect('/')
