
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def first_function():
    return render_template("index.html")

@app.route("/quiz")
def second_function():
    return render_template("quiz.html")

@app.route("/login")
def third_function():
    return render_template("login.html")

@app.route("/loggedin", methods=["POST"])
def auth():
    name = request.form["user"]
    password = request.form["password"]
    print(name, password)
    return("index.html")





if __name__ == '__main__':
    app.run()
    # name = request.form["user"]
    # password = request.form["password"]
    # print(name, password)

