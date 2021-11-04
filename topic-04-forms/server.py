from bottle import run, template, default_app
from bottle import get, post
from bottle import request
from bottle import debug 

# http://localhost:8068/.... <get>

@get("/")
def get_index():
    return ("home page!")

@get("/hello")
@get("/hello/<name>")
def get_hello(name="world"):
    return template("hello", name="Bob", extra=None)


@get("/greet")
@get("/greet/<name>")
def get_greet(name="world"):
    return template('hello', name="Bob", extra="Happy Birthday")

@get("/greeting/<names>")
def get_greetings(names):
    names = names.split(',')
    return template('greetings', names=names)

@get("/login")
def get_login():
    return template("login", message="")


@post("/login")
def post_login():
    username = request.forms['username']
    password = request.forms['password']
    if password != "magic":
        return template('login', message="Bad password")

    return template("hello", name=username + "!!!!", extra="Happy Birthday")

debug(True)

run(host="localhost", port=8068, reloader=True)