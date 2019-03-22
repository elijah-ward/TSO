"""
Data Importer

Allows importing TSO data from TSO persistence.
"""

from tso.observation.cfht_observation_block import CFHTObservationBlock
from tso.util import persistence as persistence_util
from sys import maxsize as MAX_SIZE


def convert_to_cfht(values):
    observation_blocks = []
    for line_values in values:
        observation_blocks.append(
            CFHTObservationBlock(**line_values)
        )

    return observation_blocks


def get_all_observations():
    """
    Retrieve all observation_blocks found in persistence.
    Potentially dangerous if a large amount of entries exist

    :return: All observations in TSO persistence
    """

    my_db = persistence_util.get_mysql_connection()
    cursor = my_db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM observing_blocks;")

    return convert_to_cfht(
        cursor.fetchall()
    )


def get_observations(
    min_priority=0,
    remaining_observing_chances=-1,
    observation_duration_min=-1,
    observation_duration_max=MAX_SIZE
):
    """
    Get CFHT observation blocks with given constraints.
    The default values allow for the maximal amount of requests to be returned,
    or in other words, the default values provide the same functionality

    :param min_priority:                returning list with include only observations with higher priority.
    :param remaining_observing_chances: returning list will include only observations with fewer chances left
    :param observation_duration_min:    returning list will include only observations with higher duration
    :param observation_duration_max:    returning list will include only observations with lower duration
    :return: The Observation Blocks found
    """

    sql = "SELECT * FROM observing_blocks WHERE priority > %s;" % str(min_priority)
    if remaining_observing_chances > 0:
        sql += " AND remaining_observing_chances < " + str(remaining_observing_chances)
    if observation_duration_min > 0:
        sql += " AND contiguous_exposure_time_millis >= " + str(observation_duration_min)
    if observation_duration_max > 0:
        sql += " AND contiguous_exposure_time_millis <= " + str(observation_duration_max)

    # This is the data that Eli says we need from CFHT
    # number of exposures :: this might not be within the observing blocks, but in another table
    # exposure time :: As above, I think this is contiguous_exposure_time_millis
    # read out time :: Not sure where this is

    my_db = persistence_util.get_mysql_connection()
    cursor = my_db.cursor(dictionary=True)
    cursor.execute(sql)

    return convert_to_cfht(
        cursor.fetchall()
    )

