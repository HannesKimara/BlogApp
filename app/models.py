from datetime import datetime

from werkzeug.security import generate_password_hash, check_password_hash

from . import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique = True)
    hash_pass = db.Column(db.String(255))
    blogs = db.relationship('Blog', backref = 'user', lazy = "dynamic")
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError("You cannot read password attribute")

    @password.setter
    def password(self, pass_entry):
        self.hash_pass = generate_password_hash(pass_entry)

    def verify_password(self, pass_entry):
        return check_password_hash(self.hash_pass, pass_entry)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    def __repr__(self):
        return f'User {self.username}::{self.id}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String())
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref = 'blog', lazy = "dynamic")

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    @classmethod
    def get_user_blogs(self, user_id):
        return Blog.query.filter_by(user_id = user_id).all()

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key= True)
    content = db.Column(db.String())
    blog_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id