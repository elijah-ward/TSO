"""
Configuration Parser

Takes a path to the desired config file relative to the current working directory
that will store some end-user configuration values and returns them to the application.

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
