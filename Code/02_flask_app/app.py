from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello,world!' + 'KANITHA A' + '7376222AL151' + 'Department of AIML'

if __name__ == '__main__':
    app.run(debug=True)cd "C:\One Credit\01_flask_app"
