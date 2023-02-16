from flask import Flask
from markupsafe import escape
from flask import url_for


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f"Post {post_id}"


with app.test_request_context():
    print(url_for("hello_world"))
    print(url_for("hello_world", next="123"))
    print(url_for('hello', name='JohnDoe'))
