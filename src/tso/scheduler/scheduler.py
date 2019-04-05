from astroplan.scheduling import Schedule, PriorityScheduler, Transitioner, SequentialScheduler
from astroplan import Observer, FixedTarget, ObservingBlock
from astroplan.constraints import TimeConstraint
from astroplan import download_IERS_A
from astropy.time import Time
from astropy import units as u

from tso.importer import data_importer as di
from tso.scheduler import constraint_aggregator as ca

import random
import warnings
import json

def create_transitioner(slew_rate, filters):
    # Apply atropy units to all config values
    slew_rate = slew_rate * u.deg / u.second
    for key in filters['filter'].keys():
        filters['filter'][key] = filters['filter'][key] * u.second
    return Transitioner(slew_rate, filters)


def generate_schedule(config, start_datetime, end_datetime, requests):

    # Sometimes a warning arises called OldEarthOrientationDataWarning which means the following line must run to refresh
    # we should find a way to catch this warning and only download when necessary

    download_IERS_A()
    cfht = Observer.at_site('cfht')
    transitioner = create_transitioner(config['slew_rate'], config['filters'])

    # Retrieve global constraints from Constraint Aggregator
    global_constraints = ca.initialize_constraints()

    # These are hard
    read_out = 20 * u.second
    n_exp = 5

    blocks = []

    # Hardcoded test constraints -- may have some on the ObservingBlock level
    # These differ from global_constraints above which are applied to all observations in the schedule

    # half_night_start = Time('2019-03-12 02:00')
    # half_night_end = Time('2019-03-12 08:00')
    # first_half_night = TimeConstraint(half_night_start, half_night_end)

    # for request in requests:

    #     # target = request.get_target()
    #     duration = request.observation_duration * u.second
    #     block = ObservingBlock.from_exposures(target, request.priority,
    #         duration, n_exp, read_out,
    #         configuration = {'filter': 'B'},
    #         constraints = [first_half_night])

    #     print(str(block))

    #     blocks.append(block)

    # deneb_exp = 100 * u.second
    # m13_exp = 50 * u.second

    for request in requests:
        for bandpass in ['MSE']:
            block = ObservingBlock.from_exposures(request.target, request.priority, request.duration, n_exp, read_out,
                                            configuration={'filter': bandpass},
                                            constraints=[])
            blocks.append(block)
            print('Appending block with Target {} and filter {}'.format(request.target, bandpass))


    prior_scheduler = PriorityScheduler(constraints=global_constraints,
                                          observer=cfht,
                                          transitioner=transitioner)

    priority_schedule = Schedule(Time(start_datetime), Time(end_datetime))

    prior_scheduler(blocks, priority_schedule)

    return priority_schedule


if '__name__' == '__main__':
    generate_schedule(None)
