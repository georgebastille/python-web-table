import os

from flask import Flask, render_template

# Set environment variables
os.environ["FLASK_ENV"] = "development"

app = Flask(__name__)


@app.route("/")
def landing():
    return render_template("greetings.html")


@app.route("/<query>")
def run_query(query):
    return render_template("greetings.html", name=query)


if __name__ == "__main__":
    app.run()
