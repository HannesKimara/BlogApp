from flask import render_template, url_for
from flask_login import current_user, login_required

from . import main
from ..models import User, Blog, Comment

@main.route("/")
def index():
    return render_template("index.html")