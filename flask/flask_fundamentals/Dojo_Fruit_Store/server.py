from flask import Flask, render_template, request, redirect
import time
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])
def checkout():
    strawberry_amount = int(request.form['strawberry'])
    raspberry_amount = int(request.form['raspberry'])
    apple_amount = int(request.form['apple'])
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    print("Charging "+first_name+" "+last_name+" for "+str(strawberry_amount+raspberry_amount+apple_amount)+" fruits")
    return render_template("checkout.html", strawberry_amount_checkout=strawberry_amount, raspberry_amount_check=raspberry_amount, apple_amount_amount=apple_amount, first_name_checkout=first_name, student_id_checkout=student_id, last_name_checkout=last_name, checkout_time=time.strftime('%b %d %Y %H:%M:%S %p',time.localtime(time.time())))

@app.route('/fruits')
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":
    app.run(debug=True)
