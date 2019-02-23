"""
Configuration Parser

Takes a configurations.json file that will store some end-user configuration values
and returns them to the application.

At the moment this is scoped to the Database configuration.

"""

import json
from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'configuration.json'

with open(file_location, 'r') as f:
    config = json.load(f)


def get_database_config():
    return config["DB_CONFIG"]
