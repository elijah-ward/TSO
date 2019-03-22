"""
Transformer

Meant to transform external data to one that we will be using throughout the system
"""

from tso.observation.observation_request import ObservationRequest
from tso.observation.cfht_observation_block import CFHTObservationBlock
from astropy import units as u
from astropy.coordinates import SkyCoord


def validate_block(block):
    valid = True

    valid = isinstance(block, CFHTObservationBlock)

    return valid


def block_to_request(block):
    return ObservationRequest(
        observation_id=block.observation_block_id,
        coordinates=block.sky_address, #TODO: Need to convert - unsure of type in DB
        agency_id="Missing", #TODO: GET this information from the CFHT data
        priority=block.priorty,
        remaining_observing_chances=block.remaining_observing_chances,
        observation_duration=block.contiguous_exposure_time_millis
    )


def transform_cfht_observing_blocks(cfht_observing_blocks):
    """
    Convert a list of CFHT blocks to our Internal use

    :param cfht_observing_blocks: The list of blocks to be transformed
    :return:
    """

    return [block_to_request(b) for b in cfht_observing_blocks if validate_block(b)]

