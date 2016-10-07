from flask import Flask, session, render_template, redirect
app = Flask(__name__)
app.secret_key = "Thisismysecretkey"

@app.route('/')
def index():
    if not 'count' in session:
        session['count'] = 0
    session['count'] += 1

    return render_template('index.html', count=session['count'])

@app.route('/ninja', methods=['POST'])
def ninja():
    if not 'count' in session:
        session['count'] = 0
    session['count'] += 1

    return redirect('/')

@app.route('/hacker', methods=['POST'])
def hacker():
    session.clear();

    return redirect('/')
app.run(debug=True)
