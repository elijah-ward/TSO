"""
Generate Test Data

Two main uses.
Producing the mock data...
    1. ...as a standalone SQL script (useful for interfacing with the DockerFile
    2. ...as data sent through mysql with the mysql-connector library
"""

import random
import sys
from tso.util import persistence as persistence_util


def generate_mock_agencies_values():
    values = []
    for x in range (0, 100):
        name = 'Agency' + str(x)
        _id = x
        values.append((_id, name))

    return values


def generate_mock_observation_values():
    values = []
    for x in range(0, 1000):
        _id = x
        skycoord = "10.625, 41.2, frame='icrs', unit='deg'"
        agency_id = random.randint(1, 100)
        priority = random.randint(1, 100)
        remaining_observing_chances = random.randint(1, 10)
        observation_duration = random.randint(100, 18000)
        values.append((_id, skycoord, agency_id, priority, remaining_observing_chances, observation_duration))

    return values


agencies_sql = "INSERT INTO agencies (id, name) VALUES (%s, %s);"
observation_sql = "INSERT INTO observation " \
                  "(id, sky_address, agency_id, priority, remaining_observing_chances, observation_duration) " \
                  "VALUES (%s, %s, %s, %s, %s, %s);"

mode = sys.argv[1]

if mode == 'file':
    statements = []

    statements.append("# ---------------- Agencies Mock Data ----------------")
    for v in generate_mock_agencies_values():
        statements.append(agencies_sql % v)

    statements.append("# ---------------- Observation Mock Data ----------------")
    for v in generate_mock_observation_values():
        statements.append(observation_sql % v)

    filename = "XXXX_Generated_TSO_Test_Data.sql"
    with open(filename, "w") as f:
        for s in statements:
            f.write(str(s) + "\n")

    print("Generate %s!" % filename)
elif mode == 'sql':
    my_db = persistence_util.get_mysql_connection()
    my_cursor = my_db.cursor()

    my_cursor.executemany(
        agencies_sql,
        generate_mock_agencies_values()
    )
    my_cursor.executemany(
        observation_sql,
        generate_mock_observation_values()
    )

    my_db.commit()
else:
    raise NotImplementedError("Unsupported Test Data Generation Mode")

