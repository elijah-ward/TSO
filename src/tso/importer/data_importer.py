"""
Data Importer

Allows importing TSO data from TSO persistence.
"""

from tso.observation.observation_block import ObservationBlock
from tso.util import persistence as persistence_util


def get_all_observations():
    """
    Retrieve all observations found in persistence.
    Potentially dangerous if a large amount of entries exist

    :return: All observations in TSO persistence
    """

    my_db = persistence_util.get_mysql_connection()
    cursor = my_db.cursor()
    cursor.execute("SELECT * FROM observation;")
    lines = cursor.fetchall()

    observations = []
    for line in lines:
        observations.append(
            ObservationBlock(line[0], line[1], line[2], line[3], line[4], line[5])
        )

    return observations


def get_observations_with_constraint(
    min_priority=0, remaining_observing_chances=-1, observation_duration_min=-1, observation_duration_max=-1
):
    """
    Get observation blocks with given constraints.

    :param min_priority:                returning list with include only observations with higher priority.
    :param remaining_observing_chances: returning list will include only observations with fewer chances left
    :param observation_duration_min:    returning list will include only observations with higher duration
    :param observation_duration_max:    returning list will include only observations with lower duration
    :return: The Observation Blocks found
    """

    sql = "SELECT * FROM observation WHERE priority > %s;" % str(min_priority)
    if remaining_observing_chances > 0:
        sql += " AND remaining_observing_chances < " + str(remaining_observing_chances)
    if observation_duration_min > 0:
        sql += " AND observation_duration >= " + str(observation_duration_min)
    if observation_duration_max > 0:
        sql += " AND observation_duration <= " + str(observation_duration_max)

    my_db = persistence_util.get_mysql_connection()
    cursor = my_db.cursor()
    cursor.execute(sql)

    lines = cursor.fetchall()

    observations = []
    for line in lines:
        observations.append(
            ObservationBlock(line[0], line[1], line[2], line[3], line[4], line[5])
        )
    return observations
