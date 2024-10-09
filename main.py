from flask import Flask, render_template, request, redirect, url_for, session
import authentication as auth
import questions as q
from datetime import datetime
import timer
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
    if auth.check_score(username) == False:
        return render_template('loggedin.html', username=username, action="=/submitted")
    return render_template('loggedin.html', username=username, action="=/quiz")

@app.route("/submitted")
def submitted_function():
    username = session.get('username')
    score = auth.read_score(username)
    time = timer.calculate_time_difference(auth.read_start_time(username), auth.read_end_time(username))
    auth.update_total_time(time,username)
    return render_template("submit.html", username=username, score=score, time=time)

@app.route("/quiz")
def second_function():
    username = session.get('username')
    if auth.check_score(username) == False:
        return render_template('loggedin.html', username=username)
    starting_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    auth.update_starting_time(starting_time=starting_time,username=username)
    return render_template("quiz.html", action="/quiz")

@app.route("/submit", methods=['POST', 'GET'])
def submit_form():
    username = session.get('username')
    if auth.check_time(username):
        ans_dict = {}
        for i in range(1, 21, 1):
            print(request.form.get(f'Q{i}'))
            ans_dict[f'{i}'] = request.form.get(f'Q{i}')
        print(ans_dict)
        score = q.read_qa(ans_dict)
        print(score)
        submission_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(submission_time)
        starting_time=auth.read_start_time(username)
        time = timer.calculate_time_difference(starting_time,submission_time)
        auth.update_total_time(time,username)
        auth.update_score(ans_dict=ans_dict,score=score,submission_time=submission_time,username=username)
        return render_template('submit.html', username=username, score=score, time=time)
    else:
        score = auth.read_score(username)
        time = timer.calculate_time_difference(auth.read_start_time(username), auth.read_end_time(username))
        auth.update_total_time(time, username)
        return render_template("submit.html", username=username, score=score, time=time)


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

