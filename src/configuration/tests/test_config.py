import pytest
import json
from configuration.config import Config

"""
test_config.py

Tests for the TSO global configuration object
"""

test_config_dict = json.loads(u'''{
    "telescope": {
        "slew_rate": 0.8,
        "filters": {
            "transitions": {
                "default": 30,
                "filter": [
                    {
                        "from": "B",
                        "to": "G",
                        "duration": 10
                    },
                    {
                        "from": "B",
                        "to": "R",
                        "duration": 10
                    },
                    {
                        "from": "G",
                        "to": "B",
                        "duration": 10
                    },
                    {
                        "from": "R",
                        "to": "B",
                        "duration": 10
                    }
                ]
            }
        }
    },
    "db": {
            "HOST": "127.0.0.1",
            "PORT": "3306",
            "DB": "tso",
            "USER": "tsouser",
            "PASSWORD": "password"
    }
}
''')

class TestConfig:

    def test_config_instantiate(self):
        config = Config(test_config_dict)
        assert(isinstance(config, Config))

    def test_get_database_config(self):
        config = Config(test_config_dict)
        db_config = config.get_database_config()
        assert(db_config['DB'] == 'tso')

    def test_get_telescope_config(self):
        config = Config(test_config_dict)
        tele_config = config.get_telescope_config()
        assert(tele_config['slew_rate'] == 0.8)
