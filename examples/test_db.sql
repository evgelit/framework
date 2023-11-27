-- Adminer 4.8.1 MySQL 8.0.35-0ubuntu0.20.04.1 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `attribute`;
CREATE TABLE `attribute` (
  `attribute_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `attribute_type` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `source_model` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`attribute_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `attribute` (`attribute_id`, `name`, `attribute_type`, `source_model`) VALUES
(2,	'first_name',	'varchar',	'None'),
(3,	'last_name',	'varchar',	NULL),
(4,	'dob',	'varchar',	NULL),
(5,	'test1',	'varchar',	NULL),
(7,	'test3',	'varchar',	NULL),
(8,	'test4',	'varchar',	NULL),
(9,	'test5',	'numerical',	NULL),
(10,	'test6',	'varchar',	NULL),
(11,	'test7',	'varchar',	NULL),
(12,	'test8',	'varchar',	NULL),
(13,	'test9',	'varchar',	NULL),
(14,	'test10',	'varchar',	NULL),
(15,	'test11',	'varchar',	NULL),
(16,	'test12',	'numerical',	NULL),
(17,	'test13',	'numerical',	NULL),
(18,	'test14',	'numerical',	NULL),
(19,	'test15',	'numerical',	NULL),
(20,	'test16',	'numerical',	NULL),
(21,	'test17',	'numerical',	NULL),
(22,	'test18',	'numerical',	NULL),
(23,	'test19',	'numerical',	NULL),
(24,	'test20',	'varchar',	NULL);

DROP TABLE IF EXISTS `attribute_set`;
CREATE TABLE `attribute_set` (
  `attribute_set_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  PRIMARY KEY (`attribute_set_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `attribute_set` (`attribute_set_id`, `name`) VALUES
(1,	'Test attribute set'),
(2,	'Test attribute set 1');

DROP TABLE IF EXISTS `attribute_set_attribute_id`;
CREATE TABLE `attribute_set_attribute_id` (
  `attribute_set_id` int NOT NULL,
  `attribute_id` int NOT NULL,
  KEY `attribute_id` (`attribute_id`),
  KEY `attribute_set_id` (`attribute_set_id`),
  CONSTRAINT `attribute_set_attribute_id_ibfk_2` FOREIGN KEY (`attribute_id`) REFERENCES `attribute` (`attribute_id`) ON DELETE CASCADE,
  CONSTRAINT `attribute_set_attribute_id_ibfk_4` FOREIGN KEY (`attribute_set_id`) REFERENCES `attribute_set` (`attribute_set_id`) ON DELETE CASCADE ON UPDATE RESTRICT
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `attribute_set_attribute_id` (`attribute_set_id`, `attribute_id`) VALUES
(1,	2),
(1,	3),
(1,	5),
(1,	7),
(1,	8),
(1,	9),
(1,	10),
(2,	8),
(2,	9),
(2,	10);

-- 2023-11-27 13:03:02
