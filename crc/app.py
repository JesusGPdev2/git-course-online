from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "bye code!"

@app.route("/hello")
def greating():
    return "hello you!"
# http://localhost:4000/sum/100/153
@app.route("/sum/<int:a>/<int:b>")
def sum(a: int, b: int):
    result_sum = a + b
    return str(result_sum)

#http://localhost:4000/multiply/20.4/15.3
@app.route("/multiply/<float:c>/<float:d>")
def multi(c:int, d:int):
    result_mult = c*d
    return f"The result of the multiplication is: {str(float(result_mult))}"
