from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

#User Loader Method
@login.user_loader
def load_user(id):
  return User.query.get(int(id))


#------------USER MODEL------------
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(100), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(120))
  posts = db.relationship('Post', backref='author', lazy='dynamic')

  def __repr__(self):
        return '<User {}>'.format(self.username)

  #Set Password for user
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
  
  #Check Password Hash
  def check_password_hash(self, password):
    return check_password_hash(self.password_hash, password)

#------------POST MODEL------------
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(140))
    country = db.Column(db.String(140))
    description = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.description)