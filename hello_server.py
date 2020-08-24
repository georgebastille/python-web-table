import os

import pandas as pd
from flask import Flask, render_template

# Set environment variables
os.environ["FLASK_ENV"] = "development"

app = Flask(__name__)


@app.route("/")
def landing():
    df = get_data()
    return render_template("greetings.html", dataframe=df)


@app.route("/<dateFilter>")
def run_query(dateFilter):
    df = get_data(dateFilter)
    return render_template("greetings.html", dataframe=df)


# Next up:  https://stackoverflow.com/questions/9198334/how-to-build-up-a-html-table-with-a-simple-for-loop-in-jinja2


def get_data(dateFilter=None):
    df = pd.read_csv("./data/Repossession-2019-07.csv")
    if dateFilter:
        df["date_idx"] = pd.to_datetime(df["date"])
        df.set_index("date_idx", inplace=True)
        df = df[dateFilter]
    return df.to_dict("records")


if __name__ == "__main__":
    app.run()
