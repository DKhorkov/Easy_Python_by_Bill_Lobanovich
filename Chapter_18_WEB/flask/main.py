from flask import Flask, render_template, request


app = Flask(__name__)  # Default case of creating an application


@app.route("/")  # Base URL
def index():
    return render_template('index.html')


# @app.route("/<username>")  # Greeting URL
# def greeting(username):
#     return render_template('greeting.html', username=username)


@app.route("/greeting/", methods=("GET", "POST"))  # Greeting URL
def greeting():
    if request.method == 'POST':
        username = request.form['username']
        return render_template('greeting.html', username=username)
    return render_template('greeting.html')


@app.route('/echo/', methods=("GET", "POST"))  # Необходимо указать методы для корректной работы, иначе только GET
def echo():
    if request.method == 'POST':
        place = request.form['place']  # Передача аргумента через форму
        return render_template('echo.html', place=place)
    return render_template('echo.html')


app.run(port=5001, debug=True)

