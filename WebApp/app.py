from flask import Flask
from flask import render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
import os

from datetime import datetime
import pytz

master_id = 0

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///accounts.db'
app.config['SECRET_KEY'] = os.urandom(24)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

class Family(db.Model):
  master_id = db.Column(db.Integer, nullable=False)
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(16), nullable=False, unique=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  master_name = db.Column(db.String(16), nullable=False, unique=False)
  password = db.Column(db.String(16), nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

@login_manager.user_loader
def load_user(user_id):
  global master_id
  master_id = int(user_id)+10000
  print(master_id)
  user_id = User.query.get(int(user_id))
  return user_id

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/home")
@login_required
def home():
  global master_id
  print(type(master_id))
  if master_id == 99999:
    families = Family.query.all()
    return render_template('home.html', families=families)
  if request.method == "GET":
    #print(master_id)
    families = Family.query.filter_by(master_id=master_id).all()
    #families = Family.query.all()
    print("OK")
    return render_template('home.html', families=families)

@app.route("/signup", methods=["GET", "POST"])
def signup():
  if request.method == "POST":
    master_name = request.form.get('master_name')
    password = request.form.get('password')
    user = User(master_name=master_name, password=generate_password_hash(password, method='sha256'))
    db.session.add(user)
    db.session.commit()
    return redirect('/login')
  else:
    return render_template('signup.html')

@app.route("/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    user_id = str(int(request.form.get('user_id'))-10000)
    password = request.form.get('password')
    user = User.query.filter_by(id=user_id).first()
    if check_password_hash(user.password, password):
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
    master_id = request.form.get('master_id')
    name = request.form.get('name')
    family = Family(master_id=master_id,name=name)
    db.session.add(family)
    db.session.commit()
    return redirect('/home')
  else:
    return render_template('create.html')

@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
  family = Family.query.get(id)
  if request.method == "GET":
    return render_template('edit.html', family=family)
  elif request.method == "POST":
    family.name = request.form.get('name')
    db.session.commit()
    return redirect('/home')

@app.route("/delete/<int:id>", methods=["GET"])
@login_required
def delete(id):
  family = Family.query.get(id)
  db.session.delete(family)
  db.session.commit()
  return redirect('/home')

@app.route("/about")
def about():
  return render_template('about.html')

if __name__ == "__main__":
  app.run(debug=True)