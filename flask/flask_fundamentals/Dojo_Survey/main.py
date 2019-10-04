from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def create_result():
    name_from_form = request.form['name']
    Dojo_Location_form = request.form['Dojo_Location']
    Favourite_Language_form = request.form['Favourite_Language']
    comment_form = request.form['comment']
    return render_template("result.html", name_on_template=name_from_form, location_on_template=Dojo_Location_form, language_on_template=Favourite_Language_form, comment_on_template=comment_form)
if __name__ == '__main__':
   app.run(debug = True)
