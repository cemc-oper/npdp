import time

from flask import jsonify, current_app
from py2neo import Graph, NodeSelector

from npdp_server.api_v1 import api_v1_app


@api_v1_app.route('/relationship/<node_id>', methods=['GET'])
def query_relationship(node_id):
    pass
