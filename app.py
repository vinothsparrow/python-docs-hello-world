from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "PoC by Vinoth Kumar (<a href=https://hackerone.com/vinothkumar>https://hackerone.com/vinothkumar</a>)"
