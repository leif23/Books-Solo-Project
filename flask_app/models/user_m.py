from flask_app.config.mySQLconnect import connectToMySQL
from flask import flash
import re
email_regex = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
db_schema = "book_solo_project"
class User: 
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

        self.books = []

    @classmethod
    def save(cls, data):
        query ="""
            insert into users(first_name, last_name, email, password, created_at)
            values (%(first_name)s, %(last_name)s, %(email)s, %(password)s, now())
        """
        
        return connectToMySQL(db_schema).query_db(query,data)
    
    @staticmethod
    def validator(user_validate): 
        query = """

        select * from users where email = %(email)s;
        """
        result = connectToMySQL(db_schema).query_db(query, user_validate)
        
        isValid = True 
        if len(result) >=1: 
            isValid = False
            flash("Email Already existed", "reg")
        if len(user_validate["email"]) < 1: 
            flash("Email, must not be blank", "reg")
            isValid=False
        if len(user_validate["first_name"]) < 3 and len(user_validate["last_name"]) < 3:
            flash(" First and Last name must be atleast 3 characters", "reg")
            isValid = False
        if not email_regex.match(user_validate["email"]): 
            flash(" Email Doesn't match", "reg")
            isValid = False
        if len(user_validate["password"]) < 8: 
            flash("Password must be atleast 8 characters", "reg")
            isvalid = False
        if user_validate["password"] != user_validate["confirmPass"]:
            flash("Password Doesn't match ", "reg")
            isValid = True
        return isValid

    @classmethod 
    def get_email(cls, data):
        query = """
        select * from users where email = %(email)s;
        """
        result = connectToMySQL(db_schema).query_db(query, data)
        
        if len(result) < 1:
            return False
        return cls(result[0])

    @classmethod
    def get_user_by_id(cls, data):
        query = """
        select * from users where id = %(id)s;
        """
        result = connectToMySQL(db_schema).query_db(query, data)
        return cls(result[0])

    # @classmethod
    # def get_by_id(cls, data): 
    #     query = """
    #         select * from users where id = %(id)s;
    #     """
        
    #     return connectToMySQL(db_schema).query_db(query, data)