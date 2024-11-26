from sqlalchemy.sql import func
from src import db


class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  first_name = db.Column(db.String(128), nullable=False)
  last_name = db.Column(db.String(128), nullable=False)
  user_name = db.Column(db.String(128), nullable=False)
  email = db.Column(db.String(128), nullable=False)
  active = db.Column(db.Boolean(), default=True, nullable=False)
  date_created = db.Column(db.DateTime, default=func.now(), nullable=False)
  date_updated = db.Column(db.DateTime, default=func.now())

  def __init__(self, first_name, last_name, user_name, email):
    self.first_name = first_name
    self.last_name = last_name
    self.user_name = user_name
    self.email = email
