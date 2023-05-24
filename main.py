from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.get("/api/v1/pipsqueak")
def get():
    args = request.args
    return "GET"


@app.post("/api/v1/pipsqueak")
def shorten():
    args = request.args
    return "POST"
