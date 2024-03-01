-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 01, 2024 at 06:41 AM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sms`
--

-- --------------------------------------------------------

--
-- Table structure for table `scan`
--

CREATE TABLE `scan` (
  `pno` int(11) NOT NULL,
  `Name` varchar(255) DEFAULT NULL,
  `Age` varchar(255) DEFAULT NULL,
  `Sex` varchar(255) DEFAULT NULL,
  `Place` varchar(255) DEFAULT NULL,
  `PhoneNo` varchar(255) DEFAULT NULL,
  `Date` varchar(255) DEFAULT NULL,
  `Rdoc` varchar(255) DEFAULT NULL,
  `Study` varchar(255) DEFAULT NULL,
  `Amount` varchar(255) DEFAULT NULL,
  `Expense` varchar(255) DEFAULT NULL,
  `Total` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `scan`
--

INSERT INTO `scan` (`pno`, `Name`, `Age`, `Sex`, `Place`, `PhoneNo`, `Date`, `Rdoc`, `Study`, `Amount`, `Expense`, `Total`) VALUES
(13, 'Geetha', '34', 'Female', 'Virudhunagar', '9876543211', '26/02/24', 'Dr.RadhaLakshmi', 'X-Ray', '1500', '300', '1800'),
(14, 'Mani', '45', 'Male', 'Chennai', '9834567896', '26/02/24', 'Dr.Priyan', 'MRI', '3000', '700', '3700'),
(15, 'Selvi', '50', 'Female', 'Rajapalayam', '8674456431', '26/02/24', 'Dr.AnbuSelvi', 'CT', '2500', '500', '3000'),
(17, 'Praisy', '40', 'Female', 'Madurai', '9754632161', '26/02/24', 'Dr.RadhaLakshmi', 'HSG', '1200', '200', '1400'),
(34, 'Nagu', '18', 'female', 'Madurai', '8012425684', '28/02/24', 'Dr.AnbuSelvi', 'Ultra Sound', '2000', '500', '2000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `scan`
--
ALTER TABLE `scan`
  ADD PRIMARY KEY (`pno`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `scan`
--
ALTER TABLE `scan`
  MODIFY `pno` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
