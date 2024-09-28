from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! ' + 'Pawan G' + '7376222AL180' + 'Dept of AIML'

if __name__=='__main__':
    app.run(debug=True)