from flask import Flask, request, render_template, redirect, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, world!</p>"

# @app.route("/<name>")
# def hello(name):
#     return f"Hello, {escape(name)}!"

@app.route("/projects/")
def project():
    return "The project page."

@app.route("/about")
def about():
    return "The about page."

@app.route("/methods", methods=['get', 'post'])
def method():
    if request.method == 'POST':
        return "POST\n"
    else:
        return "GET\n"

@app.route("/template/", methods=["get"])
@app.route("/template/<name>", methods=["get"])
def template_name(name=None):
    return render_template('hello.html', name=name)

@app.route("/request", methods=["get"])
def request_get():
    return render_template("request.html", value=request.args.get("value"))

@app.route("/request/post", methods=["get", "post"])
def request_post():
    if request.method == "POST":
        return redirect(url_for('request_get', value=request.form['value']))
    else:
        return redirect(url_for('request_get'))
