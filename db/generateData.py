import mysql.connector
import random

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="password",
  database="tso",
)

mycursor = mydb.cursor()

vals = []
# generate agencies
for x in range (0, 100):
    name = 'Agency' + str(x)
    id = x
    vals.append((id, name))

sql = "INSERT INTO agencies (id, name) VALUES (%s, %s)" 
mycursor.executemany(sql, vals)

# generate observations
# template skycoord: "10.625, 41.2, frame='icrs', unit='deg'"
vals = []
for x in range (0,1000):
    id = x
    right_ascension = (random.randint(0, 360000)/1000)
    declination = (random.randint(0, 360000)/1000)
    agency_id = random.randint(1, 100)
    priority = random.randint(1, 100)
    remaining_observing_chances = random.randint(1, 10)
    observation_duration = random.randint(100, 18000)
    vals.append((id, right_ascension, declination, agency_id, priority, remaining_observing_chances, observation_duration))

sql = "INSERT INTO observation (id, right_ascension, declination, agency_id, priority, remaining_observing_chances, observation_duration) VALUES (%s, %s, %s, %s, %s, %s, %s)" 
mycursor.executemany(sql, vals)

mydb.commit()
