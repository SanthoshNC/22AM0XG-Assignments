from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, world " + "I'm Ramkumar (7376222IT231) " + "from Department of Information Technology."

if __name__ == "__main__":
    app.run(debug=True)