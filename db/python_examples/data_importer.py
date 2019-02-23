"""
data_importer.py

An example of the beginnings of what an observation importer could look like
"""

import mysql.connector
from src.configuration import configuration_parser


def get_observations():

    config = configuration_parser.get_database_config()

    db = mysql.connector.connect(
        host=config["HOST"],
        port=config["PORT"],
        database=config["DB"],
        user=config["USER"],
        password=config["PASSWORD"]
    )
    cursor = db.cursor()
    lines = cursor.execute("SELECT * FROM observation;")

    print(lines)

    for line in lines:
        print(line)


get_observations()

