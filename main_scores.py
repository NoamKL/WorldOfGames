#!/usr/bin python3

from flask import Flask, render_template

from utils import SCORES_FILE_NAME

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        score = open(SCORES_FILE_NAME, 'r').read()
        return render_template("scores.html", score=score)
    except FileNotFoundError as error:
        return render_template("scores.html", error=error)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True, port=10000)
