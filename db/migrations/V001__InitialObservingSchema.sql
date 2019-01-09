-- MySQL dump 10.13  Distrib 5.7.9, for Win64 (x86_64)
--
-- Host: gloin    Database: observing
-- ------------------------------------------------------
-- Server version	5.5.5-10.1.12-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `agencies`
--

DROP TABLE IF EXISTS `agencies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agencies` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `agency_token` varchar(191) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `letter` char(1) DEFAULT NULL,
  `description` text,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_UNIQUE` (`agency_token`),
  UNIQUE KEY `name` (`name`),
  KEY `letter` (`letter`)
) ENGINE=InnoDB AUTO_INCREMENT=42922 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `agencies_programs`
--

DROP TABLE IF EXISTS `agencies_programs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agencies_programs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `agency_token` varchar(191) NOT NULL,
  `agency_id` bigint(20) NOT NULL,
  `semester_id` bigint(20) NOT NULL,
  `rank` bigint(20) DEFAULT NULL,
  `allocated_time_millis` bigint(20) DEFAULT NULL,
  `runid` varchar(12) DEFAULT NULL,
  `grade` varchar(12) DEFAULT NULL,
  `program_type` varchar(45) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `program_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_UNIQUE` (`agency_token`),
  UNIQUE KEY `runid_UNIQUE` (`runid`),
  KEY `agency_id` (`agency_id`),
  KEY `run_id` (`semester_id`),
  KEY `program_type` (`program_type`),
  KEY `program_id` (`program_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18292 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `agencies_runs`
--

DROP TABLE IF EXISTS `agencies_runs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `agencies_runs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `agency_id` bigint(20) NOT NULL,
  `semester_id` bigint(20) NOT NULL,
  `allocate_time_millis` bigint(20) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `agencies_runs_agency_id_run_id` (`agency_id`,`semester_id`),
  KEY `agency_id` (`agency_id`),
  KEY `run_id` (`semester_id`)
) ENGINE=InnoDB AUTO_INCREMENT=42928 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `clock_logs`
--

DROP TABLE IF EXISTS `clock_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `clock_logs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `clock_log_token` varchar(191) NOT NULL,
  `clock_log_data` blob,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `clock_log_token_UNIQUE` (`clock_log_token`)
) ENGINE=InnoDB AUTO_INCREMENT=4555 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `events`
--

DROP TABLE IF EXISTS `events`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `events` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `event_token` varchar(191) NOT NULL,
  `event_type` varchar(191) NOT NULL,
  `event_id` bigint(20) NOT NULL,
  `event_start_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `event_end_at` timestamp NULL DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_UNIQUE` (`event_token`),
  KEY `event_type` (`event_type`,`event_id`),
  KEY `event_start_at` (`event_start_at`,`event_end_at`),
  KEY `event_end_at` (`event_end_at`)
) ENGINE=InnoDB AUTO_INCREMENT=91618 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `exposures`
--

DROP TABLE IF EXISTS `exposures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exposures` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(191) NOT NULL,
  `observing_block_id` bigint(20) NOT NULL,
  `observing_group_id` bigint(20) NOT NULL,
  `exposure_data` mediumblob,
  `attributing_agency_id` bigint(20) NOT NULL,
  `program_id` bigint(20) NOT NULL,
  `status` varchar(45) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `observing_component_id` bigint(20) DEFAULT NULL,
  `obsid` bigint(20) DEFAULT NULL,
  `dirty` int(11) NOT NULL DEFAULT '0',
  `version` int(11) NOT NULL DEFAULT '0',
  `instrument_run_id` bigint(20) DEFAULT NULL,
  `observed_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_UNIQUE` (`token`),
  UNIQUE KEY `exposures_obsid` (`obsid`),
  KEY `attributing_agency_id` (`attributing_agency_id`),
  KEY `observing_block_id` (`observing_block_id`),
  KEY `observing_group_id` (`observing_group_id`),
  KEY `program_roots_id` (`program_id`),
  KEY `observing_component_id` (`observing_component_id`),
  KEY `dirty` (`dirty`),
  KEY `instrument_run_id` (`instrument_run_id`),
  KEY `observed_at` (`observed_at`),
  KEY `program_id` (`program_id`,`observed_at`)
) ENGINE=InnoDB AUTO_INCREMENT=961426 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `instrument_runs`
--

DROP TABLE IF EXISTS `instrument_runs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `instrument_runs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `semester_id` bigint(20) NOT NULL,
  `instrument` varchar(45) NOT NULL,
  `queue_run` varchar(6) NOT NULL,
  `camera_run` int(2) DEFAULT NULL,
  `start_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `end_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`),
  UNIQUE KEY `instrument_queue_run` (`semester_id`,`queue_run`),
  UNIQUE KEY `instrument_camera_run` (`semester_id`,`instrument`,`camera_run`),
  KEY `queue_run` (`queue_run`)
) ENGINE=InnoDB AUTO_INCREMENT=2602609 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lookups`
--

DROP TABLE IF EXISTS `lookups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lookups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `key0` varchar(45) DEFAULT NULL,
  `key1` varchar(45) DEFAULT NULL,
  `name` varchar(45) DEFAULT NULL,
  `value` varchar(100) DEFAULT NULL,
  `description` mediumtext,
  `lookup_data` blob,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key0_key1_name` (`key0`,`key1`,`name`)
) ENGINE=InnoDB AUTO_INCREMENT=128122 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `metadata`
--

DROP TABLE IF EXISTS `metadata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `metadata` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `key` varchar(191) NOT NULL,
  `data` mediumblob,
  PRIMARY KEY (`id`),
  UNIQUE KEY `metadata_key` (`key`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `observer_logs`
--

DROP TABLE IF EXISTS `observer_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `observer_logs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `observer_log_token` varchar(191) NOT NULL,
  `observer_log_data` mediumblob,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `observer_log_token_UNIQUE` (`observer_log_token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `observing_block_snapshots`
--

DROP TABLE IF EXISTS `observing_block_snapshots`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `observing_block_snapshots` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `observing_block_snapshot_data` mediumblob,
  `observing_block_id` bigint(20) NOT NULL,
  `observing_block_version` int(11) NOT NULL,
  `snapshotable_id` bigint(20) DEFAULT NULL,
  `snapshotable_type` varchar(60) NOT NULL,
  `prune_at` datetime DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `observing_block_snapshot_join` (`observing_block_id`,`snapshotable_type`,`snapshotable_id`),
  KEY `snapshotable_type` (`snapshotable_type`,`snapshotable_id`),
  KEY `prune_at` (`prune_at`)
) ENGINE=InnoDB AUTO_INCREMENT=15349 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `observing_blocks`
--

DROP TABLE IF EXISTS `observing_blocks`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `observing_blocks` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(191) NOT NULL,
  `observing_groups_id` bigint(20) NOT NULL,
  `observing_block_data` blob NOT NULL,
  `candidate` tinyint(4) DEFAULT NULL,
  `sky_address` varchar(191) DEFAULT NULL,
  `public` tinyint(4) DEFAULT NULL,
  `active_runid` bigint(20) DEFAULT NULL,
  `min_qrun_millis` bigint(20) DEFAULT NULL,
  `max_qrun_millis` bigint(20) DEFAULT NULL,
  `contiguous_exposure_time_millis` bigint(20) DEFAULT NULL,
  `priority` bigint(20) DEFAULT NULL,
  `next_observable_at` bigint(20) DEFAULT NULL,
  `unobservable_at` bigint(20) DEFAULT NULL,
  `remaining_observing_chances` bigint(20) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dirty` int(11) NOT NULL DEFAULT '0',
  `version` int(11) NOT NULL DEFAULT '0',
  `label` int(11) NOT NULL,
  `program_id` bigint(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_UNIQUE` (`token`),
  UNIQUE KEY `program_label_unique` (`program_id`,`label`),
  KEY `og_id` (`observing_groups_id`),
  KEY `active_runid` (`active_runid`),
  KEY `dirty` (`dirty`)
) ENGINE=InnoDB AUTO_INCREMENT=341707 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `observing_components`
--

DROP TABLE IF EXISTS `observing_components`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `observing_components` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(191) NOT NULL,
  `observing_blocks_id` bigint(20) NOT NULL,
  `observing_templates_id` bigint(20) NOT NULL,
  `targets_id` bigint(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dirty` int(11) NOT NULL DEFAULT '0',
  `version` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_UNIQUE` (`token`),
  KEY `observing_blocks_id` (`observing_blocks_id`),
  KEY `exposure_templates_id` (`observing_templates_id`),
  KEY `targets_id` (`targets_id`),
  KEY `dirty` (`dirty`)
) ENGINE=InnoDB AUTO_INCREMENT=643225 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `observing_groups`
--

DROP TABLE IF EXISTS `observing_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `observing_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(191) NOT NULL,
  `candidate` tinyint(4) DEFAULT NULL,
  `notify_observers` tinyint(4) DEFAULT NULL,
  `expires_at` bigint(20) DEFAULT NULL,
  `attributing_agency_runid` bigint(20) DEFAULT NULL,
  `program_id` bigint(20) NOT NULL,
  `observing_group_data` blob NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dirty` int(11) NOT NULL DEFAULT '0',
  `version` int(11) NOT NULL DEFAULT '0',
  `label` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_UNIQUE` (`token`),
  UNIQUE KEY `program_label_unique` (`program_id`,`label`),
  KEY `program_roots_id` (`program_id`),
  KEY `attributing_agency_id` (`attributing_agency_runid`),
  KEY `dirty` (`dirty`)
) ENGINE=InnoDB AUTO_INCREMENT=188881 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `observing_templates`
--

DROP TABLE IF EXISTS `observing_templates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `observing_templates` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `token` varchar(191) NOT NULL,
  `observing_template_data` blob,
  `program_id` bigint(20) NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dirty` int(11) NOT NULL DEFAULT '0',
  `version` int(11) NOT NULL DEFAULT '0',
  `label` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_UNIQUE` (`token`),
  UNIQUE KEY `program_label_unique` (`program_id`,`label`),
  KEY `program_roots_id` (`program_id`),
  KEY `dirty` (`dirty`)
) ENGINE=InnoDB AUTO_INCREMENT=891697 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `pi_programs`
--

DROP TABLE IF EXISTS `pi_programs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pi_programs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `usertoken` varchar(191) DEFAULT NULL,
  `program_id` bigint(20) NOT NULL,
  `legacy_userid` varchar(20) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pi_programs_program_id_usertoken` (`program_id`,`usertoken`),
  KEY `usertoken` (`usertoken`),
  KEY `program_roots_id` (`program_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18934 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `programs`
--

DROP TABLE IF EXISTS `programs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `programs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `program_token` varchar(191) NOT NULL,
  `active_runid` varchar(12) DEFAULT NULL,
  `program_data` blob,
  `complete_percentage` double DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `active` tinyint(4) DEFAULT NULL,
  `instrument` varchar(45) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dirty` int(11) NOT NULL DEFAULT '0',
  `version` int(11) NOT NULL DEFAULT '0',
  `reserved_targets` bit(1) DEFAULT b'0',
  `proprietary_period_expires_at` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token_UNIQUE` (`program_token`),
  KEY `active_runid` (`active_runid`),
  KEY `instrument` (`instrument`),
  KEY `dirty` (`dirty`)
) ENGINE=InnoDB AUTO_INCREMENT=18634 DEFAULT CHARSET=utf8 COMMENT='		';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `queues`
--

DROP TABLE IF EXISTS `queues`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `queues` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `queue_token` varchar(191) NOT NULL,
  `queue_data` mediumblob,
  `observation_night` date NOT NULL,
  `label` int(11) NOT NULL DEFAULT '0',
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `queue_token_UNIQUE` (`queue_token`),
  UNIQUE KEY `observation_night_label_unique` (`observation_night`,`label`)
) ENGINE=InnoDB AUTO_INCREMENT=739 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `semesters`
--

DROP TABLE IF EXISTS `semesters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `semesters` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `semester` varchar(3) DEFAULT NULL,
  `start_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `end_at` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  `proprietary_period_end_date` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `semester` (`semester`)
) ENGINE=InnoDB AUTO_INCREMENT=317140 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `tar1`
--

DROP TABLE IF EXISTS `tar1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tar1` (
  `id` bigint(20) NOT NULL DEFAULT '0',
  `agency_id` bigint(20) NOT NULL,
  `run_id` bigint(20) NOT NULL,
  `allocate_time_millis` bigint(20) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `target_identities`
--

DROP TABLE IF EXISTS `target_identities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `target_identities` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `canonical_name` varchar(191) NOT NULL,
  `name` varchar(120) DEFAULT NULL,
  `ra` float NOT NULL,
  `dec` float NOT NULL,
  `pm_ra` float NOT NULL,
  `pm_dec` float NOT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `target_identities` (`canonical_name`)
) ENGINE=InnoDB AUTO_INCREMENT=183031 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `target_reservations`
--

DROP TABLE IF EXISTS `target_reservations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `target_reservations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `target_identities_id` bigint(20) NOT NULL,
  `target_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `target_reservations_id` (`id`),
  KEY `target_reservations_join_ids` (`target_id`,`target_identities_id`),
  KEY `target_reservations_target_id` (`target_id`),
  KEY `target_reservations_target_identities_id` (`target_identities_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `targets`
--

DROP TABLE IF EXISTS `targets`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `targets` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `target_data` mediumblob,
  `notify_observers` tinyint(4) DEFAULT NULL,
  `program_id` bigint(20) NOT NULL,
  `token` varchar(191) NOT NULL,
  `name` varchar(191) DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `dirty` int(11) NOT NULL DEFAULT '0',
  `version` int(11) NOT NULL DEFAULT '0',
  `label` int(11) NOT NULL,
  `target_identities_id` bigint(20) DEFAULT NULL,
  `target_identity_angular_distance` float DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `token` (`token`),
  UNIQUE KEY `program_label_unique` (`program_id`,`label`),
  KEY `program_roots_id` (`program_id`),
  KEY `dirty` (`dirty`)
) ENGINE=InnoDB AUTO_INCREMENT=848797 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `weather_logs`
--

DROP TABLE IF EXISTS `weather_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `weather_logs` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `weather_log_token` varchar(191) NOT NULL,
  `weather_log_data` mediumblob,
  `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `weather_log_token_UNIQUE` (`weather_log_token`)
) ENGINE=InnoDB AUTO_INCREMENT=14884 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-12-03  9:03:33
