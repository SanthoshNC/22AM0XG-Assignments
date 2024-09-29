from flask import Flask 

app  = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! ' + 'Ashwin Karthik M ' + 'Dept of IT ' +'7376222IT113'

if __name__ == '__main__':
    app.run(debug=True)
