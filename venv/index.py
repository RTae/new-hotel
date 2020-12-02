from flask import Flask, jsonify
from flask_cors import CORS
from src import Customer as C

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Home Page Route'


@app.route('/about')
def about():
    return 'About Page Route'


@app.route('/portfolio')
def portfolio():
    return 'Portfolio Page Route'


@app.route('/contact')
def contact():
    return 'Contact Page Route'

@app.route('/customer')
def x():
    Customer = C.Customer()
    return jsonify(Customer.getAllCustomer())