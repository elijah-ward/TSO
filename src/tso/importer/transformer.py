from src.tso.observation import dynamic_constraint, observation_block
from astropy import units as u
from astropy.coordinates import SkyCoord


def transform(data_string):
    print('Transforming the data :: {}'.format(data_string))
    d_constraint = dynamic_constraint.DynamicConstraint(2590, 2)
    constraints = [d_constraint]
    c = SkyCoord(ra=10.625*u.degree, dec=41.2*u.degree, frame='icrs')
    temp_block = observation_block.ObservationBlock(22, "Kirk", 10, c, constraints)

    return temp_block
