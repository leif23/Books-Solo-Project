from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.book_m import Books
from flask_app.models.user_m import User

@app.route("/books")
def books(): 
    if "creator_id" not in session:
        return redirect("/")

    data = { 
        "id": session["creator_id"]
    }
    return render_template("books.html", users = User.get_user_by_id(data), all_books = Books.get_all() )

@app.route("/books", methods=["POST"])
def add_books(): 

    if not Books.book_validation(request.form):
        return redirect("/books")

    book_data = {
        "creator_id":request.form["creator_id"],
        "title":request.form["title"],
        "description":request.form["description"]
    }
    
    Books.save_books(book_data)
    
    return redirect("/books")

@app.route("/edit/<int:id>")
def edit(id): 

    if "creator_id" not in session:
        return redirect("/")

    book_data = {
        "id":id
    }
    return render_template("edit_and_favorites.html", book_edit = Books.get_book_by_id(book_data), nickNames = User.get_user_by_id({"id":session["creator_id"]}), fave_books = Books.get_fave_book_by_id({"id":session["creator_id"]}) )

@app.route("/edit", methods=["POST"])
def edit_books():

    if not Books.book_validation(request.form):
        return redirect(f"/edit/{request.form['id']}")
        
    data_books = { 
        "id":request.form["id"],
        "title":request.form["title"],
        "description":request.form["description"],
        "creator_id": request.form["creator_id"]
    }
    Books.edit_books(data_books)
    return redirect("/books")

@app.route("/view/<int:id>")
def view_book(id):
    data = {
        "id":id
    }
    return render_template("details.html", view = Books.get_book_by_id(data), nickNames = User.get_user_by_id({"id":session["creator_id"]}))

@app.route("/delete/<int:id>")
def delete_book(id):
    data ={ 
        "id":id
    }
    Books.destroy_books(data)
    return redirect("/books")

@app.route("/logOut")
def log_off():
    session.clear()
    return redirect("/")


    # todo favorite book table

@app.route("/favorites", methods=["POST"])
def add_fave():

    fave_data = {
        "user_id":request.form["user_id"],
        "book_id":request.form["book_id"]
    }
    Books.add_book(fave_data)
    return redirect("/books")

@app.route("/delete/favorite/<int:id>")
def destroy_favorites(id):
    data = { 
        "book_id":id,
        "user_id":session["creator_id"]
    }
    Books.delete_favorite(data)
    return redirect("/books")

