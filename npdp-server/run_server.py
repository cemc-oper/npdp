#!/usr/bin/env python3
# coding=utf-8
from pathlib import Path
import click
import os
import sys


@click.command()
@click.option('-c', '--config-file', help='config file path')
@click.option('-s', '--static-folder', help='static folder')
@click.option('-t', '--template-folder', help='template folder')
def runserver(config_file, static_folder, template_folder):
    from npdp_server import create_app
    app = create_app(config_file,
                     str(Path(static_folder).absolute()),
                     str(Path(template_folder).absolute()))

    app.run(
        host=app.config['SERVER_CONFIG']['host']['ip'],
        port=app.config['SERVER_CONFIG']['host']['port']
    )


if __name__ == '__main__':
    runserver()
