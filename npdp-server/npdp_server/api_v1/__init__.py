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

    selector = NodeSelector(database)
    if search_type == "operation_system":
        records = selector.select("OperationSystem") \
            .where("(any(prop in keys(_) where _[prop] CONTAINS '{input}'))".format(input=search_input))
    elif search_type == "ftp":
        records = selector.select("FTPServer") \
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
        node_dict = {
            'labels': list(record.labels()),
            'props': dict(record),
            'id': record.__remote__._id
        }
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


@api_v1_app.route('/node/ids/<node_id>', methods=['GET'])
def query_node_by_id(node_id):

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
    records = list(selector.select()
                   .where("id(_)={node_id}".format(node_id=node_id)))

    if len(records) == 0:
        result = {
            'app': 'npdp-server',
            'api': 'node/ids',
            'timestamp': time.time(),
            'data': {
                'status': 'error',
                'message': "can't find node by id.",
                'request': {
                    'id': node_id
                }
            }
        }
        return jsonify(result)

    record = records[0]
    node_dict = {
        'labels': list(record.labels()),
        'props': dict(record),
        'id': node_id
    }

    result = {
        'app': 'npdp-server',
        'api': 'node/ids',
        'timestamp': time.time(),
        'data': {
            'status': 'ok',
            'request': {
                'id': node_id
            },
            'node': node_dict
        }
    }

    return jsonify(result)
