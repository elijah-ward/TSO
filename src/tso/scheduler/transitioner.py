from astroplan.scheduling import Transitioner
from astropy import units as u


def initialize(slew_rate, filter_transitions):

    slew_rate = .8 * u.deg / u.second
    transitioner = Transitioner(slew_rate,
                                {'filter': {('B', 'G'): 10 * u.second,
                                            ('G', 'R'): 10 * u.second,
                                            'default': 30 * u.second
                                            }})

    return transitioner
