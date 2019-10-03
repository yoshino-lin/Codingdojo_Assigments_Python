from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World!'

@app.route('/dojo')
def dojo():
   return 'Dojo'

@app.route('/say/<name>')
def say(name):
    return "Hi "+name.capitalize()+"!"  #.capitalize()首字母大写

@app.route('/repeat/<int:times>/<say_what>')
def say_many_time(times,say_what):
    say_return = ""
    for i in range(times):
        say_return += say_what +" "
    return say_return
@app.route('/<others>')
def warning_system(others):
    return "Sorry! No response. Try again."

if __name__ == '__main__':
   app.run(debug = True)
