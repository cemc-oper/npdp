# coding=utf-8
from pathlib import Path
from datetime import datetime, date, time, timedelta

from flask import Flask
from flask.json import JSONEncoder


class NPDPServerJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime("%Y-%m-%dT%H:%M:%S")
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, time):
            return obj.strftime('%H:%M:%S')
        elif isinstance(obj, timedelta):
            return {'day': obj.days, 'seconds': obj.seconds}
        return JSONEncoder.default(self, obj)


def create_app(config_file_path=None, static_folder=None, template_folder=None):
    static_folder = str(static_folder)
    template_folder = str(template_folder)
    app = Flask(__name__,
                static_folder=static_folder,
                template_folder=template_folder)

    from npdp_server.common.config import Config
    app.config.from_object(Config.load_config(config_file_path))
    app.json_encoder = NPDPServerJSONEncoder

    with app.app_context():
        from npdp_server.main import main_app
        app.register_blueprint(main_app, url_prefix="")

        from npdp_server.api_v1 import api_v1_app
        app.register_blueprint(api_v1_app, url_prefix="/api/v1")

    return app
