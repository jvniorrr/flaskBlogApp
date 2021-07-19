from flask import render_template, url_for, flash, redirect
from flaskblogapp import app
from flaskblogapp.forms import RegistrationForm, LoginForm
from flaskblogapp.models import User, Post

posts = [
    {
        "author": "Junior Mendoza",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "July 17, 2021"
    },
    {
        "author": "Jane Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "July 18, 2021"
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form  = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for('home')) # name of the function is passed here. so referencing home.html, but the home function
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form  = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)