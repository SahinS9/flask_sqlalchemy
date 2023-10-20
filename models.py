from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from app import db



class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique = True)
    date_joined = db.Column(db.Date, default = datetime.utcnow)
    tasks =  db.relationship('Task', backref = 'user', cascade='save-update, delete-orphan' )


    def __repr__(self):
        return f"{self.name} with {self.email} at {self.date_joined} as {self.id}"


class Task(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        if self.user:
            return f"{self.user.name}'s task: {self.name}"
        else:
            return f"Task with no associated user: {self.name}"
