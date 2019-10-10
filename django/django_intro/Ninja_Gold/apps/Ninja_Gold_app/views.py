from django.shortcuts import render, HttpResponse, redirect
import time
import random
id = 0
def index(request):
    if 'player_gold' in request.session:
        pass
    else:
        request.session['player_gold'] = 0

    if 'player_activities' in request.session:
        pass
    else:
        request.session['player_activities'] = {}
    context={
        'player_gold':request.session['player_gold'],
        'player_activities':request.session['player_activities'],
    }
    return render(request,'Ninja_Gold_app/index.html',context)

def process_money(request):
    global id
    time_now = time.strftime("%Y/%m/%d %H:%M:%p", time.localtime())
    player_action = request.POST.get('building')
    if player_action == "farm":
        money_get = random.randint(10, 20)
    elif player_action == "cave":
        money_get = random.randint(5, 10)
    elif player_action == "house":
        money_get = random.randint(2, 5)
    elif player_action == "casino":
        money_get = random.randint(-50, 50)
        #money_get = random.randint(150, 350)
    if len(request.session['player_activities']) >= 15:
        if request.session['player_gold'] < 500:
            request.session['player_gold']+=0
            request.session['player_activities'][id]=["red","You failed! Try again.",""]
            id+=1
        else:
            request.session['player_gold']+=0
            request.session['player_activities'][id]=["green","You won!! Try again.",""]
            id+=1
    elif request.session['player_gold'] > 500:
        request.session['player_gold']+=0
        request.session['player_activities'][id]=["green","You won!! Try again.",""]
        id+=1
    else:
        if money_get<0:
            request.session['player_gold']+=money_get
            what_happend = "Enter a casino and lost "+str(0-money_get)+" gold... Ouch..."
            request.session['player_activities'][id]=["red",what_happend,time_now]
            id+=1
        else:
            request.session['player_gold']+=money_get
            what_happend = "Earn "+str(money_get)+" gold from "+player_action+"!"
            request.session['player_activities'][id]=["green",what_happend,time_now]
            id+=1
    print(request.session['player_activities'])
    return redirect('/')

def destroy_session(request):
    del request.session['player_gold'],
    del request.session['player_activities'],
    return redirect('/')
