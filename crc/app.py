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
    
@app.route("/multiply/<int:c>/<int:d>")
def multi(c:int, d:int):
    return f"The result of the multiplication is:{str(float(c*d)})"
