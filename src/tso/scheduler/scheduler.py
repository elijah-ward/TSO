from astroplan.scheduling import Schedule, PriorityScheduler, Transitioner
from astroplan import Observer, FixedTarget, ObservingBlock
from astroplan.constraints import TimeConstraint
from astropy.time import Time
from astropy import units as u

from tso.importer import data_importer as di
from tso.scheduler import constraint_aggregator as ca

def create_transitioner(slew_rate):
    return Transitioner(slew_rate,
        {'filter': {('B','G'): 10*u.second,
                    ('G','R'): 10*u.second,
                    'default': 30*u.second}})

def generate_schedule(schedule_horizon):

    print("HERE WE AREEE")

    cfht = Observer.at_site('cfht')
    target = FixedTarget.from_name('Deneb')

    noon_before = Time('2019-03-11 19:00')
    noon_after = Time('2019-03-12 19:00')

    global_constraints = ca.initialize_constraints()

    requests = di.get_all_observations()

    read_out = 20 * u.second
    n_exp = 10
    blocks = []

    half_night_start = Time('2019-03-12 02:00')
    half_night_end = Time('2019-03-12 08:00')
    first_half_night = TimeConstraint(half_night_start, half_night_end)

    for request in requests:

        target = request.get_target()
        duration = request.duration * u.second
        block = ObservingBlock.from_exposures(target, request.priority,
            duration, n_exp, read_out,
            configuration = {'filter': 'B'},
            constraints = [first_half_night])

        blocks.append(block)

    slew_rate = .8*u.deg/u.second
    transitioner = create_transitioner(slew_rate)

    prior_scheduler = PriorityScheduler(constraints = global_constraints,
                                        observer = cfht,
                                        transitioner = transitioner)

    priority_schedule = Schedule(noon_before, noon_after)

    prior_scheduler(blocks, priority_schedule)

    priority_schedule.to_table()


if '__name__' == '__main__':
    generate_schedule(0)








