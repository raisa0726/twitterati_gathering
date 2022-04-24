from flask import Flask, jsonify
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
now_group_id = 1
class Group(db.Model):
  group_id = db.Column(db.Integer, primary_key=True, nullable=False)
  group_name = db.Column(db.String(16), nullable=False, unique=False)
  group_password = db.Column(db.String(16), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class User_Group(db.Model):
  id = db.Column(db.Integer, primary_key=True, nullable=False)
  user_id = db.Column(db.Integer, nullable=False)
  group_id = db.Column(db.Integer, nullable=False)
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

@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
  global read_user_id
  if request.method == "GET":
    users = User.query.filter_by(user_id=read_user_id).all()
    user_groups = User_Group.query.filter_by(user_id=read_user_id).all()
    user_key = ["user_id","user_name"]
    user_value = []
    for user in users:
      user_value.append(user.user_id)
      user_value.append(user.user_name)
    user_data = dict(zip(user_key,user_value))
    return render_template('home.html',users=users, groups=user_groups)

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
      print("OK")
      return redirect('/home')
  else:
    return render_template('login.html')

@app.route("/logout")
def logout():
  global read_user_id
  if read_user_id != 0:
    logout_user()
    read_user_id=0
  return redirect('/')

@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
  global now_group_id
  if request.method == "POST":
    user_id = int(request.form.get('user_id'))
    user_name = request.form.get('user_name')
    user_password = request.form.get('user_password')
    #user = db.session.query(User).filter(User.user_name==user_name and User.user_password==user_password).all()
    #print(user)
    #now_group_id += 1
    group_id = len(db.session.query(Group).all())+now_group_id
    group_name = request.form.get('group_name')
    group_password = generate_password_hash(request.form.get('group_password'), method='sha256')
    group = Group(group_id=group_id, group_name=group_name, group_password=group_password)
    db.session.add(group)
    db.session.commit()
    group = db.session.query(Group).filter(group_name==group_name and group_password==group_password).all()
    user_group = User_Group(user_id=user_id, group_id=group_id, user_name=user_name, group_name=group_name, user_password=user_password, group_password=group_password)
    db.session.add(user_group)
    db.session.commit()
    return redirect('/home')
  else:
    return render_template('create.html')

@app.route("/join", methods=["GET", "POST"])
@login_required
def join():
  if request.method == "POST":
    user_id = int(request.form.get('user_id'))
    user_name = request.form.get('user_name')
    user_password = request.form.get('user_password')
    group_id = int(request.form.get('group_id'))
    group_name = request.form.get('group_name')
    group_password = request.form.get('group_password')
    group = Group.query.filter_by(group_id=group_id).first()
    if check_password_hash(group.group_password, group_password):
      group_password = generate_password_hash(request.form.get('group_password'), method='sha256')
      user_group = User_Group(user_id=user_id, group_id=group_id, user_name=user_name, group_name=group_name, user_password=user_password, group_password=group_password)
      db.session.add(user_group)
      db.session.commit()
      return redirect('/home')
  else:
    return render_template('join.html')

@app.route("/edit/<int:group_id>", methods=["GET", "POST"])
@login_required
def edit(group_id):
  global read_user_id
  user_id = read_user_id
  group = Group.query.get(group_id)
  user_group = User_Group.query.filter_by(user_id=user_id,group_id=group_id)
  if request.method == "GET":
    return render_template('edit.html', group=group)
  elif request.method == "POST":
    group.group_name = request.form.get('group_name')
    group_password = request.form.get('group_password')
    user_group.group_name = request.form.get('group_name')
    user_group.group_password = request.form.get('new_group_password')
    if check_password_hash(group.group_password, group_password):
      group.group_password = generate_password_hash(request.form.get('new_group_password'), method='sha256')
      db.session.commit()
      print("更新")
    return redirect('/home')

@app.route("/delete/<int:group_id>", methods=["GET"])
@login_required
def delete(group_id):
  global now_group_id
  group = Group.query.get(group_id)
  user_group = User_Group.query.get(group_id)
  user_group = db.session.query(User_Group).filter(User_Group.group_id==group_id).all()
  db.session.delete(group)
  for i in range(len(user_group)):
    db.session.delete(user_group[i])
  db.session.commit()
  now_group_id += 1
  return redirect('/home')

@app.route("/about")
def about():
  return render_template('about.html')

if __name__ == "__main__":

  app.run(debug=True)
