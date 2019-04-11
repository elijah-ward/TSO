"""
Transformer

Meant to transform external data to one that we will be using throughout the system
"""

from tso.observation.observation_request import ObservationRequest
from tso.observation.cfht_observation_block import CFHTObservationBlock
from astropy import units as u
from astropy.coordinates import SkyCoord
import json


def validate_block(block):
    """This function will insure that an incoming value is an instance of a CFHT
    observation block. 
    
    Args:
        block (CFHTObservationBlock): An observation request entailed in a CFHT
        block
    
    Returns:
        TYPE: True if argument passed is a CFHTObservationBlock False otherwise
    """
    valid = True

    # Check if the incoming value is an instance of CFHTObservationBlock
    if not isinstance(block, CFHTObservationBlock):
        return False

    # Check if the block has proper sky_address field, which MUST be a comma separated value of floats
    try:
        float(block.sky_address.split(',')[0])
        float(block.sky_address.split(',')[1])
    except ValueError:
        valid = False

    return valid


def block_to_request(block):
    """Summary: Converts a CFHT block into an intrnal data messaget that can be 
    used for scheduling.
    
    Args:
        block (CFHTObservationBlock): Description: Maps a validated 
        CFHTObservationBlock to and Observation request which will eventually be
        used for scheduling
    
    Returns:
        TYPE:ObservationRequest
    """
    mapped_sky_address = SkyCoord(
        ra=float(block.sky_address.split(',')[0]),
        dec=float(block.sky_address.split(',')[1]),
        unit=(u.degree, u.degree),
        frame='icrs'
    )

    return ObservationRequest(
        observation_id=block.observation_block_id,
        coordinates=mapped_sky_address,
        agency_id="Missing", #TODO: GET this information from the CFHT data???
        priority=block.priority,
        remaining_observing_chances=block.remaining_observing_chances,
        duration=(block.contiguous_exposure_time_millis / 1000.0) * u.second,
        exposure_count=block.exposure_count,
        constraint_meta=json.loads(block.observing_block_data)
    )


def transform_cfht_observing_blocks(cfht_observing_blocks):
    """
    Convert a list of CFHT blocks to our Internal use

    :param cfht_observing_blocks: The list of blocks to be transformed
    :return: The list of blocks converted to ObservationRequest if they 
    are valid CFHT blocks. 
    """

    return [block_to_request(b) for b in cfht_observing_blocks if validate_block(b)]

