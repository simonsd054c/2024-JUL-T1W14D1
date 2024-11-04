from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hello world!!"

@app.route("/another_route")
def another_route():
    return "this is another route"

@app.route("/one_more_route")
def one_more_route():
    return "<h1>here you go!! One more route.</h1>"

products = [
    {
        "id": 0,
        "title": "Product 0",
        "price": 110
    },
    {
        "id": 1,
        "title": "Product 1",
        "price": 1500
    }
]

@app.route("/products")
def get_products():
    return products

@app.route("/can_vote")
def can_vote():
    age = int(request.args.get('age'))
    if age >= 18:
        return { "message": "You can vote" }
    else:
        return { "message": "You are a kid. Go away!!" }