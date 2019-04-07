import pytest
import os
from configuration import configuration_parser
from configuration.config import Config

"""
test_configuration_parser.py

Tests for the configuration parser functional module
"""

class TestConfigurationParser:

    def test_parse(self):
        config = configuration_parser.parse('helpers/noop_config.json', os.path.split(os.path.abspath(__file__))[0])
        assert(isinstance(config, Config))
