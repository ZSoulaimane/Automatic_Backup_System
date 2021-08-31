-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 31, 2021 at 08:38 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `newbase`
--

-- --------------------------------------------------------

--
-- Table structure for table `backup-cron`
--

CREATE TABLE `backup-cron` (
  `id_back` int(11) NOT NULL,
  `id_cron` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `back_up`
--

CREATE TABLE `back_up` (
  `id_backup` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `type` varchar(200) NOT NULL,
  `server_name` varchar(200) DEFAULT NULL,
  `minute` varchar(11) DEFAULT NULL,
  `hour` varchar(11) DEFAULT NULL,
  `day_Month` varchar(11) DEFAULT NULL,
  `Month` varchar(11) DEFAULT NULL,
  `day_Week` varchar(11) DEFAULT NULL,
  `comments` varchar(200) DEFAULT NULL,
  `status` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `crontab`
--

CREATE TABLE `crontab` (
  `id_crontab` int(11) NOT NULL,
  `execution_time` varchar(200) NOT NULL,
  `download` varchar(200) DEFAULT NULL,
  `comment` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `database-siteweb`
--

CREATE TABLE `database-siteweb` (
  `id_db` int(11) NOT NULL,
  `site_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_nopad_ci;

-- --------------------------------------------------------

--
-- Table structure for table `databaseinfo`
--

CREATE TABLE `databaseinfo` (
  `id_db` int(11) NOT NULL,
  `Path` varchar(11) NOT NULL,
  `db_name` varchar(200) NOT NULL,
  `db_username` varchar(200) NOT NULL,
  `db_password` varchar(200) NOT NULL,
  `db_host` int(11) NOT NULL,
  `Status` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `errormsg`
--

CREATE TABLE `errormsg` (
  `id_error` int(11) NOT NULL,
  `msg` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `notification`
--

CREATE TABLE `notification` (
  `id_notification` int(11) NOT NULL,
  `message` varchar(200) NOT NULL,
  `date` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `notifiying`
--

CREATE TABLE `notifiying` (
  `id_cron` int(11) NOT NULL,
  `id_notification` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `onesitbackup`
--

CREATE TABLE `onesitbackup` (
  `id_website` int(11) NOT NULL,
  `id_backup` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `pinging`
--

CREATE TABLE `pinging` (
  `site_id` int(11) NOT NULL,
  `pinging_status` varchar(200) NOT NULL,
  `id_message` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `server-site`
--

CREATE TABLE `server-site` (
  `server` int(11) NOT NULL,
  `siteweb` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_nopad_ci;

-- --------------------------------------------------------

--
-- Table structure for table `server-user`
--

CREATE TABLE `server-user` (
  `ids_user` int(11) NOT NULL,
  `ids_server` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_nopad_ci;

-- --------------------------------------------------------

--
-- Table structure for table `serverinfo`
--

CREATE TABLE `serverinfo` (
  `id_server` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `host` varchar(200) NOT NULL,
  `username` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `port` int(11) NOT NULL,
  `path` varchar(200) NOT NULL,
  `status` varchar(200) NOT NULL,
  `saving_date` date DEFAULT NULL,
  `last_saving_date` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `sitewebinfo`
--

CREATE TABLE `sitewebinfo` (
  `site_id` int(11) NOT NULL,
  `server_name` varchar(200) DEFAULT NULL,
  `site_name` varchar(200) DEFAULT NULL,
  `url_website` varchar(200) NOT NULL,
  `saving_date` date DEFAULT NULL,
  `last_saving_date` date DEFAULT NULL,
  `directory_path` varchar(200) NOT NULL,
  `webstatus` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id_user` int(11) NOT NULL,
  `firstname` varchar(200) NOT NULL,
  `lastname` varchar(200) NOT NULL,
  `password` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `company_h` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `backup-cron`
--
ALTER TABLE `backup-cron`
  ADD KEY `fk` (`id_back`),
  ADD KEY `fk2` (`id_cron`);

--
-- Indexes for table `back_up`
--
ALTER TABLE `back_up`
  ADD PRIMARY KEY (`id_backup`);

--
-- Indexes for table `crontab`
--
ALTER TABLE `crontab`
  ADD PRIMARY KEY (`id_crontab`);

--
-- Indexes for table `database-siteweb`
--
ALTER TABLE `database-siteweb`
  ADD KEY `foreign` (`id_db`),
  ADD KEY `foreign1` (`site_id`);

--
-- Indexes for table `databaseinfo`
--
ALTER TABLE `databaseinfo`
  ADD PRIMARY KEY (`id_db`);

--
-- Indexes for table `errormsg`
--
ALTER TABLE `errormsg`
  ADD PRIMARY KEY (`id_error`);

--
-- Indexes for table `notification`
--
ALTER TABLE `notification`
  ADD PRIMARY KEY (`id_notification`);

--
-- Indexes for table `notifiying`
--
ALTER TABLE `notifiying`
  ADD KEY `fk` (`id_cron`),
  ADD KEY `fk_backup` (`id_notification`);

--
-- Indexes for table `onesitbackup`
--
ALTER TABLE `onesitbackup`
  ADD KEY `foreigns1` (`id_backup`),
  ADD KEY `foreign2` (`id_website`);

--
-- Indexes for table `pinging`
--
ALTER TABLE `pinging`
  ADD KEY `id_site_fk` (`site_id`),
  ADD KEY `fk` (`id_message`);

--
-- Indexes for table `server-site`
--
ALTER TABLE `server-site`
  ADD KEY `foreign_keys` (`server`),
  ADD KEY `foreign_keys1` (`siteweb`);

--
-- Indexes for table `server-user`
--
ALTER TABLE `server-user`
  ADD KEY `foreign_key` (`ids_user`),
  ADD KEY `foreign_key1` (`ids_server`);

--
-- Indexes for table `serverinfo`
--
ALTER TABLE `serverinfo`
  ADD PRIMARY KEY (`id_server`);

--
-- Indexes for table `sitewebinfo`
--
ALTER TABLE `sitewebinfo`
  ADD PRIMARY KEY (`site_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `back_up`
--
ALTER TABLE `back_up`
  MODIFY `id_backup` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `crontab`
--
ALTER TABLE `crontab`
  MODIFY `id_crontab` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `errormsg`
--
ALTER TABLE `errormsg`
  MODIFY `id_error` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `serverinfo`
--
ALTER TABLE `serverinfo`
  MODIFY `id_server` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sitewebinfo`
--
ALTER TABLE `sitewebinfo`
  MODIFY `site_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `backup-cron`
--
ALTER TABLE `backup-cron`
  ADD CONSTRAINT `fk` FOREIGN KEY (`id_back`) REFERENCES `back_up` (`id_backup`),
  ADD CONSTRAINT `fk2` FOREIGN KEY (`id_cron`) REFERENCES `crontab` (`id_crontab`);

--
-- Constraints for table `database-siteweb`
--
ALTER TABLE `database-siteweb`
  ADD CONSTRAINT `foreign` FOREIGN KEY (`id_db`) REFERENCES `databaseinfo` (`id_db`),
  ADD CONSTRAINT `foreign1` FOREIGN KEY (`site_id`) REFERENCES `sitewebinfo` (`site_id`);

--
-- Constraints for table `notifiying`
--
ALTER TABLE `notifiying`
  ADD CONSTRAINT `fks1` FOREIGN KEY (`id_cron`) REFERENCES `crontab` (`id_crontab`),
  ADD CONSTRAINT `fks2` FOREIGN KEY (`id_notification`) REFERENCES `notification` (`id_notification`);

--
-- Constraints for table `onesitbackup`
--
ALTER TABLE `onesitbackup`
  ADD CONSTRAINT `foreign2` FOREIGN KEY (`id_website`) REFERENCES `sitewebinfo` (`site_id`),
  ADD CONSTRAINT `foreigns1` FOREIGN KEY (`id_backup`) REFERENCES `back_up` (`id_backup`);

--
-- Constraints for table `pinging`
--
ALTER TABLE `pinging`
  ADD CONSTRAINT `fke1` FOREIGN KEY (`id_message`) REFERENCES `errormsg` (`id_error`),
  ADD CONSTRAINT `fke2` FOREIGN KEY (`site_id`) REFERENCES `sitewebinfo` (`site_id`);

--
-- Constraints for table `server-site`
--
ALTER TABLE `server-site`
  ADD CONSTRAINT `foreign_keys` FOREIGN KEY (`server`) REFERENCES `serverinfo` (`id_server`),
  ADD CONSTRAINT `foreign_keys1` FOREIGN KEY (`siteweb`) REFERENCES `sitewebinfo` (`site_id`);

--
-- Constraints for table `server-user`
--
ALTER TABLE `server-user`
  ADD CONSTRAINT `foreign_key` FOREIGN KEY (`ids_user`) REFERENCES `user` (`id_user`),
  ADD CONSTRAINT `foreign_key1` FOREIGN KEY (`ids_server`) REFERENCES `serverinfo` (`id_server`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
