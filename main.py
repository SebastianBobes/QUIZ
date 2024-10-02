from flask import Flask, render_template, request, redirect, url_for, session
import authentication as auth
app = Flask(__name__)
app.secret_key = 'acwo2024'
@app.route("/")
def first_function():
    return render_template("index.html")

@app.route("/loggedin")
def loggedin_function():
    username = session.get('username')
    if username ==None:
        return render_template("index.html")
    return render_template('loggedin.html', username=username)


@app.route("/quiz")
def second_function():
    return render_template("quiz.html")


@app.route("/login", methods=['POST', 'GET'])
def login():
    # if 'username' in session:
    #     return redirect(url_for('index.html'))
    if request.method == 'POST':
        name = request.form["name"]
        password = request.form["Password"]
        if auth.check_password(name, password):
            session['username']=name
            print(session['username'])
            return redirect(url_for('loggedin_function'))

    return render_template("login.html")
@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('first_function'))


if __name__ == '__main__':
    app.run(debug=True)

