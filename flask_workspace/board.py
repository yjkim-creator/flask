from flask import Flask, Blueprint, request, session, render_template, redirect, url_for

bp = Blueprint('board', __name__, url_prefix='/board')


@bp.route("/list")
def board_list():
    return "/board/list"

@bp.route("/view")
def board_view():
    return "/board/view"

@bp.route("/write")
def board_write():
    return "/board/write"