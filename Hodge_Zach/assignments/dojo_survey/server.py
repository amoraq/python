from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'bob'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', name=session['name'], dojo=session['dojo'], language=session['language'], comment=session['comment'])

@app.route('/bob', methods=['POST'])
def go_back():
    return render_template('index.html')
app.run(debug=True)
