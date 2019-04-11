"""
Generate Test Data

This is meant to generate test values for use within the Data Importer.
To run there are 2 main modes.
Producing the mock data...
    1. ...as a standalone SQL script (useful for interfacing with the DockerFile
    2. ...as data sent through mysql with the mysql-connector library

You must also prove a variable N as the last arg.
N will determine how many observation blocks will be generated from this module.
"""

import random
import sys
from datetime import datetime
import json
from tso.util import persistence as persistence_util
from configuration import configuration_parser


def clear_database(db, cursor):
    cursor.execute("TRUNCATE TABLE observing_blocks;")
    cursor.execute("TRUNCATE TABLE exposures;")
    db.commit()


def generate_mock_observation_values(n):
    values = []
    for x in range(1, n):
        filters = random.sample(population=['r', 'g', 'b'], k=random.randint(1, 3))
        blob_data = {
            "constraints": {
                'image_quality': -1,
                'sky_background_max': -1,
                'airmass_max': -1,
                'extinction_max': -1,
                'name': -1,
                'h2o_vapor_max': -1,
                'moon_distance': random.uniform(0, 360)
            },
            "filters": filters,
            'program_priority': random.randint(0, 1000)
        }
        values.append({
            'id': x,
            'token': "Token_%s" % x,
            'observing_groups_id': 123,
            'observing_block_data': json.dumps(blob_data),
            'candidate': -1,
            'sky_address': "%f,%f" % (random.uniform(0, 360), random.uniform(-90, 90)),
            'public': -1,
            'active_runid': x,
            'min_qrun_millis': -1,
            'max_qrun_millis': -1,
            'contiguous_exposure_time_millis': random.randint(1000, 18000),
            'priority': random.randint(1, 10000),
            'next_observable_at': -1,
            'unobservable_at': -1,
            'remaining_observing_chances': random.randint(1, 10),
            'created_at': datetime.now(),
            'updated_at': datetime.now(),
            'dirty': -1,
            'version': -1,
            'label': x,
            'program_id': x,

        })

    return values


def generate_mock_exposure_values(n):
    values = []
    unique_obsid = 0
    for obs_block_id in range(1, n):
        for x in range(1, random.randint(1, 7)):
            unique_obsid += 1
            values.append({
                # Let id auto incr
                'token': "Token_%s" % unique_obsid,
                'observing_block_id': obs_block_id,
                'observing_group_id': -1,
                'exposure_data': -1,
                'attributing_agency_id': -1,
                'program_id': -1,
                'status': -1,
                'created_at': datetime.now(),
                'updated_at': datetime.now(),
                'observing_component_id': -1,
                'obsid': unique_obsid,
                'dirty': -1,
                'version': -1,
                'instrument_run_id': -1,
                # Let observed_at auto incr
                })
    return values


observation_sql = "INSERT INTO observing_blocks " \
                  "( id, token, observing_groups_id, observing_block_data, candidate, sky_address, public, " \
                  "active_runid, min_qrun_millis, max_qrun_millis, contiguous_exposure_time_millis, priority, " \
                  "next_observable_at, unobservable_at, remaining_observing_chances, created_at, updated_at, " \
                  "dirty, version, label, program_id )" \
                  "VALUES (%(id)s, %(token)s, %(observing_groups_id)s, %(observing_block_data)s, " \
                  "%(candidate)s, %(sky_address)s, %(public)s, %(active_runid)s, " \
                  "%(min_qrun_millis)s, %(max_qrun_millis)s, %(contiguous_exposure_time_millis)s, %(priority)s, " \
                  "%(next_observable_at)s, %(unobservable_at)s, %(remaining_observing_chances)s, " \
                  "%(created_at)s, %(updated_at)s, %(dirty)s, %(version)s, %(label)s, %(program_id)s)"


exposure_sql = "INSERT INTO exposures "\
               "(token, observing_block_id, observing_group_id, exposure_data, attributing_agency_id,"\
               " program_id, status, created_at, updated_at, observing_component_id, obsid, dirty, "\
               " version, instrument_run_id)"\
               " VALUES (%(token)s, %(observing_block_id)s, %(observing_group_id)s, %(exposure_data)s, " \
               "%(attributing_agency_id)s, %(program_id)s, %(status)s, %(created_at)s, %(updated_at)s, " \
               "%(observing_component_id)s, %(obsid)s, %(dirty)s, %(version)s, %(instrument_run_id)s)"


mode = sys.argv[1]
n_rows = int(sys.argv[2])

if mode == 'file':
    statements = []

    statements.append("# ---------------- Observation Mock Data ----------------")
    for v in generate_mock_observation_values(n_rows):
        statements.append(observation_sql % v)

    statements.append("# ---------------- Exposures Mock Data ----------------")   
    for v in generate_mock_exposure_values(n_rows):
        statements.append(exposure_sql % v) 
    filename = "XXXX_Generated_TSO_Test_Data.sql"
    with open(filename, "w") as f:
        for s in statements:
            f.write(str(s) + "\n")

    print("Generate %s!" % filename)
elif mode == 'sql':
    my_db = persistence_util.get_mysql_connection(
       configuration_parser.parse("tso_config.json").get_database_config())
    my_cursor = my_db.cursor()

    # Ensure that the table is clear
    clear_database(my_db, my_cursor)

    my_cursor.executemany(
        observation_sql,
        generate_mock_observation_values(n_rows)
    )
    my_cursor.executemany(
        exposure_sql,
        generate_mock_exposure_values(n_rows)
    )

    my_db.commit()

    print("Done Inserting Into DB")
else:
    raise NotImplementedError("Unsupported Test Data Generation Mode")

