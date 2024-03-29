from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.model import Model
from flask_app.models.user import User

# ==========================================================
# ROUTES
# ==========================================================

# render_template
    # required import to connect HTML and ROUTING
    # NEEDS to have HTML in the same name
        # refer to @app.route('/httpsresponse') return statement
# request
    # works together with form
# redirect
    # works together with form
# session

# bcrypt

# naming convention
    # file name
        # plural



@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/<int:number>')
# PARAMETER with < > needs to be CASTED below
def number(number):
# PARAMETER within function matches CASTED variable from ROUTE
    newNum = number * 5
    return f'The number is { newNum }'


@app.route('/<name>')
# PARAMETER with < > needs to be CASTED below
def hello(name):
# PARAMETER within function matches CASTED variable from ROUTE
    return render_template('display.html', name = name, num = 8)
    # RENDER_TEMPLATE renders your basic HTML template
    # RENDER_TEMPLATE requires TEMPLATES folder
    # name ( pink )
        # comes from the BACKEND
        # connects with each parameter
    # name ( green )
        # comes from the set HTML ( display.html )
        # pulls info from using jinja


@app.route('/adv')
def adv():
    student_info = [
        { 'name' : 'Will', 'age' : 35},
        { 'name' : 'John', 'age' : 30},
        { 'name' : 'Mark', 'age' : 25},
        { 'name' : 'KB', 'age' : 27}
    ]
    return render_template('adv.html', students = student_info)
    # students = student_info
        # displays info from the backend
        # pass this into the RENDER_TEMPLATE
    # student_info ( pink )
        # comes from the BACKEND
        # connects with each parameter
    # students ( green )
        # comes from the set HTML
        # connects to the for loop
        # pulls info from using jinja


@app.route('/form')
def form():

    if 'username' not in session:
        name = 'This is a Default Value'
    else: 
        name = session['username']

    
    return render_template('forms.html', name = name)
    # @app.route('/form')
    # AND
    # @app.route('/form/submit', methods = ['POST'])
    # function together
    # RENDER then REDIRECT

@app.route('/form/submit', methods = ['POST'])
# methods = ['POST'] is REQUIRED for forms
def the_form():

    session['username'] = request.form['username']
    session['email'] = request.form['email']
    session['password'] = request.form['password']
    # request.form refers to our form info
        # should match name = '' field on html

    return redirect('/form')
    # here the info from the form is being processed
    # NEVER RENDER on a POST ROUTE
    # REDIRECT to the url the info is going
    # REDIRECT only wants a url


@app.route('/reset')
def reset():
    session.clear()
    # this clears session
    # 'logs out' current user
    return redirect('/form')
    #redirect to 'original / logout' route
