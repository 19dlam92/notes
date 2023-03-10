from flask_app.config.mysqlconnection import connectToMySQL
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')





class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # self.other_table = []
            # this is data from the other_table


# ==========================================================
# CREATE
# ==========================================================

    @classmethod
    def create_user(cls, data):
        query = '''
                INSERT INTO users 
                VALUES
                (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(confirm_password)s);
                '''
        results = connectToMySQL('users_schema').query.db(query, data)




# ==========================================================
# GET ALL
# ==========================================================

    @classmethod
    def get_all_users(cls):
        query = '''
                SELECT * FROM users;
                '''
        results = connectToMySQL('users_schema').query.db(query)
        all_users = []



# ==========================================================
# GET ONE
# ==========================================================

    @classmethod
    def get_one_user(cls, data):
        query = '''
                SELECT * FROM users
                WHERE id = %(user_id)s;
                '''
        results = connectToMySQL('users_schema').query.db(query, data)



# ==========================================================
# UPDATE
# ==========================================================

    @classmethod
    def update_user(cls, data):
        query = '''
                UPDATE users SET
                (first_name), (last_name), (email), (password), (confirm_password)
                WHERE
                (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(confirm_password)s)
                '''
        results = connectToMySQL('users_schema').query.db(query, data)




# ==========================================================
# DELETE
# ==========================================================

    @classmethod
    def delete_user(cls, data):
        query = '''
                DELETE FROM users
                WHERE id = %(id)s;
                '''
        results = connectToMySQL('users_schema').query.db(query, data)



# ==========================================================
# VALIDATION
# ==========================================================

    @staticmethod
    def validate_user():