from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import user
    # import User
        # pulls the class
    # import user
        # pulls the whole framework of the file



# ==========================================================
# CLASSES
# ==========================================================

# naming convention
    # file name
        # singular
    # match the database naming



# ==========================================================
# THIS CLASS IS JUST FOR NOTES
# ==========================================================

class Model:
    def __init__(self, data):
        # data of . . . . columns of database

        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['owner_id']
        # this is the foreign key
