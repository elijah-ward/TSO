from tso.tsocli import __main__ as tsocli
from tso.tsocli.command.pipeline import cli_pipeline
import pytest
from unittest.mock import patch


@pytest.fixture(scope="module")
def run_end_to_end():
    return True 


class TestCliIntegration:
    """
    Test Cli Integration

    Meant to have a single place to run the entire application from end-to-end,
    the fixture above should be set to True to run it end to end, setting to False for quickness sake
    """

    def test_cli_should_call_pipeline_when_successful(self, run_end_to_end):
        real_pipeline = cli_pipeline

        use_this_when_running_from_here_locally = '../../../../tso_config.json'
        use_this_when_running_pytest_from_the_root = 'tso_config.json'

        arguments = [
            'schedule',
            '--max-observation-priority',
            '300',
            '--start-date-time',
            '2019-04-07 17:00',
            '--end-date-time',
            '2019-04-7 23:00',
            '--export-to-file',
            '--export-to-browser',
            '--config-file',
            use_this_when_running_pytest_from_the_root
        ]

        if run_end_to_end:
            with patch('tso.tsocli.command.cli_pipeline', wraps=real_pipeline) as mock_pipeline:
                tsocli.main(arguments)
        else:
            with patch('tso.tsocli.command.cli_pipeline') as mock_pipeline:
                tsocli.main(arguments)
