"""
Persistence Utilities

We will be primarily be interfacing with a mySQL DB.
"""

import mysql.connector

def get_mysql_connection(db_config):

    return mysql.connector.connect(
        host=db_config["HOST"],
        port=db_config["PORT"],
        database=db_config["DB"],
        user=db_config["USER"],
        password=db_config["PASSWORD"]
    )
