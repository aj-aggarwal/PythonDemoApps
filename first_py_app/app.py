from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "My First PY Web App"

@app.route("/<string:name>")
def hello(name):
	return f"<h1>Hello, {name}!</h1>"
