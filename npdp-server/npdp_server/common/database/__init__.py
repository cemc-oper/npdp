# coding=utf-8


def get_node_dict(node):
    return {
        'labels': list(node.labels()),
        'props': dict(node),
        'id': node.__remote__._id
    }


def get_relation_dict(relation):
    relation_dict = {
        'type': relation.type(),
        'props': dict(relation),
        'id': relation.__remote__._id
    }
    return relation_dict