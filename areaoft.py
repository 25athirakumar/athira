from flask import Flask
app = Flask(__name__)

def areat(a):
    b=4
    t=0.5*a*b
    return [t]
@app.route('/aa/<int:a>')
def areat_route(a):
	
    return "The area of traingle is {}".format(areat(a))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
    
    
    
