# NOTE: This requires a functional change to test scheduler.py - it was ported over from the genetic algorithm scheduler because the "generate tests" pattern may be useful

import pytest
from tso.scheduler import scheduler

OBSERVATION_BLOCKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = sorted(funcarglist[0])
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames]
                                    for funcargs in funcarglist])


class TestScheduler(object):

    params = {
        'test_return_list': [dict(timeslots=1000, pop=1000, gen=10, cxpb=0.5, mutpb=0.2, blocks=OBSERVATION_BLOCKS), ]
    }

    def test_generate_schedule(self, timeslots, pop, gen, cxpb, mutpb, blocks):
        optimal_ind = op_sched.optimize_schedule(
            timeslots, pop, gen, cxpb, mutpb, blocks)
        assert isinstance(optimal_ind, list)
