#!/usr/bin python3
import click

SCORES_FILE_NAME = "score.txt"
BAD_RETURN_CODE = -1


def screen_cleaner():
    click.clear()
