from flask import Flask, render_template, request, redirect, session
import random
import time
app = Flask(__name__)
app.secret_key = 'cheatcode'

@app.route('/')
def index():
    if 'player_gold' not in session:
        session['player_gold'] = 0
    if 'player_activities' not in session:
        session['player_activities'] = []
    if 'color' not in session:
        session['color'] = []
    return render_template("index.html", gold_amount=session['player_gold'], player_activities_list = session['player_activities'], list_len=len(session['player_activities']), color=session['color'])

@app.route('/process_money', methods=['POST'])
def money_count():
    time_now = time.strftime("%Y/%m/%d %H:%M:%p", time.localtime())
    player_action = request.form['building']
    if player_action == "farm":
        money_get = random.randint(10, 20)
    elif player_action == "cave":
        money_get = random.randint(5, 10)
    elif player_action == "house":
        money_get = random.randint(2, 5)
    elif player_action == "casino":
        money_get = random.randint(-50, 50)
    session['player_gold']+=money_get
    if len(session['player_activities']) >= 5:
        if session['player_gold'] < 500:
            session['color'].append("red")
            session['player_activities'].append("lose")
        else:
            session['color'].append("green")
            session['player_activities'].append("win")
    if money_get<0:
        session['color'].append("red")
        session['player_activities'].append("Enter a casino and lost "+str(0-money_get)+" gold... Ouch...("+time_now+")")
    else:
        session['color'].append("green")
        session['player_activities'].append("Earn "+str(money_get)+" gold from "+player_action+"! ("+time_now+")")
    return redirect('/')

@app.route('/destroy_session')
def clear_cookie():
    session.clear()		# clears all keys
    #session.pop('count')    //clears a specific key
    return redirect('/')

if __name__ == '__main__':
   app.run(debug = True)
