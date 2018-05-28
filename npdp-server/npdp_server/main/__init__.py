# coding=utf-8
from flask import Blueprint

main_app = Blueprint('main_app', __name__, template_folder='template')

import npdp_server.main.controller
