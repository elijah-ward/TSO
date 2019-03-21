from astroplan.scheduling import Schedule, PriorityScheduler, Transitioner, SequentialScheduler
from astroplan import Observer, FixedTarget, ObservingBlock
from astroplan.constraints import TimeConstraint
from astroplan import download_IERS_A
from astropy.time import Time
from astropy import units as u

from tso.importer import data_importer as di
from tso.scheduler import constraint_aggregator as ca


def create_transitioner(slew_rate):
    return Transitioner(slew_rate,
                        {'filter': {('B', 'G'): 10 * u.second,
                                    ('G', 'R'): 10 * u.second,
                                    'default': 30 * u.second}})


def generate_schedule(schedule_horizon):

    print('Inside scheduler.py')

    download_IERS_A()

    cfht = Observer.at_site('cfht')
    deneb = FixedTarget.from_name('Deneb')
    m13 = FixedTarget.from_name('M13')

    noon_before = Time('2019-03-11 19:00')
    noon_after = Time('2019-03-12 19:00')

    global_constraints = ca.initialize_constraints()

    # requests = di.get_observations_with_constraint(min_priority=99)

    read_out = 20 * u.second
    n_exp = 5
    blocks = []

    half_night_start = Time('2019-03-12 02:00')
    half_night_end = Time('2019-03-12 08:00')
    first_half_night = TimeConstraint(half_night_start, half_night_end)

    # for request in requests:

    #     # target = request.get_target()
    #     duration = request.observation_duration * u.second
    #     block = ObservingBlock.from_exposures(target, request.priority,
    #         duration, n_exp, read_out,
    #         configuration = {'filter': 'B'},
    #         constraints = [first_half_night])

    #     print(str(block))

    #     blocks.append(block)

    deneb_exp = 100 * u.second
    m13_exp = 50 * u.second

    for priority, bandpass in enumerate(['B', 'G', 'R']):
        # We want each filter to have separate priority (so that target
        # and reference are both scheduled)
        b = ObservingBlock.from_exposures(deneb, priority, deneb_exp, n_exp, read_out,
                                          configuration={'filter': bandpass},
                                          constraints=[first_half_night])
        blocks.append(b)
        b = ObservingBlock.from_exposures(m13, priority, m13_exp, n_exp, read_out,
                                          configuration={'filter': bandpass},
                                          constraints=[first_half_night])
        blocks.append(b)

    slew_rate = .8 * u.deg / u.second
    transitioner = create_transitioner(slew_rate)

    prior_scheduler = SequentialScheduler(constraints=global_constraints,
                                          observer=cfht,
                                          transitioner=transitioner)

    priority_schedule = Schedule(noon_before, noon_after)

    prior_scheduler(blocks, priority_schedule)

    print(priority_schedule.to_table())


if '__name__' == '__main__':
    generate_schedule(0)
