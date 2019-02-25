from src.tso.observation import dynamic_constraint, observation_request
from astropy import units as u
from astropy.coordinates import SkyCoord


def transform(data_string):
    print('Transforming the data :: {}'.format(data_string))
    d_constraint = dynamic_constraint.DynamicConstraint(2590, 2)
    constraints = [d_constraint]
    c = SkyCoord(ra=10.625*u.degree, dec=41.2*u.degree, frame='icrs')
    temp_block = observation_request.ObservationRequest(
        22, c, 123, 123, 123, 123
    ) # TODO: This is wrong hahahha - just fixing tests

    return temp_block
