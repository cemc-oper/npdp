# coding=utf-8
from npdp_server.main import main_app

from flask import jsonify, render_template, abort


@main_app.route('/')
def get_index_page():
    return render_template("index.html")
