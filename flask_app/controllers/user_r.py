from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask import render_template, session, redirect, flash, request
from flask_app.models.user_m import User

@app.route("/")
@app.route("/register")
def Register():
    
    return render_template("register_and_login.html")

@app.route("/register", methods=["POST"])
def register_form(): 
    if not User.validator(request.form):
        return redirect("/")
        
    user_info = { 
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password":bcrypt.generate_password_hash(request.form["password"])    
        }
    creator_id = User.save(user_info)
    session["creator_id"] = creator_id
    return redirect("/")

@app.route("/login")
def logIn():
    
    return render_template("register_and_login.html")


@app.route("/login", methods=["POST"])
def logIn_form():
    # see user if its exist in data base
    user_login = { 
        "email": request.form["email"],
    }
    
    user_data = User.get_email(user_login)
    #if user is not registered
    if not user_data:
        flash("Invalid Email or password",'logIn')
        return redirect("/")

    if not bcrypt.check_password_hash(user_data.password,request.form["password"]):
        flash("Invalid Email or password",'logIn')
        return redirect("/")
        
    session["creator_id"] = user_data.id
    return redirect("/books")
    
