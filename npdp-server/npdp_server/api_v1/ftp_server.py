# coding=utf-8
import time

from flask import jsonify, current_app
from py2neo import Graph, NodeSelector

from npdp_server.api_v1 import api_v1_app
from npdp_server.common.database import get_node_dict, get_relation_dict


@api_v1_app.route('/ftp-server/ids/<int:node_id>/products', methods=['GET'])
def query_ftp_server_products(node_id):
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

    cursor = database.run(f'MATCH (a:OperationSystem)-[]-(b:ProductSet)'
                          f'-[]-(t:TransmissionTask)-[]-(f:FTPServer) '
                          f'WHERE id(f)={node_id} RETURN DISTINCT a, b')
    records = cursor.data()

    if len(records) == 0:
        result = {
            'app': 'npdp-server',
            'api': 'ftp-server/ids/products',
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
        operation_system = record['a']
        operation_system_dict = get_node_dict(operation_system)
        product_set = record['b']
        product_set_dict = get_node_dict(product_set)

        products.append({
            'operation_system': operation_system_dict,
            'product_set': product_set_dict
        })

    result = {
        'app': 'npdp-server',
        'api': 'ftp-server/ids/products',
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
