from flask import Flask
app = Flask(__name__)

def add(a,b):
	return a+b
@app.route('/add/<int:a>/<int:b>')
def add_route(a,b):
	return "sum of two numbers is {}".format(add(a,b))