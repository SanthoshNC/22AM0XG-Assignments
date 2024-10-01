from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World" + "Raja T" + "7376222AD179" + "Dept of AIDS"

if __name__=='__main__':
    app.run()
