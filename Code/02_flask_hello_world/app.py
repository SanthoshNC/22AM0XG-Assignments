from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! ' + 'Sudhan ' + '7376222AL210'

if __name__ == '__main__':
    app.run(debug=True)
