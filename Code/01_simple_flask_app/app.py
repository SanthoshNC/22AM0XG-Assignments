from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, IMRAN! ' + 'IMRAN J' + ' 7376222AL143' + ' DEPT of AI&ML'

if __name__ == '__main__':
    app.run(debug = True)
