# coding=utf-8
import time

from flask import jsonify, current_app
from py2neo import Graph, NodeSelector

from npdp_server.api_v1 import api_v1_app
from npdp_server.common.database import get_node_dict, get_relation_dict


@api_v1_app.route('/product-set/ids/<int:node_id>/destinations', methods=['GET'])
def query_product_set_destinations(node_id):
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

    cursor = database.run(f'MATCH (b:ProductSet)-[]-(:TransmissionTask)-[]-(d:Destination) '
                          f'WHERE id(b)={node_id} RETURN DISTINCT d')
    records = cursor.data()

    if len(records) == 0:
        result = {
            'app': 'npdp-server',
            'api': 'product-set/ids/destinations',
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
        destination = record['d']
        destination_dict = get_node_dict(destination)

        destinations.append(destination_dict)

    result = {
        'app': 'npdp-server',
        'api': 'product-set/ids/destinations',
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
