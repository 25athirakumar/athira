from flask import Flask

app = Flask(__name__)

@app.route('/aaa')
def hello():
    return 'Hello, World!'