import mysql.connector
import random
# Look into this for correct/standard way
from tso.observation.observation_request import ObservationRequest 

class dataInput:

    def getObservations(self):
        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="password",
            database="tso",
        )
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM observation")
        lines = cursor.fetchall()

        observations =[]
        for line in lines:
            print(line)
            singleObservation = ObservationRequest(line[0],(line[1],line[2]),line[3],line[4],line[5], line[6])
            observations.append(singleObservation)

        return observations
    # Get observation blocks with given constraints. 
    # Arguments: Priority -- returning list with include only observations with higher priority. 
    # remaining_observing_chances -- returning list will include only observations with fewer chances left
    # observation_duration_min -- returning list will include only observations with higher duration
    # observation_duration_max -- returning list will include only observations with lower duration
    def getObsevationsWithConstraint(self, minPriority=0, remaining_observing_chances=-1, observation_duration_min=-1, observation_duration_max=-1):
    # def getObsevationsWithConstraint(self,minPriority):
        sql = "SELECT * FROM observation WHERE priority > " + str(minPriority)
        if (remaining_observing_chances > 0):
            sql += " AND remaining_observing_chances < " + str(remaining_observing_chances)
        if (observation_duration_min > 0):
            sql += " AND observation_duration >= " + str(observation_duration_min)
        if (observation_duration_max > 0):
            sql += " AND observation_duration <= " + str(observation_duration_max)

        mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="password",
            database="tso",
        )
        cursor = mydb.cursor()
        cursor.execute(sql)

        lines = cursor.fetchall()

        observations =[]
        for line in lines:
            singleObservation = ObservationRequest(line[0],line[1],line[2],line[3],line[4],line[5])
            observations.append(singleObservation)
        return observations
