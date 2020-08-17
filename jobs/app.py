import Flask, render_template from flask

app = Flask(__name__)

@app.route("/")
def jobs():
    render_template("index.html")