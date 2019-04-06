"""
CLI tests
"""

from tso.tsocli import __main__ as tsocli
import pytest
from pytest_mock import mocker


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

    def test_cli_should_call_pipeline_with_default_args(self):

        # TODO: Mock out the COMMAND import that TSO Cli Uses
        # TODO: TEST IS FAILING FAILING FAILING

        mocker.patch('tsocli.command')

        tsocli.main("""schedule --startDateTime "2019-03-01 19:00" --endDateTime "2019-03-12 19:00" --exportToFile --exportToBrowser""".split(" "))


