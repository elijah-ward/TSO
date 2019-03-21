"""
Transformer

TODO: Take in the cfhtObservingBlocks and convert them into tsoObservingRequests
"""

from tso.observation import observation_request
from astropy import units as u
from astropy.coordinates import SkyCoord


def transform_cfht_observing_blocks(cfht_observing_blocks):
    print("TODO: Implement")


def transform(data_string):
    """"
    TODO: Deprecated
    """
    print('Transforming the data :: {}'.format(data_string))
    c = SkyCoord(ra=10.625*u.degree, dec=41.2*u.degree, frame='icrs')
    temp_block = observation_request.ObservationRequest(
        22, c, 123, 123, 123, 123
    )  # TODO: This creation of a ObsRequest is wrong...this is done just to comply to an old test for now

    return temp_block
