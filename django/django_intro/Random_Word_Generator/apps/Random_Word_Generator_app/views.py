from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string

def index(request):
    if 'attempt_time' in request.session:
        request.session['attempt_time'] +=1
    else:
        request.session['attempt_time']=0

    if 'random_str' in request.session:
        pass
    else:
        request.session['random_str'] = get_random_string(length=14)
    context = {
        "attempt_time_index":request.session['attempt_time'],
        "random_str_indx":request.session['random_str'],
    }
    return render(request,'Random_Word_Generator_app/index.html',context)

def generate(request):
    request.session['random_str'] = get_random_string(length=14)
    return redirect("/")

def reset(request):
    del request.session['attempt_time']
    del request.session['random_str']
    return redirect("/")
