from flask import Flask, render_template, redirect
from flask_migrate import Migrate
from .forms import SimpleForm
from .config import Config
from .models import db, SimplePerson


app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/simple-form")
def simple_form():
    form = SimpleForm()
    return render_template("simple_form.html", form=form)


@app.route("/simple-form", methods=["POST"])
def simple_form_post():
    form = SimpleForm()
    if form.validate_on_submit():
        person = SimplePerson()
        form.populate_obj(person)
        db.session.add(person)
        db.session.commit()
        return redirect("/")
    else:
        return "Bad Data"
