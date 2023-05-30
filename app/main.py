from flask import Flask, request, redirect, render_template

import data

TEXTFILE_NAME = "localdb.txt"  # for dev purposes only
HOST = "http://127.0.0.1:5000/"  # TODO: change this


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/favicon.ico")
def favicon():
    return "favicon"


@app.route("/<short_url>")
def redirect_to_long_url(short_url):
    d = data.get(TEXTFILE_NAME)
    long_url = d[short_url]
    if not long_url.startswith("http://") or not long_url.startswith("https://"):
        long_url = "http://" + long_url
    return redirect(long_url, code=301)


@app.get("/api/v1/pipsqueak")
def get():
    args = request.args
    short_url = args["url"]
    d = data.get(TEXTFILE_NAME)
    long_url = d[short_url]
    return long_url


@app.post("/api/v1/pipsqueak")
def shorten_url():
    args = request.args
    long_url = args["url"]
    short_url = data.generate_short_id()
    data.write(TEXTFILE_NAME, short_url, long_url)
    return HOST + short_url

