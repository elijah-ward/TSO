"""
Persistence Utilities

We will be primarily be interfacing with a mySQL DB.
"""

import mysql.connector
from configuration import configuration_parser

config = configuration_parser.get_database_config()


def get_mysql_connection():
    return mysql.connector.connect(
        host=config["HOST"],
        port=config["PORT"],
        database=config["DB"],
        user=config["USER"],
        password=config["PASSWORD"]
    )
