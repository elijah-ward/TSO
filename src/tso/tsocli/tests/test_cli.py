"""
CLI tests
"""

from tso.tsocli import __main__ as tsocli
import pytest
from unittest.mock import patch, MagicMock, mock_open


mock_configurqation = "{}"


class TestCli:

    def test_cli_should_exit_with_no_args(self):

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            tsocli.main([])

        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.code == 1

    def test_cli_should_exit_with_only_one_arg(self):

        with pytest.raises(SystemExit) as pytest_wrapped_e_pseudo_name:
            tsocli.main(['s'])

        with pytest.raises(SystemExit) as pytest_wrapped_e_full_name:
            tsocli.main(['schedule'])

        # Both Exceptions should be the same
        assert pytest_wrapped_e_pseudo_name.type == pytest_wrapped_e_full_name.type
        assert pytest_wrapped_e_pseudo_name.value.code == pytest_wrapped_e_full_name.value.code

        # The exceptions should be a System Exit
        assert pytest_wrapped_e_pseudo_name.type == SystemExit
        assert pytest_wrapped_e_pseudo_name.value.code == 1

    @patch('configuration.configuration_parser.parse', return_value=mock_configurqation)
    @patch('tso.tsocli.command.cli_pipeline')
    def test_cli_should_call_pipeline_when_successful(self, mock_pipeline, mock_config_parser):
        tsocli.main([
            'schedule',
            '--start-date-time',
            '2019-03-01 19:00',
            '--end-date-time',
            '2019-03-12 19:00',
            '--export-to-file',
            '--export-to-browser'
        ])

        assert mock_pipeline.called

    @patch('configuration.configuration_parser.parse', return_value=mock_configurqation)
    @patch('tso.tsocli.command.cli_pipeline')
    def test_cli_should_have_default_date_time_values(self, mock_pipeline, mock_config_parser):
        tsocli.main([
            'schedule',
            '--export-to-file'
        ])

        assert mock_pipeline.call_args.start_date_time
        assert mock_pipeline.call_args.end_date_time


