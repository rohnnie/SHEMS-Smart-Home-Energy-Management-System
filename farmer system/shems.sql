-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Dec 12, 2023 at 04:51 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `shems`
--

-- --------------------------------------------------------

--
-- Table structure for table `adddevice`
--

CREATE TABLE `adddevice` (
  `Location_unit_number` int(5) NOT NULL,
  `bid` int(11) NOT NULL,
  `Type` varchar(50) NOT NULL,
  `pid` int(11) NOT NULL,
  `Product` varchar(100) NOT NULL,
  `Color` text NOT NULL,
  `price` int(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `adddevice`
--

INSERT INTO `adddevice` (`Location_unit_number`, `bid`, `Type`, `pid`, `Product`, `Color`, `price`) VALUES
(101, 1001, 'LED Lights', 2, '26', 'White', 10),
(101, 1001, 'Fridge', 3, '21', 'Black', 250),
(201, 1002, 'AC', 4, '22', 'White', 75),
(201, 1002, 'LED Lights', 5, '26', 'Yellow', 6),
(201, 1002, 'Fan', 6, '23', 'White', 20),
(201, 1002, 'Dishwasher', 7, '25', 'Grey', 200),
(101, 1001, 'Fan', 15, '23', 'Peach', 15),
(101, 1001, 'Dishwasher', 19, '25', 'Grey', 200),
(201, 1002, 'Fan', 1248, 'Usha', 'white', 12000);

-- --------------------------------------------------------

--
-- Table structure for table `consumtionprices`
--

CREATE TABLE `consumtionprices` (
  `cid` int(11) NOT NULL,
  `Zip_Code` int(5) NOT NULL,
  `Timenoted` datetime NOT NULL,
  `Price` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `consumtionprices`
--

INSERT INTO `consumtionprices` (`cid`, `Zip_Code`, `Timenoted`, `Price`) VALUES
(201, 1001, '2022-08-01 12:00:00', 15),
(202, 1002, '2022-08-01 13:30:00', 12),
(203, 1003, '2022-08-15 08:45:00', 18),
(204, 1004, '2022-08-10 20:00:00', 14),
(205, 1005, '2022-08-05 10:15:00', 16),
(206, 1001, '2022-08-20 14:30:00', 20),
(207, 1002, '2023-09-10 18:45:00', 22),
(208, 1003, '2022-09-15 22:00:00', 17),
(209, 1004, '2022-09-02 16:30:00', 19),
(210, 1005, '2022-09-25 07:15:00', 21),
(211, 1005, '2023-09-25 10:15:00', 21);

-- --------------------------------------------------------

--
-- Table structure for table `energydata`
--

CREATE TABLE `energydata` (
  `eid` int(11) NOT NULL,
  `pid` int(5) NOT NULL,
  `timeinterval` datetime NOT NULL,
  `eventlabel` varchar(50) NOT NULL,
  `value` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `energydata`
--

INSERT INTO `energydata` (`eid`, `pid`, `timeinterval`, `eventlabel`, `value`) VALUES
(112, 2, '2022-08-28 11:30:00', 'Switch On', NULL),
(113, 3, '2022-08-28 11:35:00', 'Switch On', NULL),
(114, 6, '2022-08-28 11:35:00', 'Switch On', NULL),
(119, 2, '2022-08-28 16:00:00', 'Energy Use', 0.07),
(120, 3, '2022-08-28 17:14:52', 'Door Opened', NULL),
(121, 3, '2022-08-28 17:29:52', 'Energy Use', 7.80),
(122, 3, '2022-08-28 17:49:36', 'Door Closed', NULL),
(123, 2, '2022-08-28 19:00:00', 'Switch Off', 0.12),
(124, 4, '2022-08-29 10:00:00', 'Switch On', NULL),
(125, 5, '2022-08-29 10:30:00', 'Switch On', NULL),
(127, 7, '2022-08-29 10:35:00', 'Switch On', NULL),
(128, 4, '2022-08-29 10:40:00', 'Temperature Increased', 45.00),
(129, 4, '2022-08-29 11:00:00', 'Energy Use', 1.23),
(130, 4, '2022-08-29 12:00:00', 'Energy Use', 0.99),
(131, 4, '2022-08-29 12:59:45', 'Switch Off', 3.12),
(132, 5, '2022-08-29 15:00:00', 'Energy Use', 0.08),
(136, 5, '2022-08-29 18:00:00', 'Switch Off', 0.20),
(137, 4, '2022-08-29 09:00:00', 'Switch On', NULL),
(141, 4, '2022-08-29 09:40:00', 'Temperature Increased', 45.00),
(142, 4, '2022-08-29 10:00:00', 'Energy Use', 0.66),
(143, 4, '2022-08-29 11:00:00', 'Energy Use', 0.87),
(144, 4, '2022-08-29 11:59:45', 'Switch Off', 2.32),
(150, 4, '2022-09-09 10:00:00', 'Switch On', NULL),
(151, 5, '2022-09-09 10:30:00', 'Switch On', NULL),
(153, 7, '2022-09-09 10:35:00', 'Switch On', NULL),
(154, 4, '2022-09-09 10:40:00', 'Temperature Increased', 45.00),
(155, 4, '2022-09-09 11:00:00', 'Energy Use', 0.87),
(156, 4, '2022-09-09 12:00:00', 'Energy Use', 0.65),
(157, 4, '2022-09-09 12:59:45', 'Switch Off', 2.54),
(158, 5, '2022-09-09 15:00:00', 'Energy Use', 0.04),
(162, 5, '2022-09-09 18:00:00', 'Switch Off', 0.13),
(177, 2, '2022-09-29 08:30:00', 'Switch On', NULL),
(178, 3, '2022-09-29 08:35:00', 'Switch On', NULL),
(179, 6, '2022-09-29 08:35:00', 'Switch On', NULL),
(184, 2, '2022-09-29 13:00:00', 'Energy Use', 0.06),
(185, 3, '2022-09-29 14:14:52', 'Door Opened', NULL),
(186, 3, '2022-09-29 14:29:52', 'Energy Use', 10.20),
(187, 3, '2022-09-29 14:49:36', 'Door Closed', NULL),
(188, 3, '2022-09-29 16:00:00', 'Switch Off', 12.00),
(192, 2, '2022-09-29 20:55:00', 'Switch Off', 0.15);

-- --------------------------------------------------------

--
-- Table structure for table `product`
--

CREATE TABLE `product` (
  `fid` int(11) NOT NULL,
  `type1` varchar(20) NOT NULL,
  `Product_Models` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product`
--

INSERT INTO `product` (`fid`, `type1`, `Product_Models`) VALUES
(21, 'Fridge', 'GE Cafe 400 Refrigerator'),
(22, 'AC', 'LG Smart AC Unit'),
(23, 'Fan', 'Usha'),
(24, 'Oven', 'Google Nest Oven'),
(25, 'Dishwasher', 'Whirlpool XYZ Washer'),
(26, 'LED Lights', 'Solar');

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `rid` int(11) NOT NULL,
  `uid` int(11) NOT NULL,
  `Unit_Number` int(5) NOT NULL,
  `City` varchar(20) NOT NULL,
  `State` varchar(50) NOT NULL,
  `Zip_Code` int(5) NOT NULL,
  `Area` int(5) NOT NULL,
  `Bedrooms` int(2) NOT NULL,
  `Occupants` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`rid`, `uid`, `Unit_Number`, `City`, `State`, `Zip_Code`, `Area`, `Bedrooms`, `Occupants`) VALUES
(1001, 1, 101, 'Boston', 'Massachusetts', 2108, 750, 3, 4),
(1002, 1, 201, 'Orlando', 'Florida', 32789, 1200, 2, 2);
(1003, 2, 103, 'Orlando', 'Florida', 32789, 1200,3,1);

--
-- Triggers `register`
--
DELIMITER $$
CREATE TRIGGER `deletion` BEFORE DELETE ON `register` FOR EACH ROW INSERT INTO trig VALUES(null,OLD.rid,'Location DELETED',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `insertion` AFTER INSERT ON `register` FOR EACH ROW INSERT INTO trig VALUES(null,NEW.rid,'Location Inserted',NOW())
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `updation` AFTER UPDATE ON `register` FOR EACH ROW INSERT INTO trig VALUES(null,NEW.rid,'Location UPDATED',NOW())
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `test`
--

CREATE TABLE `test` (
  `id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `test`
--

INSERT INTO `test` (`id`, `name`) VALUES
(1, 'harshith');

-- --------------------------------------------------------

--
-- Table structure for table `trig`
--

CREATE TABLE `trig` (
  `id` int(11) NOT NULL,
  `fid` varchar(50) NOT NULL,
  `action` varchar(50) NOT NULL,
  `timestamp` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `trig`
--

INSERT INTO `trig` (`id`, `fid`, `action`, `timestamp`) VALUES
(1, '2', 'Location UPDATED', '2021-01-19 23:04:44'),
(2, '2', 'Location DELETED', '2021-01-19 23:04:58'),
(3, '8', 'Location Inserted', '2021-01-19 23:16:52'),
(4, '8', 'Location UPDATED', '2021-01-19 23:17:17'),
(5, '8', 'Location DELETED', '2021-01-19 23:18:54'),
(6, '1001', 'Location Inserted', '2023-12-11 22:13:32'),
(7, '1002', 'Location Inserted', '2023-12-11 22:14:34');

-- --------------------------------------------------------

--
-- Table structure for table `typee`
--

CREATE TABLE `typee` (
  `tid` int(11) NOT NULL,
  `name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `typee`
--

INSERT INTO `typee` (`tid`, `name`) VALUES
(21, 'Fridge'),
(22, 'AC'),
(23, 'Fan'),
(24, 'Oven'),
(25, 'Dishwasher'),
(26, 'LED Lights');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `firstName` varchar(50) NOT NULL,
  `lastName` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(500) NOT NULL,
  `billing` varchar(50) NOT NULL,
  `phone` int(10) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `username`, `firstName`, `lastName`, `email`, `password`,`billing`,`phone`) VALUES
(1, 'Alicecorn', 'Alice', 'Morrison', 'alice@gmail.com', 'scrypt:32768:8:1$KZZ8Rs6m5vpoGnHc$9d17822e37db828cd45e62c4aaaca82f345db00a4db9058bd1b29f27f06ecea225489fa14017b4ef4017f535bc9fc39f39706fefb0155c7fccc6ea91c8f13bba','884 NY', '1234567892');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `adddevice`
--
ALTER TABLE `adddevice`
  ADD PRIMARY KEY (`pid`),
  ADD KEY `register_id` (`bid`);

--
-- Indexes for table `consumtionprices`
--
ALTER TABLE `consumtionprices`
  ADD PRIMARY KEY (`cid`);

--
-- Indexes for table `energydata`
--
ALTER TABLE `energydata`
  ADD PRIMARY KEY (`eid`),
  ADD KEY `product_id` (`pid`);

--
-- Indexes for table `product`
--
ALTER TABLE `product`
  ADD PRIMARY KEY (`fid`);

--
-- Indexes for table `register`
--
ALTER TABLE `register`
  ADD PRIMARY KEY (`rid`),
  ADD KEY `user_id` (`uid`);

--
-- Indexes for table `test`
--
ALTER TABLE `test`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `trig`
--
ALTER TABLE `trig`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `typee`
--
ALTER TABLE `typee`
  ADD PRIMARY KEY (`tid`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `adddevice`
--
ALTER TABLE `adddevice`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1249;

--
-- AUTO_INCREMENT for table `consumtionprices`
--
ALTER TABLE `consumtionprices`
  MODIFY `cid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=212;

--
-- AUTO_INCREMENT for table `energydata`
--
ALTER TABLE `energydata`
  MODIFY `eid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=193;

--
-- AUTO_INCREMENT for table `product`
--
ALTER TABLE `product`
  MODIFY `fid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `register`
--
ALTER TABLE `register`
  MODIFY `rid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1003;

--
-- AUTO_INCREMENT for table `test`
--
ALTER TABLE `test`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `trig`
--
ALTER TABLE `trig`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `typee`
--
ALTER TABLE `typee`
  MODIFY `tid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=27;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `adddevice`
--
ALTER TABLE `adddevice`
  ADD CONSTRAINT `register_id` FOREIGN KEY (`bid`) REFERENCES `register` (`rid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `energydata`
--
ALTER TABLE `energydata`
  ADD CONSTRAINT `product_id` FOREIGN KEY (`pid`) REFERENCES `adddevice` (`pid`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `register`
--
ALTER TABLE `register`
  ADD CONSTRAINT `user_id` FOREIGN KEY (`uid`) REFERENCES `user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
