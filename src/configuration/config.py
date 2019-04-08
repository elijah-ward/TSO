import json

"""
config.py

Global configuration object for TSO
"""


class Config:

    def __init__(self, config_dict):
        self.config = config_dict

    def get_database_config(self):
        return self.config['db']

    def get_telescope_config(self):
        return self.config['telescope']

    def get_global_constraint_config(self):
        return self.config['global_constraints']

    def __str__(self):
        return str(json.dumps(self.config))
