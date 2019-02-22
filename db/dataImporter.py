import mysql.connector
import random
from src.tso.observation import fixed_constraint, observation_block, dynamic_constraint

class Scheduler:

    def __init__(self):
        self.observation_blocks = []
        self.block_count = 0

    def generate_schedule(self, schedule_horizon):
        print(schedule_horizon)
        self.block_count += 1


class dataInput:

    def __init__(self):
        self.test =0

    def getObservations(self):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="password",
            database="tso",
        )
        cursor = mydb.cursor()
        lines = cursor.execute("SELECT * FROM observation;")

        for line in lines:
            print line


inputer = dataInput()
dataInput.getObservations()

