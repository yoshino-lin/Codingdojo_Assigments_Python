from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs!")
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog!")
def create(request):
    return redirect("/")
def number_edit(request, number):
    return HttpResponse("placeholder to edit blog "+str(number))
def number_return(request, number):
    return HttpResponse("placeholder to display blog number: "+str(number))
def destroy(request, number):
    return redirect("/")
