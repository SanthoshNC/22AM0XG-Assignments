from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! ' + 'Gowtham Prasath K ' + '7376222IT144'

if __name__ == '__main__':
    app.run(debug=True)
