import os
from operator import methodcaller
from flask import Flask,render_template,redirect,session,flash,request
from flask_debugtoolbar import DebugToolbarExtension, _printable
from flask_wtf import form
from sqlalchemy.sql.operators import contains_op
from forms import SignupForm,SigninForm,Add_vol_form,Search_reading_from,Add_grammar_form,Check_spell_form,Translate_form,Studyplan_form
from modals import db,connect_db,User,Vocabulary,Grammar,Studyplan
from helper import language_tuple_list,get_reading_material,languages,translateEnTo,getEnglishDef,getChineseDef,translate_url

app = Flask(__name__)
app.debug = True

connect_db(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL','postgresql:///gogo_app_db')
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY","MY_SECRET_KEY_10_20")

toolbar = DebugToolbarExtension(app)


@app.route("/")
def hello_world():
    if "user_id" in session:
        return redirect("/home")
    return render_template("home.html")


@app.route("/home")
def home():
    if "user_id" not in session:
        flash("Please login first","warning")
        return redirect("/login")

    user = User.query.get_or_404(session["user_id"])
    return render_template("home.html",user=user)


@app.route("/signup",methods=["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        new_user = User.register(first=form.first.data,
                                last=form.last.data,
                                username=form.username.data,
                                password=form.password.data,
                                email=form.email.data,
                                native_language=form.native_language.data,
                                second_language=form.second_language.data)
        db.session.add(new_user)
        db.session.commit()
        session["user_id"] = new_user.id
        flash(f"welcome {new_user.first}","success")
        return redirect("/home")
    return render_template("signup.html",form=form)


@app.route("/login",methods=["GET","POST"])
def login():
    form = SigninForm()
    if form.validate_on_submit():
        auth_user = User.anthenticate(
            form.username.data,
            form.password.data)

        if auth_user:
            session["user_id"] = auth_user.id
            flash(f"Welcome {auth_user.first}","success")
            return redirect("/home")
        else:
            form.username.errors = ["user not found! please try other one"]
    return render_template("login.html",form=form)


@app.route("/user/profile/<int:id>")
def show_user_profile(id):
    if "user_id" not in session:
        return redirect("/home")

    curr_user = User.query.get_or_404(id)

    return render_template("profile.html",user=curr_user)


@app.route("/vocabulary",methods=["GET","POST"])
def vocabulary():
    if "user_id" not in session:
        return redirect("/login")

    user = User.query.get_or_404(session["user_id"])
    vocabulary = user.vocabularies
    focus = True
    return render_template("vocabulary.html",user=user,focus=focus,vocabulary=vocabulary)

@app.route("/vocabulary/<int:id>",methods=["GET","POST"])
def edit_vol(id):
    if "user_id" not in session:
        return redirect("/login")

    user = User.query.get_or_404(session["user_id"])

    target_vol = Vocabulary.query.get_or_404(id)
    form = Add_vol_form(obj=target_vol)

    if form.validate_on_submit():
        target_vol.vocabulary = form.vocabulary.data
        target_vol.category = form.category.data
        target_vol.definition_en = form.definition_en.data
        target_vol.definition_ch = form.definition_ch.data
        target_vol.part_of_speech = form.part_of_speech.data
        db.session.commit()
        return redirect("/vocabulary")

    return render_template("edit_vol.html",form=form,user=user,vol=target_vol)

@app.route("/add_vol",methods=["POST","GET"])
def add_vol():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":
        vol = request.form["vocab"]
        return redirect(f"/add_vol/{vol}")

    user = User.query.get_or_404(session["user_id"])
    return render_template("add_vol_form.html",user=user)


@app.route("/add_vol/<vol>",methods=["POST","GET"])
def add_vol_database(vol):

    if "user_id" not in session:
        return redirect("/login")

    eng_def = getEnglishDef(vol)
    ch_def = getChineseDef(vol,translate_url)

    default_obj = {
        "vocabulary":vol,
        "definition_en":eng_def["definition"],
        "definition_ch": ch_def,
        "part_of_speech":eng_def["partOfSpeech"]
    }

    user = User.query.get_or_404(session["user_id"])
    form = Add_vol_form()
    if form.validate_on_submit():
        new_word = Vocabulary(
            vocabulary=form.vocabulary.data,
            category=form.category.data,
            definition_en=form.definition_en.data,
            definition_ch=form.definition_ch.data,
            part_of_speech=form.part_of_speech.data,
            user_id = session["user_id"]
            )

        db.session.add(new_word)
        db.session.commit()
        return redirect("/add_vol")

    return render_template("save_vol_form.html",form=form,user=user,obj=default_obj)

@app.route("/vocabulary/delete/<int:id>")
def delete_vol(id):
    Vocabulary.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect("/vocabulary")


@app.route("/reading",methods=["POST","GET"])
def reading():
    if "user_id" not in session:
        return redirect("/login")
    form = Search_reading_from()
    data = get_reading_material("en")
    user = User.query.get_or_404(session["user_id"])
    focus = True

    if form.validate_on_submit():
        search = form.category.data
        data = get_reading_material("en",search)
        return render_template("reading.html",user=user,focus=focus,reads=data,form=form)
        
    return render_template("reading.html",user=user,focus=focus,reads=data,form=form)


@app.route("/grammar")
def grammar():
    if "user_id" not in session:
        return redirect("/login")

    user = User.query.get_or_404(session["user_id"])
    grammars = user.grammars
    focus = True
    return render_template("grammar.html",user=user,focus=focus,grammars=grammars)


@app.route("/grammar/add",methods=["GET","POST"])
def add_grammar():
    if "user_id" not in session:
        return redirect("/login")

    user_id = session["user_id"]
    form = Add_grammar_form()
    user = User.query.get_or_404(user_id)

    if form.validate_on_submit():
        new_grammar = Grammar(
            term=form.term.data,
            description=form.description.data,
            example1=form.example1.data,
            example2=form.example2.data,
            example3=form.example3.data,
            user_id = user_id)

        db.session.add(new_grammar)
        db.session.commit()
        return redirect("/grammar")
    
    return render_template("add_grammar.html",user=user,form=form)

@app.route("/grammar/<int:id>",methods=["POST","GET"])
def edit_grammar(id):
    target_grammar = Grammar.query.get_or_404(id)
    form = Add_grammar_form(obj=target_grammar)

    user = User.query.get_or_404(session["user_id"])

    if form.validate_on_submit():
        target_grammar.term = form.term.data
        target_grammar.description = form.description.data
        target_grammar.example1 = form.example1.data
        target_grammar.example2 = form.example2.data
        target_grammar.example3 = form.example3.data
        
        db.session.commit()
        return redirect("/grammar")

    return render_template("edit_grammar.html",user=user,form=form,grammar=target_grammar)

@app.route("/grammar/delete/<int:id>")
def delete_grammar(id):
    Grammar.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect("/grammar")

@app.route("/review",methods=["GET","POST"])
def review():
    if "user_id" not in session:
        return redirect("/login")

    user = User.query.get_or_404(session["user_id"])
    focus = True
    if request.method == 'POST' and request.form:
        vol_ids = ",".join([id for id in request.form])
        return redirect(f"/review/card/{vol_ids}")

    return render_template("review.html",user=user,focus=focus)


@app.route("/review/card/<ls>")
def practice_vol(ls):
    if "user_id" not in session:
        return redirect("/login")

    vol_ids = list(ls.split(","))
    vocabs = [Vocabulary.query.get(id) for id in vol_ids]
    user = User.query.get_or_404(session["user_id"])

    return render_template("practice.html",user=user,vocabs=vocabs,review_list=ls)


@app.route("/review/dictionary/<int:id>/<review_list>",methods=["POST","GET"])
def review_spell(id,review_list):
    if "user_id" not in session:
        return redirect("/login")
    
    vol = Vocabulary.query.get_or_404(id)

    user = User.query.get_or_404(session["user_id"])
    form=Check_spell_form()

    if form.validate_on_submit():
        result = False
        if form.spell.data == vol.vocabulary:
            result = True
            return render_template("check_spell.html",user=user,form=form,vol=vol,review_list=review_list,result=result)

        return render_template("check_spell.html",user=user,form=form,vol=vol,review_list=review_list,result=result)

    return render_template("check_spell.html",user=user,form=form,vol=vol,review_list=review_list)


@app.route("/translate",methods=["GET","POST"])
def translate():
    if "user_id" not in session:
        return redirect("/login")

    user = User.query.get_or_404(session["user_id"])
    focus = True

    form = Translate_form()

    _languages = language_tuple_list(languages)

    form.language.choices = _languages

    if form.validate_on_submit():
        content = form.content.data
        language = form.language.data
        result = translateEnTo(content,language,translate_url)
        return render_template("translate.html",user=user,focus=focus,form=form,result=result)
    return render_template("translate.html",user=user,focus=focus,form=form)


@app.route("/studyplan")
def studyplan():
    if "user_id" not in session:
        return redirect("/login")

    user = User.query.get_or_404(session["user_id"])
    focus = True
    return render_template("studyplan.html",user=user,focus=focus)


@app.route("/studyplan/add",methods=["POST","GET"])
def add_study_plan():
    if "user_id" not in session:
        return redirect("/login")

    form = Studyplan_form()
    user = User.query.get_or_404(session["user_id"])

    if form.validate_on_submit():
        new_plan = Studyplan(
            plan=form.plan.data,
            repeat=form.repeat.data,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            user_id=session["user_id"])
        db.session.add(new_plan)
        db.session.commit()
        return redirect("/studyplan")
    return render_template("add_plan_form.html",user=user,form=form)


@app.route("/studyplan/statusupdate/<int:id>",methods=["POST"])
def add_studyplan(id):
    if "user_id" not in session:
        return redirect("/login")    

    user = User.query.get_or_404(session["user_id"])

    target_plan = Studyplan.query.get_or_404(id)

    if  not target_plan.is_complete:
        target_plan.is_complete = True
    else:
        target_plan.is_complete = False

    db.session.commit()
    return redirect("/studyplan")

@app.route("/plan/update/<int:id>",methods=["POST","GET"])
def update_plan(id):
    if "user_id" not in session:
        return redirect("/login")

    user = User.query.get_or_404(session["user_id"])

    curr_plan = Studyplan.query.get_or_404(id)
    form = Studyplan_form(obj=curr_plan)

    if form.validate_on_submit():
        curr_plan.plan = form.plan.data
        curr_plan.repeat = form.repeat.data
        curr_plan.start_date = form.start_date.data
        curr_plan.end_date = form.end_date.data
        db.session.commit()
        return redirect("/studyplan")

    return render_template("update_plan.html",user=user,form=form)

@app.route("/plan/delete/<int:id>")
def delete_plan(id):
    if "user_id" not in session:
        return redirect("/login")

    Studyplan.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect("/studyplan")

@app.route("/signout")
def signout():
    session.pop("user_id")
    return redirect("/")

