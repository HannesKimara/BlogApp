from flask import render_template, url_for, redirect
from flask_login import current_user, login_required

from . import main
from .. import db
from ..models import User, Blog, Comment
from .forms import NewBlogForm

@main.route("/")
def index():
    all_blogs = Blog.query.order_by(db.desc(Blog.created_at)).limit(15).all()
    return render_template("index.html", blogs = all_blogs)

@main.route("/blog/new", methods = ['GET', 'POST'])
@login_required
def new_blog():
    form = NewBlogForm()
    if form.validate_on_submit():
        new_blog = Blog(title = form.title.data, content = form.content.data, user = current_user)
        new_blog_id = new_blog.save()
        return redirect(url_for('main.blog_content', blog_id = new_blog_id))

    return render_template("new_blog.html", form = form)

@main.route("/blog/view/<blog_id>")
def blog_content(blog_id):
    curr_blog = Blog.query.filter_by(id = blog_id).first()

    return render_template('blog.html', blog = curr_blog)

@main.route("/blogs")
def view_blogs():
     all_blogs = Blog.query.order_by(db.desc(Blog.created_at)).all()

     return render_template("blogs.html", blogs = all_blogs)