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


def generate_schedule(
    telescope_config,
    global_constraint_configuration,
    start_datetime,
    end_datetime,
    no_weather_constraints=False,
    requests=None
):

    # Sometimes a warning arises called OldEarthOrientationDataWarning which means the following line must run to refresh
    # should find a way to catch this warning and only download when necessary

    download_IERS_A()
    cfht = Observer.at_site('cfht')
    transitioner = create_transitioner(telescope_config['slew_rate'], telescope_config['filters'])

    # Retrieve global constraints from Constraint Aggregator

    global_constraints = ca.initialize_constraints(
        global_constraint_configuration,
        start_datetime,
        end_datetime,
        no_weather_constraints
    )

    # Currently defined in config but may belong on the block-level instead
    read_out = telescope_config['read_out'] * u.second

    # TODO: gather this data from each ObservationRequest instead
    n_exp = 5

    blocks = []

    # In order to supply block-level constraints, they should be initialized from attributes of the source data
    # and passed into the ObservingBlock initialization below

    for request in requests:
        # For each filter available on the telescope
        # TODO: define the available set within config
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
