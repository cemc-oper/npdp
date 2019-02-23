# coding=utf-8
from setuptools import setup

setup(
    name='npdp-server',

    version='1.0',

    description='NPDP Seaver',
    long_description=__doc__,

    packages=['npdp_server'],

    include_package_data=True,

    zip_safe=False,

    install_requires=[
        'click',
        'Flask',
        'PyYAML',
        'py2neo<4.0'
    ]
)
