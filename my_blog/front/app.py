from flask import Flask, request, render_template
from all_posts_views import all_posts_app

app = Flask(__name__)
app.register_blueprint(all_posts_app, url_prefix='/posts')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)
