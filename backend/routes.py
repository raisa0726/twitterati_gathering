from unittest import result
from flask import current_app,jsonify,request
from flask_login import login_required, login_user, logout_user
from app import create_app,db
from models import Group, User_Group, User
from werkzeug.security import generate_password_hash, check_password_hash

read_group_id = 0
read_user_id = 0
now_group_id = 1
# Create an application instance
app = create_app()

# Define a route to fetch the avaialable articles
@login_manager.user_loader
def load_user(user_id):
  global read_user_id
  read_user_id = int(user_id)
  user_id = User.query.get(int(user_id))
  return jsonify(user_id)

@app.route("/")
def index():
  return jsonify()

@app.route("/user", methods=["GET"])
@login_required
def home():
	global read_user_id
	users = User.query.filter_by(user_id=read_user_id).all()
	groups = User_Group.query.filter_by(user_id=read_user_id).all()
	return jsonify(users, groups)

@app.route("/user/signup", methods=["GET", "POST"])
def signup():
  if request.method == "POST":
    user_name = request.form.get('user_name')
    user_password = request.form.get('user_password')
    user = User(user_name=user_name, user_password=generate_password_hash(user_password, method='sha256'))
    db.session.add(user)
    db.session.commit()
    return jsonify()
  else:
    return jsonify()

@app.route("/user/login", methods=["GET", "POST"])
def login():
  if request.method == "POST":
    user_id = int(request.form.get('user_id'))
    user_password = request.form.get('user_password')
    user = User.query.filter_by(user_id=user_id).first()
    if check_password_hash(user.user_password, user_password):
      login_user(user)
      return jsonify()
  else:
    return jsonify()

@app.route("/user/logout")
def logout():
  global read_user_id
  if read_user_id != 0:
    logout_user()
    read_user_id=0
  return jsonify()

@app.route("/user/create", methods=["GET", "POST"])
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
    return jsonify()
  else:
    return jsonify()

@app.route("/group/join", methods=["GET", "POST"])
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
      return jsonify()
  else:
    return jsonify()

@app.route("/group/edit/<int:group_id>", methods=["GET", "POST"])
@login_required
def edit(group_id):
  global read_user_id
  user_id = read_user_id
  group = Group.query.get(group_id)
  user_group = User_Group.query.filter_by(user_id=user_id,group_id=group_id)
  if request.method == "GET":
    return jsonify()
  elif request.method == "POST":
    group.group_name = request.form.get('group_name')
    group_password = request.form.get('group_password')
    user_group.group_name = request.form.get('group_name')
    user_group.group_password = request.form.get('new_group_password')
    if check_password_hash(group.group_password, group_password):
      group.group_password = generate_password_hash(request.form.get('new_group_password'), method='sha256')
      db.session.commit()
      print("更新")
    return jsonify()

@app.route("/group/delete/<int:group_id>", methods=["GET"])
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
  return jsonify()

@app.route("/about")
def about():
  return jsonify()

if __name__ == "__main__":
  app.run(debug=True)
