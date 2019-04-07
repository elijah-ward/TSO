"""
Configuration Parser

Takes a configurations.json file that will store some end-user configuration values
and returns them to the application.

At the moment this is scoped to the Database configuration.

"""

import json
import os
from pathlib import Path
from configuration.config import Config

def parse(conf_filepath):

    current_dir = os.getcwd()
    file_location = '{}/{}'.format(current_dir, conf_filepath)
    print(file_location)

    with open(file_location, 'r') as f:
        config = json.load(f)
        return Config(config)
