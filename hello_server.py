import os

import pandas as pd
from flask import Flask, render_template, request

# Set environment variables
os.environ["FLASK_ENV"] = "development"

app = Flask(__name__)


@app.route("/")
def landing():
    df = get_data()
    return render_template("tabular.html", rows=df)


@app.route("/query")
def run_query():
    params = request.args
    df = get_data(params.get("dateFilter", None))
    return render_template("tabular.html", rows=df)


def get_data(dateFilter=None):
    df = pd.read_csv("./data/Repossession-2019-07.csv")
    if dateFilter:
        df["date_idx"] = pd.to_datetime(df["date"])
        df.set_index("date_idx", inplace=True)
        df = df[dateFilter]
    return df.to_dict("records")


if __name__ == "__main__":
    app.run()
