"""
Configuration Parser

Takes a path to the desired config file relative to the current working directory
that will store some end-user configuration values and returns them to the application.

"""

import json
import os
from pathlib import Path
from configuration.config import Config


def parse(conf_filepath, root_path=None):

    if root_path is None:
        current_dir = os.getcwd()
    else:
        current_dir = root_path

    file_location = '{}/{}'.format(current_dir, conf_filepath)

    with open(file_location, 'r') as f:
        config = json.load(f)
        return Config(config)
