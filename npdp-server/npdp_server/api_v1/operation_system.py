# coding=utf-8
import time

from flask import jsonify, current_app
from py2neo import Graph, NodeSelector

from npdp_server.api_v1 import api_v1_app
from npdp_server.common.database import get_node_dict, get_relation_dict


@api_v1_app.route('/operation-system/ids/<int:node_id>/products', methods=['GET'])
def query_operation_system_products(node_id):
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

    cursor = database.run(f'MATCH (a:OperationSystem)-[]-(b:ProductSet) WHERE id(a)={node_id} RETURN DISTINCT b')
    records = cursor.data()

    if len(records) == 0:
        result = {
            'app': 'npdp-server',
            'api': 'operation-system/ids/products',
            'timestamp': time.time(),
            'data': {
                'status': 'error',
                'message': "can't find products.",
                'request': {
                    'id': node_id
                }
            }
        }
        return jsonify(result)

    products = []

    for record in records:
        product_set = record['b']
        product_set_dict = get_node_dict(product_set)

        products.append(product_set_dict)

    result = {
        'app': 'npdp-server',
        'api': 'operation-system/ids/products',
        'timestamp': time.time(),
        'data': {
            'status': 'ok',
            'request': {
                'id': node_id
            },
            'products': products
        }
    }

    return jsonify(result)


@api_v1_app.route('/operation-system/ids/<int:node_id>/destinations', methods=['GET'])
def query_operation_system_destination(node_id):
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

    cursor = database.run(f'MATCH (a:OperationSystem)-[]-(:ProductSet)'
                          f'-[]-(:TransmissionTask)-[]-(b:Destination) '
                          f'WHERE id(a)={node_id} RETURN DISTINCT b')
    records = cursor.data()

    if len(records) == 0:
        result = {
            'app': 'npdp-server',
            'api': 'operation-system/ids/destinations',
            'timestamp': time.time(),
            'data': {
                'status': 'error',
                'message': "can't find destinations.",
                'request': {
                    'id': node_id
                }
            }
        }
        return jsonify(result)

    destinations = []

    for record in records:
        destination = record['b']
        destination_dict = get_node_dict(destination)

        destinations.append(destination_dict)

    result = {
        'app': 'npdp-server',
        'api': 'operation-system/ids/destinations',
        'timestamp': time.time(),
        'data': {
            'status': 'ok',
            'request': {
                'id': node_id
            },
            'destinations': destinations
        }
    }

    return jsonify(result)