from flask import Blueprint, render_template, url_for
from models import get_all_posts

all_posts_app = Blueprint('all_posts_app', __name__)


@all_posts_app.route('/')
def posts_list():
    posts = get_all_posts()
    return render_template('all_posts.html', posts=posts)


@all_posts_app.route('/<int:id>/', endpoint='')
def posts_list(id):
    return render_template('post.html')
