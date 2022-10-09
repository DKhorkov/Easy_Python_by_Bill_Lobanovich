from flask import render_template, Flask, request


app = Flask(__name__)  # Task 1


# @app.route('/')  # Task 3
# def home():
#     return "It's alive!"


@app.route('/', methods=("GET", "POST"))  # Task 4 and 5, modernized by methods
def home():
    if request.method == 'POST':
        thing = request.form.get('thing')
        height = request.form.get('height')
        color = request.form.get('color')
        return render_template('home.html', thing=thing, height=height, color=color)
    return render_template('home.html')


app.run(host='Localhost', port=5000, debug=True)  # Task 1
