from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World! Abinaya P S Dept of AIML 7376222AL105"


if __name__ == "__main__":
    # Make sure to set host and port
    app.run(host='0.0.0.0', port=5000, debug=True)
