# coding=utf-8
import time

from flask import jsonify, current_app
from py2neo import Graph, NodeSelector

from npdp_server.api_v1 import api_v1_app
from npdp_server.common.database import get_node_dict, get_relation_dict


@api_v1_app.route('/node/ids/<int:node_id>', methods=['GET'])
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


@api_v1_app.route('/node/ids/<int:node_id>/relationship', methods=['GET'])
def query_node_relationship_by_id(node_id):
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

    cursor = database.run(f'MATCH (a)-[r]-(b) WHERE id(a)={node_id} RETURN a,r,b')
    records = cursor.data()

    if len(records) == 0:
        result = {
            'app': 'npdp-server',
            'api': 'node/ids/relationship',
            'timestamp': time.time(),
            'data': {
                'status': 'error',
                'message': "can't find relationships by id.",
                'request': {
                    'id': node_id
                }
            }
        }
        return jsonify(result)

    relationships = []

    for record in records:
        relation = record['r']
        relation_dict = get_relation_dict(relation)
        start_node = relation.start_node()
        start_node_dict = get_node_dict(start_node)
        end_node = relation.end_node()
        end_node_dict = get_node_dict(end_node)

        if start_node_dict['id'] == node_id:
            relation_dict['end_node'] = end_node_dict
        else:
            relation_dict['start_node'] = start_node_dict
        relationships.append(relation_dict)

    result = {
        'app': 'npdp-server',
        'api': 'node/ids/relationship',
        'timestamp': time.time(),
        'data': {
            'status': 'ok',
            'request': {
                'id': node_id
            },
            'relationships': relationships
        }
    }

    return jsonify(result)
