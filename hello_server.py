import os

import pandas as pd
from flask import Flask, render_template

# Set environment variables
os.environ["FLASK_ENV"] = "development"

app = Flask(__name__)


@app.route("/")
def landing():
    return render_template("greetings.html")


@app.route("/<query>")
def run_query(query):
    df = pd.read_csv("./data/Repossession-2019-07.csv").to_dict("records")
    return render_template("greetings.html", name=query, dataframe=df)


# Next up:  https://stackoverflow.com/questions/9198334/how-to-build-up-a-html-table-with-a-simple-for-loop-in-jinja2


if __name__ == "__main__":
    app.run()
