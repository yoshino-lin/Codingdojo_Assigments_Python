from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default_board():
   return render_template("index.html", number_of_box_width=8, number_of_box_height=8, box_color1="red", box_color2="black")

@app.route('/<int:x>')
def default_board_2(x):
    return render_template("index.html", number_of_box_width=x, number_of_box_height=x, box_color1="red", box_color2="black")

@app.route('/<int:x>/<int:y>')
def default_board_3(x,y):
    return render_template("index.html", number_of_box_width=x, number_of_box_height=y, box_color1="red", box_color2="black")

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def default_board_4(x,y,color1,color2):
    return render_template("index.html", number_of_box_width=x, number_of_box_height=y, box_color1=color1, box_color2=color2)


if __name__ == '__main__':
   app.run(debug = True)
