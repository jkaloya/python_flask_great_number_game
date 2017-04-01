from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = "NumberGame"

def num_game():
    session['user_num'] = int(random.randrange(1,101))

@app.route('/')
def index():
    num_game()
    print session['user_num']
    return render_template("index.html")

@app.route('/check', methods=['POST'])
def check():
    print "Get POST info"
    session['guess'] = request.form['number']
    if int(session['guess']) > session['user_num']:
        print 'Too high!'
        session['Results']="Too high!"
    elif int(session['guess']) < session['user_num']:
        print 'Too low!'
        session['Results']="Too Low!"
    elif int(session['guess']) == session['user_num']:
        print 'Correct!'
        session['Results']= "Correct!"
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    for key in session.keys():
        session.pop(key, None)
    return redirect('/')

app.run(debug=True)
