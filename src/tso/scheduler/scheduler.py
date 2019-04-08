from astroplan.scheduling import Schedule, PriorityScheduler, Transitioner, SequentialScheduler
from astroplan import Observer, FixedTarget, ObservingBlock
from astroplan.constraints import TimeConstraint
from astroplan import download_IERS_A
from astropy.time import Time
from astropy import units as u
from astropy.coordinates import SkyCoord

from tso.importer import data_importer as di
from tso.scheduler import constraint_aggregator as ca

import random
import warnings
import json


def create_transitioner(slew_rate, filter_config):
    # Apply atropy units to all config values
    slew_rate = slew_rate * u.deg / u.second

    # Gather filter transitions from the provided config
    # This iteration is heavily subscriptive to the structure within the example config file
    filters = {}
    filters['filter'] = {}
    for transition in filter_config['transitions']['filter']:
        transition_from = transition['from']
        transition_to = transition['to']
        filter_pair = (transition_from, transition_to)
        filters['filter'][filter_pair] = transition['duration'] * u.second

    # If a transition isn't supplied for a filter pair, the default duration is used
    filters['filter']['default'] = filter_config['transitions']['default'] * u.second
    return Transitioner(slew_rate, filters)


def generate_schedule(config, global_constraint_configuration, start_datetime, end_datetime, requests=None):

    # Sometimes a warning arises called OldEarthOrientationDataWarning which means the following line must run to refresh
    # we should find a way to catch this warning and only download when necessary

    download_IERS_A()
    cfht = Observer.at_site('cfht')
    transitioner = create_transitioner(config['slew_rate'], config['filters'])

    # Retrieve global constraints from Constraint Aggregator

    global_constraints = ca.initialize_constraints(
        global_constraint_configuration,
        start_datetime,
        end_datetime
    )

    # hardcoded but should come from block
    read_out = 20 * u.second
    n_exp = 5

    blocks = []

    # Hardcoded test constraints -- may have some on the ObservingBlock level
    # These differ from global_constraints above which are applied to all observations in the schedule

    # half_night_start = Time('2019-03-12 02:00')
    # half_night_end = Time('2019-03-12 08:00')
    # first_half_night = TimeConstraint(half_night_start, half_night_end)

    for request in requests:
        for bandpass in ['B', 'G', 'R']:
            block = ObservingBlock.from_exposures(
                request.target,
                request.priority,
                request.duration,
                n_exp,
                read_out,
                configuration={'filter': bandpass},
                constraints=[]
            )
            blocks.append(block)
            print('Appending block {} with Target {} and filter {}'.format(block, request.target, bandpass))

    prior_scheduler = PriorityScheduler(
        constraints=global_constraints,
        observer=cfht,
        transitioner=transitioner
    )

    priority_schedule = Schedule(Time(start_datetime), Time(end_datetime))

    prior_scheduler(blocks, priority_schedule)

    return priority_schedule


if '__name__' == '__main__':
    generate_schedule(None)
