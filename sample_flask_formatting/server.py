from flask_app import app
from flask_app.controllers import controllers, users
# ONLY import controllers once its been made
    # it'll crash the server





if __name__ == '__main__':
    app.run(debug = True)
# This triggers our app to run