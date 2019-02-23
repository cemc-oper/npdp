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
    print("static folder:{static_folder}".format(static_folder=static_folder))
    print("template folder:{template_folder}".format(template_folder=template_folder))
    app = Flask(__name__,
                static_folder=str(static_folder),
                template_folder=str(template_folder))

    from npdp_server.common.config import Config
    print('create_app: config_file_path=', config_file_path)
    app.config.from_object(Config.load_config(config_file_path))
    app.json_encoder = NPDPServerJSONEncoder

    with app.app_context():
        from npdp_server.main import main_app
        main_app.template_folder = template_folder
        main_app.static_folder = static_folder
        app.register_blueprint(main_app, url_prefix="")

        from npdp_server.api_v1 import api_v1_app
        app.register_blueprint(api_v1_app, url_prefix="/api/v1")
        api_v1_app.template_folder = template_folder
        api_v1_app.static_folder = static_folder

    return app
