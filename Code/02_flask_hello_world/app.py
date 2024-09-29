from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World" + "Gokul Ramasubbiah" + "7376222AL132" + "Dept of AIML"

if __name__=='__main__':
    app.run()
