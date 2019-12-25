from flask import Flask
app = Flask(__name__)

def big(a,b,c):
  if(a>b and a>c):
    return a
  elif(b>c and b>a):
    return b
  else:
    return c

@app.route('/')
def home():
  return "Open the URL and go to /big/a/b/c to see the website"

@app.route('/big/<int:a>/<int:b>/<int:c>')
def big_route(a,b,c):
  return "The biggest number is {}".format(big(a,b,c))

if __name__ == '__main__':
  app.run(host='0.0.0.0')