# ==========================================================
# DECORATORS
# ==========================================================

# Are identified by @
# Specified in the following methods



# ==========================================================
# CLASS METHODS
# ==========================================================

@classmethod
# HELPS IDENTIFIES the following code block
# ONLY applies the current code block
def class_method(cls):
    # CLS is ALWAYS passed in for @classmethod
        # it works like SELF
        # allows itself to catch info and refers the CLASS vs the individual INSTANCES



# ==========================================================
# STATIC METHODS
# ==========================================================

@staticmethod
# HELPS IDENTIFIES the following code block
# ONLY applies the current code block
def static_method( doesnt_need_info_to_be_passed_in, but_may_have_parameters ):
    # HELPS verify info
        # validation
        # 
        # 
    # NOT directly related to INSTANCE or CLASS



# ==========================================================
# APP.ROUTE
# ==========================================================

@app.route('/')
def home():
    return 'You are home!'



@app.route('/hello_world')
def hello_world():
    return 'Hello World!'



@app.route('/hello_world/<variable_info>/<variable_id>')
def hello_variable(variable_info, variable_id):
    # URL and FUNCTION PARAMETERS must match
    # VARIABLES in urls MUST be passed into the FUNCTION PARAMETER
    # print(variable_info)
    # print(variable_id)
    return f'Hello {variable_info} your id is {variable_id}'
    # HTTP response



@app.route('/<int:hello_world>')
# hello_world is TYPE CASTED
# by CASTING int: here type conversion in the function isn't needed
def hello_world(hello_world):
    newNum = hello_world * 5
    return f'Hello World {newNum}!'

