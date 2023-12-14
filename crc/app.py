from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "bye code!"

@app.route("/hello")
def greating():
    return "hello you!"

@app.route("/sum/<int:a>/<int:b>")
def sum(a: int, b: int):
    result_sum = a + b
    return str(result_sum)
