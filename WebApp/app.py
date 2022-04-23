from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import os

from datetime import datetime
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

read_group_id = 0
read_user_id = 0

class Group(db.Model):
  group_id = db.Column(db.Integer, primary_key=True, nullable=False)
  group_name = db.Column(db.String(16), nullable=False, unique=False)
  group_password = db.Column(db.String(16), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class User_Group(db.Model):
  user_id = db.Column(db.Integer, primary_key=True, nullable=False)
  group_id = db.Column(db.Integer, primary_key=True, nullable=False)
  user_name = db.Column(db.String(16), nullable=False, unique=False)
  group_name = db.Column(db.String(16), nullable=False, unique=False)
  user_password = db.Column(db.String(16), nullable=False)
  group_password = db.Column(db.String(16), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class User(UserMixin, db.Model):
  user_id = db.Column(db.Integer, primary_key=True, nullable=False)
  user_name = db.Column(db.String(16), nullable=False, unique=False)
  user_password = db.Column(db.String(16), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))


@login_manager.user_loader
def load_user(user_id):
  global read_user_id
  read_user_id = int(user_id)
  user_id = User.query.get(int(user_id))
  return user_id

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/home")
@login_required
def home():
  global read_user_id
  if request.method == "GET":
    users = User.query.filter_by(user_id=read_user_id).all()
    return render_template('home.html', users=users)

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if request.method == "POST":
    user_name = request.form.get('user_name')
    user_password = request.form.get('user_password')
    user = User(user_name=user_name, user_password=generate_password_hash(user_password, method='sha256'))
    db.session.add(user)
    db.session.commit()
    return redirect('/login')
  else:
    return render_template('signup.html')

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    user_id = int(request.form.get('user_id'))
    user_password = request.form.get('user_password')
    user = User.query.filter_by(user_id=user_id).first()
    if check_password_hash(user.user_password, user_password):
      login_user(user)
      return redirect('/home')
  else:
    return render_template('login.html')

@app.route("/logout")
def logout():
  global master_id
  if master_id != 0:
    logout_user()
    master_id=0
  return redirect('/')

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
  if request.method == "POST":
    user_id = int(request.form.get('user_id'))
    user_name = request.form.get('user_name')
    user_password = request.form.get('user_user_password')
    user = User.query.get(user_id=user_id)
    print(user)
    group_name = request.form.get('group_name')
    group_password = generate_password_hash(request.form.get('group_password'), metho='sha256')
    group = Group(group_name=group_name, group_password=group_password)
    #db.session.add(group)
    #db.session.commit()
    #group = Group.query.get(group_name=group_name, group_password=group_password)
    #print(group)
    #user_group = User_Group(user_id=user_id, group_id=group_name=group_name, group_password=group_password)
    return redirect('/home')
  else:
    return render_template('create.html')

@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
  Group = Group.query.get(id)
  if request.method == "GET":
    return render_template('edit.html', Group=Group)
  elif request.method == "POST":
    Group.name = request.form.get('name')
    db.session.commit()
    return redirect('/home')

@app.route("/delete/<int:id>", methods=["GET"])
@login_required
def delete(id):
  Group = Group.query.get(id)
  db.session.delete(Group)
  db.session.commit()
  return redirect('/home')

@app.route("/about")
def about():
  return render_template('about.html')

if __name__ == "__main__":
  app.run(debug=True)