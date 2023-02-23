// ====================================================
// TERMINAL COMMANDS
// ====================================================

> pipenv install flask flask-bcrypt pymysql
> pip list
    this shows your current imports
> pipenv shell
    create the environment
> pip install --upgrade pip
    if there are any necessary updates

**WHEN** the pip / pipen cmd isnt working
    try **python -m pip / pipenv** instead
> python server.py
    starts / restarts your server


// ====================================================
// PYTHON ERRORS
// ====================================================

# KeyErrors

> the "" isnt defined
> somewhere in the code "" isnt being called
> check spelling / syntax

# pymysql.err

> check your queries & code that calls the queries
> check the physical query that you're trying to access
> look for **: s , _ . ( spacing )**
> check if you're calling the **correct schema**
    > verify all instances of the **schema** are the same
> **UnknownColumn** refer to the foreign key

# tuples

> refers to your query
> tuple out of range
> check your parsing
> check if you're accessing the correct class
    > mix match of info can cause errors too

# Method Not Allowed

> check HOW the info is being passed
> <form> action = "" <---
> REQUIRES the **<input> submit button** - throws errors otherwise
    > render_template("asdf.html")
    > "asdf.html" - action = "/(to the new page **WHENN** info is passed)"
    > redirect("/(to the next url)")

# Not Found

> url hasn't been established

# Jinja2

> verify jinja syntax
> are you referencing the correct variable?
> HTML = {{ }}
> controllers = < >

# IndexError

https://thecleverprogrammer.com/2021/01/04/how-to-fix-bugs-in-python/


// ====================================================
// UTILIZING JINJA
// ====================================================

> @app.route("/<name>")
> def route(name):
    > return render_template("index.html", name = name)

> when using **name = name** it catches information for jinja to register in the html
> when using <> within the **@app.route** it MUST match in **def route():**
    > therefore . . . .
        > @app.route("/<name>")
        > def route(name):
        > in the HTML = {{ name }}