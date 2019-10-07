from flask import Flask, render_template, request, redirect, session
import base64
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'number_to_guess' not in session:
        session['number_to_guess'] = random.randint(1, 100)
    if 'guess_time' not in session:
        session['guess_time'] = 0
    return render_template("index.html", how_many_time_guess = session['guess_time'])

@app.route('/', methods=['POST'])
def index2():
    if session['guess_time'] < 4:
        player_guess = request.form['guess']
        if int(player_guess) > session['number_to_guess']:
            session['guess_time'] += 1
            return render_template("index.html", feed_back="Too high", color="red", how_many_time_guess = session['guess_time'])
        elif int(player_guess) < session['number_to_guess']:
            session['guess_time'] += 1
            return render_template("index.html", feed_back="Too Low", color="red", how_many_time_guess = session['guess_time'])
        else:
            session['guess_time'] += 1
            return render_template("index.html", feed_back=str(session['number_to_guess'])+" was the number!", color="green", how_many_time_guess = session['guess_time'])
    else:
        return render_template("index.html", feed_back="You Lose!", color="yellow", how_many_time_guess = session['guess_time'])


@app.route('/destroy_session')
def clear_cookie():
    session.clear()		# clears all keys
    #session.pop('count')    //clears a specific key
    return redirect('/')


if __name__ == '__main__':
   app.run(debug = True)
