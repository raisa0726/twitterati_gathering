from app import db,ma
from datetime import datetime
from datetime import datetime
import pytz

# Group
class Groups(db.Model):
    group_id = db.Column(db.Integer, primary_key=True, nullable=False)
    group_name = db.Column(db.String(16), nullable=False, unique=False)
    group_password = db.Column(db.String(16), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

    def __repr__(self):
        return "<Groups %r>" % self.group_name

class GroupsShema(ma.Schema):
    class Meta:
        fields = ("group_id","group_name", "group_password", "created_at")

groups_schema = GroupsShema()
groups_schema = GroupsShema(many=True)

# User_group
class User_Group(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    group_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

    def __repr__(self):
        return "<User_Groups %r>" % self.id

class User_GroupsShema(ma.Schema):
    class Meta:
        fields = ("id"," user_id", "group_id", "created_at")

user_groups_schema = User_GroupsShema()
user_groups_schema = User_GroupsShema(many=True)

# User
class Users(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True, nullable=False)
    user_name = db.Column(db.String(16), nullable=False, unique=False)
    user_password = db.Column(db.String(16), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('Asia/Tokyo')))

    def __repr__(self):
        return "<Users %r>" % self.user_name

class UsersShema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ("user_id","user_name", "user_password", "created_at")

users_schema = UsersShema()
users_schema = UsersShema(many=True)
