DROP DATABASE IF EXISTS tso;
CREATE DATABASE tso;
USE tso;
DROP TABLE IF EXISTS `agencies`;
CREATE TABLE agencies (
  id bigint(20) NOT NULL,
  name varchar(45) DEFAULT NULL,
  PRIMARY KEY (id)
);

DROP TABLE IF EXISTS observation;

CREATE TABLE observation (
  id bigint(20) NOT NULL ,
  sky_address varchar(191) NOT NULL,
  agency_id bigint(20) NOT NULL,
  priority bigint(10) NOT NULL,
  remaining_observing_chances integer(10) NOT NULL,
  observation_duration bigint(20) NOT NULL,
  PRIMARY KEY (id)
);

