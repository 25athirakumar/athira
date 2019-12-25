from flask import Flask
app = Flask(__name__)

def arm(num):
    b=0
    c=num 
    while num>0:
        arm=num%10
        b=b+arm**3
        num=int(num/10)
    if b==c:
        return "is"
    else:
        return "is not"

@app.route('/arm/<int:num>')
def arm_route(num):
    return "The number {} an armstrong number".format(arm(num))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')