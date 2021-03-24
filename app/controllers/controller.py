from flask import render_template
from app import app
from app.models.order_list import orders

# @app.route('/')
# def index():
#     return 'Hello World'
#MVP
@app.route('/orders')
def index():
    return render_template('index.html', title="Home", orders=orders)
#Extensions
@app.route('/orders/<index>')
def show(index):
    return render_template('show.html', orders=orders[int(index)])