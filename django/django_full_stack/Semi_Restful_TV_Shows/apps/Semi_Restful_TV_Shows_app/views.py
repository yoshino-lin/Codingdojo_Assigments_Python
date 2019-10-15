from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from apps.Semi_Restful_TV_Shows_app.models import *

def index(request):
    context = {
    }
    return render(request,'Semi_Restful_TV_Shows_app/index.html',context)
def show_index(request):
    return redirect('/shows')
def show(request):
    context = {
        "show_list":Show.objects.all(),
    }
    return render(request,'Semi_Restful_TV_Shows_app/show.html',context)
def show_add(request):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        the_title = request.POST.get('title_add')
        the_network = request.POST.get('network_add')
        the_release_date = request.POST.get('release_date_add')
        the_description = request.POST.get('description_add')
        Show.objects.create(title=the_title, network=the_network, release_date=the_release_date, desc = the_description)
        new_id = Show.objects.last().id
        return redirect('/shows/'+str(new_id))
def show_change(request,show_id):
    errors = Show.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect("/shows/"+str(show_id)+"/edit")
    else:
        the_show_to_update = Show.objects.get(id = show_id)
        the_show_to_update.title = request.POST.get('title_add')
        the_show_to_update.network = request.POST.get('network_add')
        the_show_to_update.release_date = request.POST.get('release_date_add')
        the_show_to_update.desc = request.POST.get('description_add')
        the_show_to_update.save()
    return redirect('/shows/'+str(show_id))

def show_display(request,show_id):
    context = {
        "the_show":Show.objects.get(id=show_id),
    }
    return render(request,'Semi_Restful_TV_Shows_app/show_info.html',context)
def original_info(request,show_id):
    context = {
        "the_show_to_edit":Show.objects.get(id=show_id),
    }
    return render(request,'Semi_Restful_TV_Shows_app/edit.html',context)

def destroy(request,show_id):
    Show.objects.get(id=show_id).delete()
    return redirect('/shows')
