from flask import Flask, render_template, request, redirect, url_for
import authentication as auth
app = Flask(__name__)


@app.route("/")
def first_function():
    return render_template("index.html")


@app.route("/quiz")
def second_function():
    return render_template("quiz.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form["name"]
        password = request.form["Password"]
        if auth.check_password(name, password):
            return redirect(url_for('first_function'))

    return render_template("login.html")


if __name__ == '__main__':
    app.run(debug=True)

