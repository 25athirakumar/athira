from flask import Flask
app = Flask(__name__)
@app.route('/sqrt/<int:num>')
def f(num):
  # No conversion of x needed.
  return str(num**0.5)
if __name__ == '__main__':
    app.run(host='0.0.0.0')