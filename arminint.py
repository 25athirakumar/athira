from flask import Flask
app = Flask(__name__)

def arm(num):
    list=[]
    for a in range(1,num):
        c=a
        b=0
        while a>0:
            arm=a%10
            b=b+arm**3
            a=int(a/10)
        if c==b:
            list.append(b)
    return(list)

@app.route('/arm/<int:num>')
def arm_route(num):
    return "The armstrong numbers are {}".format(arm(num))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0')