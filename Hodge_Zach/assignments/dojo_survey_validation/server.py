from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'bob'
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')

    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['language'] = request.form['language']

    if len(request.form['comment']) < 1:
        flash("Comment cannot be empty!")
        return redirect('/')

    session['comment'] = request.form['comment']

    if len(session['comment']) > 120:
        flash("Comment cannot be longer than 120 characters!")
        return redirect('/')
        
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html', name=session['name'], dojo=session['dojo'], language=session['language'], comment=session['comment'])

@app.route('/bob', methods=['POST'])
def go_back():
    return render_template('index.html')
app.run(debug=True)
