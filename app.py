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

@app.route("/products/0")
def product_0():
    product0 = products[0]
    return product0

@app.route("/products/1")
def product_1():
    product1 = products[1]
    return product1

@app.route("/products/2")
def product_2():
    return {"message": "Product 2 does not exist"}, 404

@app.route("/products", methods=["POST"])
def create_product():
    # get product information from body of the request
    body_data = request.get_json()
    # print(body_data)
    products.append(body_data)
    return products

@app.route("/can_vote")
def can_vote():
    age = int(request.args.get('age'))
    if age >= 18:
        return { "message": "You can vote" }
    else:
        return { "message": "You are a kid. Go away!!" }