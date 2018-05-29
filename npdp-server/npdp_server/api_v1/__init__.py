# coding=utf-8
import time

from flask import Blueprint, request, current_app, jsonify
from py2neo import Graph, NodeSelector

api_v1_app = Blueprint('api_v1_app', __name__)


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

    if search_type == "operation_system":
        selector = NodeSelector(database)
        records = selector.select("OperationSystem")\
            .where("_.name =~ '.*{input}.*'".format(input=search_input))
        result_list = []
        for record in records:
            result_list.append(dict(record))
        result = {
            'app': 'npdp-server',
            'api': 'search',
            'timestamp': time.time(),
            'data': {
                'status': 'ok',
                'request': request.form,
                'operation_systems': result_list
            }
        }
    elif search_type == "ftp":
        selector = NodeSelector(database)
        records = selector.select("FTPServer") \
            .where("_.name =~ '.*{input}.*' or _.host =~ '.*{input}.*".format(input=search_input))
        result_list = []
        for record in records:
            result_list.append(dict(record))
        result = {
            'app': 'npdp-server',
            'api': 'search',
            'timestamp': time.time(),
            'data': {
                'status': 'ok',
                'request': request.form,
                'operation_systems': result_list
            }
        }
    elif search_type == "all":
        result = {
            'app': 'npdp-server',
            'api': 'search',
            'timestamp': time.time(),
            'data': {
                'status': 'error',
                'message': 'type not implemented.',
                'request': request.form,
            }
        }
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
