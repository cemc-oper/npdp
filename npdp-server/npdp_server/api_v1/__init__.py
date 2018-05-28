# coding=utf-8
from flask import Blueprint, request, current_app, jsonify
from py2neo import Graph, NodeSelector

api_v1_app = Blueprint('api_v1_app', __name__)


@api_v1_app.route('/search', methods=['POST'])
def search():
    search_type = request.form['type']
    search_context = request.form['context']

    database_config = current_app.config['SERVER_CONFIG']['database']

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
        print(list(selector.select("OperationSystem")
                   .where("_.name =~ '.*{context}.*'".format(context=search_context))))
    elif search_type == "ftp":
        pass
    elif search_type == "all":
        pass
    else:
        pass

    return jsonify({
        'status': 'ok'
    })
