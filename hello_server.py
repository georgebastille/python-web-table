import os
from typing import Dict, List

import matplotlib
import pandas as pd  # type: ignore
from flask import Flask, render_template, request

matplotlib.use("agg")
import matplotlib.pyplot as plt

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
    return render_template("tabular.html", rows=df, image="static/chart.png")


def get_data(dateFilter: str = None) -> List[Dict]:
    # TODO: Make this an interface and import it
    df = pd.read_csv("./data/Repossession-2019-07.csv")
    df["date_idx"] = pd.to_datetime(df["date"], dayfirst=True)
    df.set_index("date_idx", inplace=True)
    if dateFilter:
        df = df.loc[dateFilter]
    fig = df.SalesVolume.plot(figsize=(10, 3)).get_figure()
    fig.savefig("./static/chart.png")
    plt.close()
    return df.to_dict("records")


if __name__ == "__main__":
    app.run()
