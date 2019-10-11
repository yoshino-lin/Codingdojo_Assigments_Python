from django.shortcuts import render, HttpResponse, redirect
from apps.Books_Authors_with_Templates_app.models import *

def index(request):
    context={
        "books_list":Book.objects.all(),
    }
    return render(request,'Books_Authors_with_Templates_app/index.html',context)

def authors(request):
    context={
        "authors_list":Author.objects.all(),
    }
    return render(request,'Books_Authors_with_Templates_app/authors.html',context)


def destroy_session(request):
    return redirect('/')
