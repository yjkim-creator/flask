from flask import Flask, Blueprint, request, session, render_template, redirect, url_for

bp = Blueprint('test', __name__, url_prefix='/test')


@bp.route("/list")
def test_list():
    return "Blueprint test list"