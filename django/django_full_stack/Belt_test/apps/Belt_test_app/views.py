from django.shortcuts import render, HttpResponse, redirect
from apps.Belt_test_app.models import *
from django.contrib import messages
import time
import datetime

def index(request):
    if 'first_name' in request.session:
        return redirect('/dashboard')
    else:
        context={
        }
        return render(request,'Belt_test_app/login.html',context)

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),email=request.POST.get('email'),password=pw_hash)
        user = User.objects.get(email=request.POST['email'])
        request.session['user_id'] = user.id
        request.session['first_name'] = user.first_name
        request.session['last_name'] = user.last_name
        context={
            "username": request.session['first_name']+" "+request.session['last_name'],
            "user_id":request.session['user_id'],
            "this_user":User.objects.get(id=request.session['user_id']),
            "this_users_trips":Trip.objects.filter(uploaded_by=User.objects.get(id=request.session['user_id'])),
            "this_users_trips_go":Trip.objects.filter(users_who_go=User.objects.get(id=request.session['user_id'])),
            "other_trips":Trip.objects.exclude(uploaded_by=User.objects.get(id=request.session['user_id'])),
        }
        return render(request,'Belt_test_app/index.html',context)


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
                "this_user":User.objects.get(id=request.session['user_id']),
                "this_users_trips":Trip.objects.filter(uploaded_by=User.objects.get(id=request.session['user_id'])),
                "this_users_trips_go":Trip.objects.filter(users_who_go=User.objects.get(id=request.session['user_id'])),
                "other_trips":Trip.objects.exclude(uploaded_by=User.objects.get(id=request.session['user_id'])),
            }
            return render(request,'Belt_test_app/index.html',context)
    else:
        context={
            "username": request.session['first_name']+" "+request.session['last_name'],
            "user_id":request.session['user_id'],
            "this_user":User.objects.get(id=request.session['user_id']),
            "this_users_trips":Trip.objects.filter(uploaded_by=User.objects.get(id=request.session['user_id'])),
            "this_users_trips_go":Trip.objects.filter(users_who_go=User.objects.get(id=request.session['user_id'])),
            "other_trips":Trip.objects.exclude(uploaded_by=User.objects.get(id=request.session['user_id'])),
        }
        return render(request,'Belt_test_app/index.html',context)

def new(request):
    if 'first_name' not in request.session:
        return redirect('/')
    else:
        context={
            "username": request.session['first_name']+" "+request.session['last_name'],
        }
        return render(request,'Belt_test_app/new.html',context)

def create_trip(request):
    errors = Trip.objects.basic_validator3(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/new')
    else:
        user = User.objects.get(id=request.session['user_id'])
        Trip.objects.create(Destination=request.POST['Desination_add'],start_at=request.POST['Start_date_add'],end_at=request.POST['End_date_add'],plan=request.POST["Plan_add"],uploaded_by=user)
        return redirect('/dashboard')

def trip_delete(request,trip_id):
    the_trip_to_delet = Trip.objects.get(id=trip_id)
    if the_trip_to_delet.uploaded_by.id == request.session['user_id']:
        the_trip_to_delet.delete()
    else:
        pass
    return redirect('/dashboard')

def edit(request,trip_id):
    if 'first_name' not in request.session:
        return redirect('/')
    else:
        the_trip = Trip.objects.get(id=trip_id)
        start_time = the_trip.start_at.strftime("%Y-%m-%d")
        end_time = the_trip.end_at.strftime("%Y-%m-%d")
        context={
            "username": request.session['first_name']+" "+request.session['last_name'],
            "trip_editing" : Trip.objects.get(id=trip_id),
            'start_time_edit':start_time,
            'end_time_edit':end_time,
        }
        return render(request,'Belt_test_app/edit.html',context)

def edit_trip(request,trip_id):
    errors = Trip.objects.basic_validator3(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit/'+str(trip_id))
    else:
        the_trip = Trip.objects.get(id=trip_id)
        the_trip.Destination=request.POST['Desination_add']
        the_trip.start_at=request.POST['Start_date_add']
        the_trip.end_at=request.POST['End_date_add']
        the_trip.plan=request.POST["Plan_add"]
        the_trip.save()
        return redirect('/dashboard')

def trips_info(request,trip_id):
    if 'first_name' not in request.session:
        return redirect('/')
    else:
        context={
            "username": request.session['first_name']+" "+request.session['last_name'],
            "trip_display" : Trip.objects.get(id=trip_id),
        }
        return render(request,'Belt_test_app/display.html',context)

def join_the_trip(request,trip_id):
    the_trip = Trip.objects.get(id=trip_id)
    the_trip.users_who_go.add(User.objects.get(id=request.session['user_id']))
    return redirect('/dashboard')

def cancel_trip(request,trip_id):
    the_trip = Trip.objects.get(id=trip_id)
    the_trip.users_who_go.remove(User.objects.get(id=request.session['user_id']))
    return redirect('/dashboard')

def logout(request):
    del request.session['first_name']
    del request.session['last_name']
    del request.session['user_id']
    return redirect('/')
