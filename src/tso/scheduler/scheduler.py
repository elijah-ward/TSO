from astroplan.scheduling import Schedule, PriorityScheduler, Transitioner, SequentialScheduler
from astroplan import Observer, FixedTarget, ObservingBlock
from astroplan.constraints import TimeConstraint
from astroplan import download_IERS_A
from astropy.time import Time
from astropy import units as u

from tso.importer import data_importer as di
from tso.scheduler import constraint_aggregator as ca

import random

def create_transitioner(slew_rate, filters):
    # Apply atropy units to all config values
    slew_rate = slew_rate * u.deg / u.second
    for key in filters['filter'].keys():
        filters['filter'][key] = filters['filter'][key] * u.second
    return Transitioner(slew_rate, filters)


def generate_schedule(config, start_datetime, end_datetime, ):

    print('Inside scheduler.py')
    download_IERS_A()
    cfht = Observer.at_site('cfht')
    transitioner = create_transitioner(config['slew_rate'], config['filters'])

    # Placeholder -- generating demonstration targets
    n_targets_test = 30
    target_names = ['Deneb', 'M13', 'sirius', 'M31', 'Polaris', 'Vega']
    targets = []

    # dynamically produce a list of FixedTarget objects from the target_names identifiers
    # This is just a placeholder until we figure out properly creating targets from coords

    for i in range(0,n_targets_test):
        targets.append(FixedTarget.from_name(target_names[random.randrange(len(target_names))]))

    # Retrieve global constraints from Constraint Aggregator
    global_constraints = ca.initialize_constraints()

    # requests = di.get_observations_with_constraint(min_priority=99)

    # These are hard
    read_out = 20 * u.second
    n_exp = 5

    blocks = []

    # Hardcoded test constraints -- may have some on the ObservingBlock level
    # These differ from global_constraints above which are applied to all observations in the schedule

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

    for target in targets:
        for priority, bandpass in enumerate(['MSE']):
            block = ObservingBlock.from_exposures(target, priority, deneb_exp, n_exp, read_out,
                                            configuration={'filter': bandpass},
                                            constraints=[])
            blocks.append(block)
            print('Appending block with Target {} and filter {}'.format(target, bandpass))

    # for priority, bandpass in enumerate(['B', 'G', 'R']):
    #     # We want each filter to have separate priority (so that target
    #     # and reference are both scheduled)
    #     b = ObservingBlock.from_exposures(deneb, priority, deneb_exp, n_exp, read_out,
    #                                       configuration={'filter': bandpass},
    #                                       constraints=[])
    #     blocks.append(b)
    #     b = ObservingBlock.from_exposures(m13, priority, m13_exp, n_exp, read_out,
    #                                       configuration={'filter': bandpass},
    #                                       constraints=[])
    #     blocks.append(b)

    prior_scheduler = SequentialScheduler(constraints=[],
                                          observer=cfht,
                                          transitioner=transitioner)

    priority_schedule = Schedule(Time(start_datetime), Time(end_datetime))

    prior_scheduler(blocks, priority_schedule)

    print(priority_schedule.to_table())


if '__name__' == '__main__':
    generate_schedule(None)
