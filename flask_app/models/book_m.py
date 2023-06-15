from flask_app.config.mySQLconnect import connectToMySQL
from flask import flash

from flask_app.models import user_m

db_schema = "book_solo_project"
class Books: 
    def __init__(self, data):
        self.id = data["id"]
        self.creator_id = data["creator_id"]
        self.title = data["title"]
        self.description = data["description"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.creator = None

    @classmethod
    def get_all(cls): 
        query = """
        
            select * from users join books on users.id = books.creator_id;

        """
        result = connectToMySQL(db_schema).query_db(query)
        print(result)
        
        all_books = [] 
        for row in result:
            
            one_user = user_m.User({
                "id":row["id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "email":row["email"],
                "password":" ",
                "created_at":row["created_at"],
                "updated_at":row["updated_at"],
            })
            user_book = Books({
                "id":row["books.id"],
                "title":row["title"],
                "description":row["description"],
                "created_at":row["books.created_at"],
                "updated_at":row["books.updated_at"],
                "creator_id":row["creator_id"]
            })
            user_book.creator = one_user
            all_books.append(user_book)
        print(all_books)
        return all_books
            
        
        
    @classmethod
    def save_books(cls, data): 
        query = """
            insert into books (creator_id ,title, description, created_at) values (%(creator_id)s, %(title)s, %(description)s, now())
        """
        print("---F---")
        result = connectToMySQL(db_schema).query_db(query, data)
        print(result)
        return result


    @staticmethod
    def book_validation(validate_books):
        isValid = True

        if len(validate_books["title"]) < 5 or len(validate_books["description"]) < 5:
            flash("Title and Description must be atleast 5 characters", "books")
            isValid =False 
        return isValid 


    @classmethod
    def get_book_by_id(cls, data):
        query = """ 
            select * from books left join users on users.id = books.creator_id where books.id = %(id)s;
        """
        result = connectToMySQL(db_schema).query_db(query, data)


        # checking if the user has a book and will return 1, but if not return 0
        if not result:
            return False
        result = result[0]
        #making an instance with users
        one_books = cls(result)
        one_user = user_m.User({
            "id":result["users.id"],
            "first_name":result["first_name"],
            "last_name":result["last_name"],
            "email":result["email"],
            "password":" ",
            "created_at":result["created_at"],
            "updated_at":result["updated_at"],
        })
        one_books.creator = one_user
        return one_books

        # todo edit
    @classmethod
    def edit_books(cls, data):
        query = """
            update books set title = %(title)s, description = %(description)s, updated_at = now() where books.id = %(id)s
        """

        result = connectToMySQL(db_schema).query_db(query, data)
        print(result)
        return result


        #todo delete 
    @classmethod
    def destroy_books(cls, data):
        query = """
            delete from books where id =%(id)s;
        """
        result = connectToMySQL(db_schema).query_db(query, data)
        return result


    # todo favorites table

    @classmethod
    def add_book(cls, data):
        query="""
            insert into favorite_books (user_id, book_id) values ( %(user_id)s, %(book_id)s);
        """
        result = connectToMySQL(db_schema).query_db(query, data)
        return result 


    @classmethod
    def get_fave_book_by_id(cls, data):
        query = """
            select * from books left join favorite_books on books.id = book_id
            left join users on users.id = favorite_books.user_id where users.id = %(id)s;
        """
        result = connectToMySQL(db_schema).query_db(query, data)
        print(result)
        if not result:
            return False
        res = result[0]
        print(res)
        temp = { 
            "id":res["user_id"],
            "first_name":res["first_name"],
            "last_name":res["last_name"],
            "email":res["email"],
            "password":res["password"],
            "created_at":res["users.created_at"],
            "updated_at":res["users.updated_at"]
        }
        
        user = user_m.User(temp)
        for row_db in result:
            user.books.append(cls(row_db))

        return user

    # @classmethod
    # def un_favorite(cls, data):
    #     query = """
    #         select * from books where books.id not in (select user_id from favorite_books where books.id = %(id)s);
    #     """
    #     result = connectToMySQL(db_schema).query_db(query, data)
    #     unFave_book = [] 
    #     for unFave in result:
    #         unFave_book.append(unFave)
    #     return unFave_book
    
    @classmethod
    def delete_favorite(cls, data):
        query = """
            delete from favorite_books where user_id = %(user_id)s AND book_id = %(book_id)s;
        """
        result = connectToMySQL(db_schema).query_db(query, data)
        return result




    





        

