from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World! AKSHAYAN N - 7376222IT108, Dept of IT"

if __name__ == "__main__":
    app.run(debug=True)

