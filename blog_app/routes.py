from flask import render_template, url_for, flash, redirect
from blog_app import app
from blog_app.forms import RegistrationForm, LoginForm
from blog_app.models import User, Post

posts = [
    {'author': 'Hector Solis',
     'title': 'Blog Post 1',
     'content': 'First post content',
     'date_posted': 'May 5, 2021'},
     {'author': 'Hector Solis',
     'title': 'Blog Post 2',
     'content': 'Second post content',
     'date_posted': 'May 6, 2021'}
]


@app.route("/")
def home():
    return render_template('index.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)