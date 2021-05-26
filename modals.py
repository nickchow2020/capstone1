from enum import unique
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from sqlalchemy.orm import backref

bcrypt = Bcrypt()

db = SQLAlchemy()

def connect_db(arr):
    db.app = arr
    db.init_app(arr)

class User(db.Model):
    """User Modal"""

    __tablename__ = "users"

    def __repr__(self):
        return f"username {self.username},and it's first name {self.first}"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    first = db.Column(db.Text,nullable=False)

    last = db.Column(db.Text,nullable=False)

    username = db.Column(db.Text,nullable=False,unique=True)

    password = db.Column(db.Text,nullable=False)

    email = db.Column(db.Text,nullable=False,unique=True)

    native_language = db.Column(db.Text,nullable=False)

    second_language = db.Column(db.Text,nullable=False)

    vocabularies = db.relationship("Vocabulary",order_by='desc(Vocabulary.id)',backref="user")

    grammars = db.relationship("Grammar",order_by='desc(Grammar.id)',backref="user")

    plans = db.relationship("Studyplan",order_by="desc(Studyplan.id)",backref="user")

    @classmethod
    def register(cls,first,last,username,password,email,native_language,second_language):
        encrypt_pass = bcrypt.generate_password_hash(password)
        utf_pass = encrypt_pass.decode("utf8")
        return cls( first=first,
                    last=last,
                    username=username,
                    password=utf_pass,
                    email=email,
                    native_language=native_language,
                    second_language=second_language)

    @classmethod
    def anthenticate(cls,username,password):
        curr_user = User.query.filter_by(username=username).first()
        if curr_user and bcrypt.check_password_hash(curr_user.password,password):
            return curr_user
        else:
            return False

class Vocabulary(db.Model):
    """Vocabularies"""

    __tablename__ = "vocabularies"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    vocabulary = db.Column(db.Text,nullable=False)

    category = db.Column(db.Text,nullable=False)

    definition_en = db.Column(db.Text,nullable=False)

    definition_ch = db.Column(db.Text,nullable=False)

    part_of_speech = db.Column(db.Text,nullable=False)

    familiarities = db.Column(db.Integer,nullable=False,default=1)

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


class Grammar(db.Model):
    """Grammer"""

    __tablename__ = "grammars"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    term = db.Column(db.Text,nullable=False)

    description = db.Column(db.Text,nullable=False)

    example1 = db.Column(db.Text,nullable=False)
    example2 = db.Column(db.Text)
    example3 = db.Column(db.Text)

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))


class Studyplan(db.Model):
    """Study Plan"""

    __tablename__ = "studyplans"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)

    plan = db.Column(db.Text,nullable=False)

    repeat = db.Column(db.Text,nullable=False)

    start_date = db.Column(db.Date,nullable=False) 

    end_date = db.Column(db.Date,nullable=False)

    is_complete = db.Column(db.Boolean,default=False)

    user_id = db.Column(db.Integer,db.ForeignKey("users.id"),nullable=False)
