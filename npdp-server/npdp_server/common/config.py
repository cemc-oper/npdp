# coding=utf=8
from pathlib import Path
import yaml


class Config(object):
    def __init__(self, config_path: str or Path):
        with open(config_path) as config_file:
            config_dict = yaml.load(config_file)
            server_config = config_dict['npdp_server']
            self.SERVER_CONFIG = server_config

            if 'debug' in server_config:
                debug_config = server_config['debug']
                if 'flask_debug' in debug_config:
                    flask_debug = debug_config['flask_debug']
                    if flask_debug is True:
                        self.DEBUG = True
                    elif flask_debug is not True:
                        self.DEBUG = False

    @classmethod
    def load_config(cls, config_file_path: str or Path):
        print("config_file_path:", str(config_file_path))
        config_object = Config(config_file_path)
        return config_object
