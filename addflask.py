from flask import Flask
app = Flask(__name__)

def add(a,b):
	return a+b
@app.route('/add/<int:a>/<int:b>')
def add_route(a,b):
	return "sum of two numbers is {}".format(add(a,b))
    
def sub(a,b):
	return a-b
@app.route('/sub/<int:a>/<int:b>')
def sub_route(a,b):
	return "sub of two numbers is {}".format(sub(a,b))


def mul(a,b):
	return a*b
@app.route('/mul/<int:a>/<int:b>')
def mul_route(a,b):
	return "mul of two numbers is {}".format(mul(a,b))
if __name__ == '__main__':
    app.run(host='0.0.0.0')