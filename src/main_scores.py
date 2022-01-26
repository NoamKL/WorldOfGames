#!/usr/bin python3

from flask import Flask, render_template

from utils import SCORES_FILE_NAME


def score_server():
    app = Flask(__name__)
    app.run()
    try:
        score = open(SCORES_FILE_NAME, 'r').read()
        return render_template("scores.html", score=score)
    except FileNotFoundError as error:
        return render_template("scores.html", error=error)
