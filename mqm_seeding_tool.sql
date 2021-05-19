-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 19, 2021 at 05:31 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mqm_seeding_tool`
--

-- --------------------------------------------------------

--
-- Table structure for table `clone`
--

CREATE TABLE `clone` (
  `id` int(11) NOT NULL,
  `api_id` int(11) DEFAULT NULL,
  `api_hash` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `username` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `clone`
--

INSERT INTO `clone` (`id`, `api_id`, `api_hash`, `username`, `phone`) VALUES
(1, 3845192, 'ee3f76456f539941ef8c223d793c1187', 'Esmond Wise', '84325976595'),
(2, 3326683, 'c54dfc6033d59f572a21000728991468', 'Randall Steele', '84869668594'),
(3, 3937949, '94bf170cea89644bf4bc31f47108f390', 'Theodore Webb', '84369805473'),
(4, 3899170, '60161bb54d9068dda563e9caec9768c9', 'Bruno Tenny', '84374127674'),
(5, 3058516, 'a1822fd9138786cc42d621c13db24901', 'Rachel Lowe', '84368867049'),
(6, 3343349, 'a928562f49ced1e618a4619a1cbd9759', 'Miriam Yates', '84375987705'),
(7, 3564149, '9913e056d6c1fdeb99537a1a2efb5d14', 'Kara George', '84363845419'),
(8, 3890124, '17f0ff3ad5bdd5b763248419f68f6f00', 'Colin Lawson', '84372861781'),
(9, 3270938, '86e0af9dfbe558659b275c8f02d6222d', 'Cade Lee', '84375608814'),
(10, 2126667, '50b9db49a24ec0fc54f534998ec7f8d3', 'Derek Newman', '84355925914'),
(11, 2485366, 'ec8c75a71e74e1707968d5c9634a9ba7', 'Andy Robin', '84382847319'),
(12, 2206963, '909c311a00ad464a0d82424aea0f4d73', 'Yolanda Larson', '84359016827'),
(13, 3870880, 'b1e97f1f83524c8bbb3cd5008b876cb7', 'Una Riley', '84389212394'),
(14, 2683901, '6609f630319449a1c78a4f8436bd6b05', 'Jim Chapman', '84396253864'),
(15, 3257283, 'c53d2022da392ddb4594c4cac24f09d3', 'Myung Morales', '84366735490'),
(16, 3611832, '137a07b7be751ba04ce2ed44d8b77498', 'Wei Jie', '84366595278'),
(17, 3239558, 'f1de35314720cfc6fcf34bbd02975ae4', 'Su Meili', '84342834178'),
(18, 3329695, 'cce89af40c1b968d3bc99a9c5c20fcff', 'Lai Zian', '84352709778'),
(19, 3185539, '64195fbd53f2e93a45c2f7b539452434', 'Dong Zongying', '84396401748'),
(20, 2281228, 'e2d47479249149309e60db0c073a2a56', '黄茂德', '84378834954'),
(21, 3811763, '1be5d46e6f4eeca117e5a805d321defb', '何致功', '84393342971'),
(22, 3663039, 'c3f2f2e6ab791c5ad6479123085d7309', '侯煜月', '84369544960'),
(23, 3546062, '4862cb714d2a9cfe11ce4a313f0d1a10', 'Công Thương', '84398298480'),
(24, 3103389, '08ad2d3fb9da8631eb2890a5896c3e14', 'Văn Cường', '84376012064'),
(25, 3743318, '42804852d202dc2cd01e2e260636f6e1', 'Hoàng Văn Hóa', '84379872519'),
(26, 2020572, '4ab7f4b0effea15b0229f18b2fc2a8de', 'Thúy Kiều', '84375696109'),
(27, 3492886, '3e202eaebe8fb317859fc220e16a2c74', 'Bùi Thị Huyền', '84379877432'),
(28, 3090444, 'd9815b9e9afda43ea26738f9000c2439', 'Khánh Huyền', '84377289729'),
(29, 2290211, 'b28f673a1ee7065b324a14be3b33bdf7', 'Trần Thị Quỳnh Diệp', '84348796301'),
(30, 3437296, '0ad3454f0106521940cc4f9b5d2be273', 'Hùng Dũng', '84923866874'),
(31, 3068248, '085ed9e57d7ba5f38e68715194fc3728', 'Karon Snider', '84382075692'),
(32, 3991066, 'ae7b851cccbe2ef433ef508d99c1d750', 'Hoàng Ngọc Dũng', '84386370560'),
(33, 3094510, '0d29cc25c2617de45962bf572d59bad6', 'Nguyễn Nhi', '84329983642'),
(34, 3056391, 'a90fc24ebbc9f1ca138df8acf1f57e9f', 'Đoàn Bá Quân', '84387729871'),
(35, 3964750, '1a66aae914ad35490dae424b7c34efb6', 'Đào Cốc', '84378752504'),
(36, 3577124, 'dc4726227fd06bbed0fc8c796b2a7e6d', 'Bảo Bảo', '84397305570'),
(37, 3497691, '975a41f07f1b43280cb900bd251b2a51', 'Bằng Cường Văn', '84348026487'),
(38, 3502288, 'f0f567dfb8161580ceec4ed86b4a1ea6', 'Hùng Bá', '84325883148'),
(39, 3403509, 'b213f0b229a5ae9e0462c9260193aa33', 'Nguyễn Thị Vân', '84383725427'),
(40, 3620605, '1cbe3874675cd639a260a133a95d6f88', 'David Minh Nhật', '84354125283'),
(41, 2393261, '36f18997ad1be26f109bdc16b00ef7f3', 'Trần Bích Quân', '84389224130'),
(42, 3582519, 'a4a7a5f9f239fcb9c16f2fe5a56db4b6', 'Tony Nguyen', '84396078560'),
(43, 2370088, '27f4b3234a7437380611d56b5ba52d93', 'Bùi Đình Thôn', '84385204325'),
(44, 2559905, '5d469328cf148a117d62958164c38dfc', 'Miller Anthea', '84375652347'),
(45, 2488510, 'eb39c67e0202e6711262a4c0439e5be1', '财务', '84394656976'),
(46, 3839533, '34312c7bb9ed8fcdfbc1e41364df59ac', 'A Phủ', '84387528412'),
(47, 3032283, 'e08d2f53864fd55c75be474f924105db', 'Harrison Peck', '84378843763'),
(48, 2589403, '1dfbf984f7f64390b15fc3529b018b0f', 'Hoa Lệ', '84921697430');

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `username` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fname` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `isAdmin` tinyint(1) DEFAULT NULL,
  `vip_pack` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `register_time` datetime DEFAULT NULL,
  `sentences_per_day` int(10) DEFAULT 0,
  `clone_limit` int(10) DEFAULT 0,
  `effective_days` int(10) DEFAULT 0,
  `expired_date` datetime DEFAULT NULL,
  `remaining_days` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `username`, `password`, `fname`, `phone`, `isAdmin`, `vip_pack`, `register_time`, `sentences_per_day`, `clone_limit`, `effective_days`, `expired_date`, `remaining_days`) VALUES
(1, 'quannm', 'e10adc3949ba59abbe56e057f20f883e', 'Quân', '+84123456987', 1, 'Vipad', '2021-05-19 00:00:00', 9999, 9999, 9999, '2021-06-11 10:36:12', 9999),
(7, 'nmq', 'e10adc3949ba59abbe56e057f20f883e', 'NMQ', '+84000000000', 0, 'Vip2', '2021-05-19 08:52:11', 4800, 12, 30, '2021-07-18 08:54:13', 30),
(8, 'quannm1', 'e10adc3949ba59abbe56e057f20f883e', 'NMQ', '+84123456789', 0, 'Vip2', '2021-05-19 08:59:41', 3600, 12, 30, '2021-06-18 08:59:41', 30),
(9, 'phucbv', 'e10adc3949ba59abbe56e057f20f883e', 'Phúc', '+84123456987', 0, 'Vip3', '2021-05-19 09:02:27', 9000, 30, 30, '2021-06-18 09:02:27', 30),
(10, 'cuongtv', 'e10adc3949ba59abbe56e057f20f883e', 'Cường', '+84987654321', 0, 'Vip2', '2021-05-19 09:04:45', 4800, 12, 30, '2021-07-18 09:04:45', 60),
(11, 'quannm2', 'e10adc3949ba59abbe56e057f20f883e', 'NMQ', '+84123123123', 0, 'Vip3', '2021-05-19 09:05:43', 9000, 30, 30, '2021-06-18 09:05:43', 30);

-- --------------------------------------------------------

--
-- Table structure for table `dialog`
--

CREATE TABLE `dialog` (
  `id` int(11) NOT NULL,
  `customer` varchar(80) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `content` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `group_id` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `delay` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `group`
--

CREATE TABLE `group` (
  `id` int(11) NOT NULL,
  `customer` varchar(80) CHARACTER SET utf8mb4 DEFAULT NULL,
  `group_id` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL,
  `group_title` text CHARACTER SET utf8mb4 DEFAULT NULL,
  `group_link` text CHARACTER SET utf8mb4 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `clone`
--
ALTER TABLE `clone`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `api_id` (`api_id`),
  ADD UNIQUE KEY `api_hash` (`api_hash`);

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `dialog`
--
ALTER TABLE `dialog`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `group`
--
ALTER TABLE `group`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `clone`
--
ALTER TABLE `clone`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `dialog`
--
ALTER TABLE `dialog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `group`
--
ALTER TABLE `group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
