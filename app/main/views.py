from flask import render_template, url_for, redirect
from flask_login import current_user, login_required
import requests

from . import main
from .. import db
from ..models import User, Blog, Comment
from .forms import NewBlogForm, CommentForm
from ..email import mail_message

@main.route("/")
def index():
    all_blogs = Blog.query.order_by(db.desc(Blog.created_at)).limit(15).all()
    quote = requests.get('http://quotes.stormconsultancy.co.uk/random.json').json()['quote']
    print(quote)
    return render_template("index.html", blogs = all_blogs, quote = quote)

@main.route("/blog/new", methods = ['GET', 'POST'])
@login_required
def new_blog():
    form = NewBlogForm()
    if form.validate_on_submit():
        email_list = []
        new_blog = Blog(title = form.title.data, content = form.content.data, user = current_user)
        new_blog_id = new_blog.save()

        all_users = User.query.all()
        for user in all_users:
            email_list.append(user.email)

        mail_message("New blog notification","email/welcome_user",user.email, user=user)
        return redirect(url_for('main.blog_content', blog_id = new_blog_id))

    return render_template("new_blog.html", form = form)

@main.route("/blog/view/<blog_id>")
def blog_content(blog_id):
    curr_blog = Blog.query.filter_by(id = blog_id).first()

    return render_template('blog.html', blog = curr_blog)

@main.route("/blogs")
@login_required
def view_blogs():
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comment(content = form.content.data, user = current_user)
        new_comment.save()
        return redirect(url_for('main.blog_content', blog_id = new_blog_id))

    all_blogs = Blog.query.order_by(db.desc(Blog.created_at)).all()
    comments = Comment.query.filter_by(user_id = current_user.id).all()
    return render_template("blogs.html", blogs = all_blogs)