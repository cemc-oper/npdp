# coding=utf-8
import time

from flask import Blueprint, request, current_app, jsonify
from py2neo import Graph, NodeSelector

api_v1_app = Blueprint('api_v1_app', __name__)

import npdp_server.api_v1.node
import npdp_server.api_v1.relationship
import npdp_server.api_v1.operation_system
import npdp_server.api_v1.ftp_server
from npdp_server.common.database import get_node_dict


@api_v1_app.route('/search', methods=['POST'])
def search():
    print(request.json)
    search_type = request.json['search_type']
    search_input = request.json['search_input']

    database_config = current_app.config['SERVER_CONFIG']['database']

    print("[api_v1_app] /search: connecting to neo4j...")
    database = Graph(
        "{protocol}://{ip}:{port}".format(
            protocol=database_config['connection']['protocol'],
            ip=database_config['connection']['ip'],
            port=database_config['connection']['port']
        ),
        user=database_config['auth']['user'],
        password=database_config['auth']['password']
    )

    selector = NodeSelector(database)
    if search_type == "operation_system":
        records = selector.select("OperationSystem") \
            .where("(any(prop in keys(_) where _[prop] CONTAINS '{input}'))".format(input=search_input))
    elif search_type == "ftp":
        records = selector.select("FTPServer") \
            .where("(any(prop in keys(_) where _[prop] CONTAINS '{input}'))".format(input=search_input))
    elif search_type == "product":
        records = selector.select("ProductSet") \
            .where("(any(prop in keys(_) where _[prop] CONTAINS '{input}'))".format(input=search_input))
    elif search_type == "all":
        records = selector.select() \
            .where("(any(prop in keys(_) where _[prop] CONTAINS '{input}'))".format(input=search_input))
    else:
        result = {
            'app': 'npdp-server',
            'api': 'search',
            'timestamp': time.time(),
            'data': {
                'status': 'error',
                'message': 'type not supported.',
                'request': request.form
            }
        }
        return jsonify(result)

    result_list = []
    for record in records:
        node_dict = get_node_dict(record)
        result_list.append(node_dict)
    result = {
        'app': 'npdp-server',
        'api': 'search',
        'timestamp': time.time(),
        'data': {
            'status': 'ok',
            'request': request.form,
            'results': result_list
        }
    }

    return jsonify(result)
