"""
Data Importer

Allows importing TSO data from TSO persistence.
"""

from tso.observation.cfht_observation_block import CFHTObservationBlock
from tso.util import persistence as persistence_util
from sys import maxsize as MAX_SIZE
import json


def convert_to_cfht(
    values,
    max_program_priority=0,
    exposure_count_data={}
):
    observation_blocks = []
    for line_values in values:

        new_block = CFHTObservationBlock(**line_values)

        blob_data = json.loads(new_block.observing_block_data)
        # Filter only those blocks that comply with the program priority
        if int(blob_data["program_priority"]) <= int(max_program_priority):

            # For those blocks that are valid, set their exposure count
            new_block.exposure_count = exposure_count_data.get(new_block.observation_block_id)
            observation_blocks.append(
                new_block
            )

    return observation_blocks


def get_all_observations(db_config=None):
    """
    Retrieve all observation_blocks found in persistence.
    Potentially dangerous if a large amount of entries exist

    :return: All observations in TSO persistence
    """

    if db_config is None:
        raise RuntimeError("Error :: Cannot import without database configuration")

    my_db = persistence_util.get_mysql_connection(db_config)
    cursor = my_db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM observing_blocks;")

    return convert_to_cfht(
        cursor.fetchall(),
        0,
        get_exposure_counts_per_observation_id(db_config)
    )


def get_observations_with_args(db_config=None, **kwargs):
    if db_config is None:
        raise RuntimeError("Error :: Cannot import without database configuration")

    # Remove all the keys that are none
    non_empty_values = {}
    for key, value in kwargs.items():
        if value is not None:
            non_empty_values[key] = value

    return get_observations(
        db_config=db_config,
        #TODO: default MAX_PRIORITY params from some value in config
        max_observation_priority=non_empty_values.get("max_observation_priority", 0),
        max_program_priority=non_empty_values.get("max_program_priority", 0),
        remaining_observing_chances=non_empty_values.get("remaining_observing_chances", -1),
        observation_duration_min=non_empty_values.get("observation_duration_min", -1),
        observation_duration_max=non_empty_values.get("observation_duration_max", MAX_SIZE)
    )


def get_observations(
    db_config=None,
    max_observation_priority=0,
    max_program_priority=0,
    remaining_observing_chances=-1,
    observation_duration_min=-1,
    observation_duration_max=MAX_SIZE
):
    """
    Get CFHT observation blocks with given constraints.
    The default values allow for the maximal amount of requests to be returned,
    or in other words, the default values provide the same functionality
    """
    if db_config is None:
        raise RuntimeError("Error :: Cannot import without database configuration")

    sql = "SELECT * FROM observing_blocks WHERE priority <= %s;" % str(max_observation_priority)
    if remaining_observing_chances > 0:
        sql += " AND remaining_observing_chances < " + str(remaining_observing_chances)
    if observation_duration_min > 0:
        sql += " AND contiguous_exposure_time_millis >= " + str(observation_duration_min)
    if observation_duration_max > 0:
        sql += " AND contiguous_exposure_time_millis <= " + str(observation_duration_max)

    my_db = persistence_util.get_mysql_connection(db_config)
    cursor = my_db.cursor(dictionary=True)
    cursor.execute(sql)

    return convert_to_cfht(
        cursor.fetchall(),
        max_observation_priority,
        get_exposure_counts_per_observation_id(db_config)
    )


def get_exposure_counts_per_observation_id(db_config=None):
    """
    Get Exposure Counts Per Observation Id

    :return dict with schema -> { observationId: exposureCount }
    """

    if db_config is None:
        raise RuntimeError("Error :: Cannot import without database configuration")

    my_db = persistence_util.get_mysql_connection(db_config)
    cursor = my_db.cursor(dictionary=True)
    cursor.execute("SELECT observing_block_id, count(*) AS exposure_count FROM exposures GROUP BY observing_block_id;")
    raw_dict = cursor.fetchall()

    final = {}
    for sub in raw_dict:
        final[sub['observing_block_id']] = sub['exposure_count']

    return final


