from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


# ==========================================================
# VALIDATION
# ==========================================================



class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



# ==========================================================
# CREATE
# ==========================================================

    @classmethod
    def create_user(cls, data):
        query = '''
                INSERT INTO table 

                '''





# ==========================================================
# GET ALL
# ==========================================================

    @classmethod
    def get_all_users(cls):
        query = '''
                SELECT * FROM users

                '''
        results = connectToMySQL('users_schema').query.db(query)
        all_users = []



# ==========================================================
# GET ONE
# ==========================================================

    @classmethod
    def get_one_user(cls):
        query = '''
                SELECT * FROM users WHERE id = %(user_id)s;
                '''
        results = connectToMySQL('users_schema').query.db(query, data)



# ==========================================================
# UPDATE
# ==========================================================

    @classmethod
    def update_user(cls):
        query = '''
                UPDATE users SET

                '''
        




# ==========================================================
# DELETE
# ==========================================================

    @classmethod
    def delete_user(cls):
        query = '''
                DELETE FROM users
                WHERE $(id)s;
                '''

