"""
connect.py

An example of connecting to the tso DB from the mysql.connector library
"""


import mysql.connector
# Connect WITH mysql -h 127.0.0.1 -u root -P 3306 -p

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE IF EXISTS tso")
mycursor.execute("CREATE DATABASE tso")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="password",
  database="tso"
)

mycursor = mydb.cursor()

mycursor.execute("DROP TABLE IF EXISTS `observing_blocks`")
mycursor.execute("CREATE TABLE `observing_blocks` ( `id` bigint(20) NOT NULL AUTO_INCREMENT, `token` varchar(191) NOT NULL,  `observing_groups_id` bigint(20) NOT NULL,  `observing_block_data` blob NOT NULL,  `candidate` tinyint(4) DEFAULT NULL,  `sky_address` varchar(191) DEFAULT NULL,  `public` tinyint(4) DEFAULT NULL,  `active_runid` bigint(20) DEFAULT NULL,  `min_qrun_millis` bigint(20) DEFAULT NULL,  `max_qrun_millis` bigint(20) DEFAULT NULL,  `contiguous_exposure_time_millis` bigint(20) DEFAULT NULL,  `priority` bigint(20) DEFAULT NULL,  `next_observable_at` bigint(20) DEFAULT NULL,  `unobservable_at` bigint(20) DEFAULT NULL,  `remaining_observing_chances` bigint(20) DEFAULT NULL,  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  `dirty` int(11) NOT NULL DEFAULT '0',  `version` int(11) NOT NULL DEFAULT '0',  `label` int(11) NOT NULL,  `program_id` bigint(20) DEFAULT NULL,  PRIMARY KEY (`id`),  UNIQUE KEY `token_UNIQUE` (`token`),  UNIQUE KEY `program_label_unique` (`program_id`,`label`),  KEY `og_id` (`observing_groups_id`),  KEY `active_runid` (`active_runid`),  KEY `dirty` (`dirty`))")

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
