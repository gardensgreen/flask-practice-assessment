from flask import Flask, render_template
from .forms import SimpleForm
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def main_page():
    return render_template("main_page.html")


@app.route("/simple-form")
def simple_form():
    form = SimpleForm()
    return render_template("simple_form.html", form=form)
