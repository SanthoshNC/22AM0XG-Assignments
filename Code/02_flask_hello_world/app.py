from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World" + "Gowtham bala k "+ "7376222AL135" + "Dept of AIML"

if __name__=='__main__':
    app.run()
