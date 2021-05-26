from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SelectField,TextAreaField
from wtforms.validators import InputRequired,Optional,Email
from wtforms.fields.html5 import DateField

class SignupForm(FlaskForm):
    """Form for """
    first = StringField("First Name",validators=[InputRequired()])
    last = StringField("Last Name",validators=[InputRequired()])
    username = StringField("Username",validators=[InputRequired()])
    password = PasswordField("Password",validators=[InputRequired()])
    email = StringField("Email",validators=[InputRequired(),Email()])
    native_language = StringField("Native Language",validators=[InputRequired()])
    second_language = StringField("Second Language",validators=[InputRequired()])

class SigninForm(FlaskForm):
    """Sign in Form"""
    username = StringField("Username",validators=[InputRequired()])
    password = PasswordField("Password",validators=[InputRequired()])


class Add_vol_form(FlaskForm):
    """Add Vocabulary Form"""
    vocabulary = StringField("Word",validators=[InputRequired()])
    category = StringField("Category",validators=[InputRequired()])
    definition_en = StringField("English Definition",validators=[InputRequired()])
    definition_ch = StringField("Chinese Definition",validators=[InputRequired()])
    part_of_speech = StringField("Part of Speech",validators=[InputRequired()])

class Search_reading_from(FlaskForm):
    """Add Search Reading Form"""
    category = SelectField("Reading For Category",choices=[
        ("business","Busines"),
        ("entertainment","Entertainment"),
        ("general","General"),
        ("science","Science"),
        ("sports","Sports"),
        ("technology","Technology")])

class Add_grammar_form(FlaskForm):
    """Add Grammar Form"""
    term = StringField("Grammer",validators=[InputRequired()])
    description = TextAreaField("Description",validators=[InputRequired()])
    example1 = StringField("Example1",validators=[InputRequired()])
    example2 = StringField("Example2")
    example3 = StringField("Example3")

class Check_spell_form(FlaskForm):
    """Check for Spelling Form"""
    spell = StringField("Word Spell As",validators=[InputRequired()])


class Translate_form(FlaskForm):
    """Get the translate form"""
    content = TextAreaField("Content to Translate:",validators=[InputRequired()])
    language = SelectField("Translate to:")

class Studyplan_form(FlaskForm):
    """Get Study Plan Field"""

    plan = TextAreaField("Plan",validators=[InputRequired()])
    repeat = SelectField("Repeat Method",choices=[("daily","Daily"),("weekly","Weekly"),("monthly","Monthly")],validators=[InputRequired()])
    start_date = DateField("Start From",validators=[InputRequired()])
    end_date = DateField("End At",validators=[InputRequired()])
