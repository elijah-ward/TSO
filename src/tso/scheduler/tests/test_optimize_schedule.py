import pytest
from tso.scheduler import optimize_schedule as op_sched

OBSERVATION_BLOCKS = [1,2,3,4,5,6,7,8,9,10]

def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = sorted(funcarglist[0])
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames]
            for funcargs in funcarglist])

class TestOptimizeSchedule(object):

    params = {
        'test_return_list': [dict(timeslots=1000, pop=1000, gen=10, cxpb=0.5, mutpb=0.2, blocks=OBSERVATION_BLOCKS), ]
    }

    def test_return_list(self, timeslots, pop, gen, cxpb, mutpb, blocks):
        optimal_ind = op_sched.optimize_schedule(timeslots, pop, gen, cxpb, mutpb, blocks)
        assert isinstance(optimal_ind, list)
