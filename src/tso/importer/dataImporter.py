import mysql.connector
import random
from ..observation.observation_block import ObservationBlock
class dataInput:

    def getObservations():
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="password",
            database="tso",
        )
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM observation")
        lines = cursor.fetchall()

        for line in lines:
            print(line)

print("here")
inputer = dataInput()
dataInput.getObservations()

