from flask import Flask
from flask import url_for
from flask import request
from markupsafe import escape
import mysql.connector

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
    print("\n")
    print(url_for("hello_world"))
    print(url_for("hello_world", next="123"))
    print(url_for("hello", name="JohnDoe"))
    print(url_for("show_post", post_id=2))
    print(url_for("static", filename="style.css"))
    print("\n")

# HTTP METHED


@app.route("/test_http", methods=["GET", "POST"])
def test_http():
    if request.method == "POST":
        return "it is post"
    else:
        return "it is get"


@app.get("/test_get")
def test_get():
    return "it is just get"


@app.post("/test_post")
def test_post():
    return "it is just post"


# request object


# APIS with  JSON
@app.route("/me")
def me_api():
    return {
        "username": "ibepo",
        "theme": "right",
        "image": url_for("static", filename="lemons"),
    }


@app.rute("/users")
def users_api():
    users = ["kbe", "tmac", "james"]
    return users.to_json()


# db = mysql.connector.connect(host="139.196.77.225", user="root", passwd="111111")
db = mysql.connector.connect(host="localhost", user="root", passwd="111111")
mycursor = db.cursor()
mycursor.execute(("CREATE DATABASE test"))
