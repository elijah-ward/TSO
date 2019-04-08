# NOTE: This requires a functional change to test scheduler.py - it was ported over from the genetic algorithm scheduler because the "generate tests" pattern may be useful

import pytest
import json
from tso.scheduler import scheduler
from tso.scheduler.utils import generate_mock_requests as gr
from astroplan.scheduling import Schedule, Transitioner

N_BLOCKS = 5

testSchedulerConfig = json.loads(u'''{
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
}
''')

mock_global_constraint_config = json.loads(u'''{
    "AirmassConstraint": {
        "max": 3,
        "boolean_constraint": "False"
    },
    "AtNightConstraint": {}
}
''')


def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = sorted(funcarglist[0])
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames]
                                    for funcargs in funcarglist])


class TestScheduler(object):

    params = {
        'test_generate_schedule': [dict(start_datetime='2019-03-10 19:00', end_datetime='2019-03-12 19:00', requests=gr.generate_mock_requests(N_BLOCKS)), ],
        'test_create_transitioner': [dict(slew_rate=testSchedulerConfig['slew_rate'], filter_config=testSchedulerConfig['filters']), ]
    }

    def test_generate_schedule(self, start_datetime, end_datetime, requests):
        schedule = scheduler.generate_schedule(
            testSchedulerConfig,
            mock_global_constraint_config,
            start_datetime,
            end_datetime,
            requests=requests
        )
        assert isinstance(schedule, Schedule)

    def test_create_transitioner(self, slew_rate, filter_config):
        transitioner = scheduler.create_transitioner(slew_rate, filter_config)
        assert isinstance(transitioner, Transitioner)
