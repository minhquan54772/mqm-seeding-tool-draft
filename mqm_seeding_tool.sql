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
DROP TABLE IF EXISTS `clone`;
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
(1, 3845192, 'ee3f76456f539941ef8c223d793c1187', 'None', '325976595'),
(2, 3326683, 'c54dfc6033d59f572a21000728991468', 'None', '869668594'),
(3, 3937949, '94bf170cea89644bf4bc31f47108f390', 'None', '369805473'),
(4, 3899170, '60161bb54d9068dda563e9caec9768c9', 'None', '374127674'),
(5, 3058516, 'a1822fd9138786cc42d621c13db24901', 'None', '368867049'),
(6, 3343349, 'a928562f49ced1e618a4619a1cbd9759', 'None', '375987705'),
(7, 3564149, '9913e056d6c1fdeb99537a1a2efb5d14', 'None', '363845419'),
(8, 3890124, '17f0ff3ad5bdd5b763248419f68f6f00', 'None', '372861781'),
(9, 3270938, '86e0af9dfbe558659b275c8f02d6222d', 'None', '375608814'),
(10, 2126667, '50b9db49a24ec0fc54f534998ec7f8d3', 'None', '355925914'),
(11, 2485366, 'ec8c75a71e74e1707968d5c9634a9ba7', 'None', '382847319'),
(12, 2206963, '909c311a00ad464a0d82424aea0f4d73', 'None', '359016827'),
(13, 3870880, 'b1e97f1f83524c8bbb3cd5008b876cb7', 'None', '389212394'),
(14, 2683901, '6609f630319449a1c78a4f8436bd6b05', 'None', '396253864'),
(15, 3257283, 'c53d2022da392ddb4594c4cac24f09d3', 'None', '366735490'),
(16, 3247921, 'f72be6859e80e013b2071cce906827a2', 'None', '378435501'),
(17, 3611832, '137a07b7be751ba04ce2ed44d8b77498', 'None', '366595278'),
(18, 3239558, 'f1de35314720cfc6fcf34bbd02975ae4', 'None', '342834178'),
(19, 3329695, 'cce89af40c1b968d3bc99a9c5c20fcff', 'None', '352709778'),
(20, 3185539, '64195fbd53f2e93a45c2f7b539452434', 'None', '396401748'),
(21, 2281228, 'e2d47479249149309e60db0c073a2a56', 'None', '378834954'),
(22, 3811763, '1be5d46e6f4eeca117e5a805d321defb', 'None', '393342971'),
(23, 3663039, 'c3f2f2e6ab791c5ad6479123085d7309', 'None', '369544960'),
(24, 3546062, '4862cb714d2a9cfe11ce4a313f0d1a10', 'None', '398298480');



-- --------------------------------------------------------

--
-- Table structure for table `customer`
--
DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `username` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `password` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `fname` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `phone` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `isAdmin` tinyint(1) DEFAULT NULL,
  `vip_pack` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `register_time` datetime DEFAULT NULL,
  `sentences_per_day` int(10) DEFAULT 0,
  `clone_limit` int(10) DEFAULT 0,
  `effective_days` int(10) DEFAULT 0
) ;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `username`, `password`, `fname`, `phone`, `isAdmin`) VALUES
(1, 'admin', '21232f297a57a5a743894a0e4a801fc3', 'ADMIN', '+84000000000', 1),
(2, 'quannm', 'e10adc3949ba59abbe56e057f20f883e', 'Quân NM', '+84123456789', 1),
(3, 'nmq', 'e10adc3949ba59abbe56e057f20f883e', 'Quân', '+84123456789', 0),
(4, 'khachhang001', 'e10adc3949ba59abbe56e057f20f883e', 'Trần Thương', '+84123456789', 0),
(5, 'khachhang0011', 'e10adc3949ba59abbe56e057f20f883e', 'Khách hàng 001.2', '+84123456789', 0);

-- --------------------------------------------------------

--
-- Table structure for table `dialog`
--
DROP TABLE IF EXISTS `dialog`;
CREATE TABLE `dialog` (
  `id` int(11) NOT NULL,
  `customer` varchar(80) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `content` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `group_id` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `delay` int(11) DEFAULT NULL
  
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `dialog`
--

INSERT INTO `dialog` (`id`, `customer`, `user_id`, `content`, `group_id`, `delay`) VALUES
(26, 'nmq', 1, ':rocket: Only 4 days left for you to receive LUCKY tokens from AirDrop. :wrapped_gift: Instant Receive Airdrop Tokens\n------------------------------------------\n:globe_with_meridians: Link below:  https://luckyswap.finance/airdrop\n:fire: Maximum Reward: 100 LUCKY tokens.\n:party_popper: No Need KYC or Referral to receive LUCKY tokens.\n:money_bag: You need to verify/submit your ERC20 ETH wallet address on MetaMask/ Trust.\n:shamrock: Add link LUCKY tokens: 0x59ab4584cf661f921c3b25a433f3d8a08b416b7b\n:flexed_biceps: Done.', '-1001158850531', 1),
(27, 'khachhang001', 2, 'Admin cho mình hỏi khi đăng ký AirDrop có phải KYC không?', '-1001431242902', 60),
(28, 'khachhang001', 1, 'Chào bạn, AirDrop không cần KYC và bạn chỉ cần có ví Trust hoặc ví Binance Chain nhe bạn.', '-1001431242902', 60),
(29, 'khachhang001', 2, 'Admin cho mình xin link địa chỉ token Lucky để thêm vào ví nhe.', '-1001431242902', 60),
(30, 'khachhang001', 1, 'Link AirDrop: https://luckyswap.finance/airdrop. Địa chỉ token: 0x59ab4584cf661f921c3b25a433f3d8a08b416b7b', '-1001431242902', 60),
(31, 'khachhang001', 2, 'Cảm ơn Ad', '-1001431242902', 60),
(37, 'khachhang0011', 11, 'Hello, can you tell me about LuckySwap?', '-1001431242902', 60),
(38, 'khachhang0011', 1, 'LuckySwap is an ecosystem that includes all DeFi products, such as AirDrop, Swap, NFT, Staking, Gaming,... And on April 15, 2021 will open LuckySwap Exchange on BSC. You can follow link Finance: https://luckyswap.finance/', '-1001431242902', 60),
(39, 'khachhang0011', 11, 'Yes, thanks ad. How many advertising channels does LuckySwap?', '-1001431242902', 60),
(40, 'khachhang0011', 1, ':globe_with_meridians: Link Liquidity Provider: https://app.uniswap.org/#/add/ETH/0x59aB4584CF661F921c3b25A433f3D8A08B416B7b', '-1001431242902', 3),
(41, 'khachhang0011', 1, ':globe_with_meridians: Liên kết UNISWAP: https://app.uniswap.org/', '-1001431242902', 3),
(42, 'khachhang0011', 1, ':globe_with_meridians: Liên kết LUCKYSWAP: https://luckyswap.exchange/#/swap', '-1001431242902', 3),
(43, 'khachhang0011', 1, ':globe_with_meridians: Ecosystem Link: https://luckyswap.io/', '-1001431242902', 3),
(44, 'khachhang0011', 1, ':globe_with_meridians: Link Whitepaper: https://luckyswap.finance/whitepaper.pdf', '-1001431242902', 3),
(45, 'khachhang0011', 1, ':globe_with_meridians: Link Fanpage: https://m.facebook.com/LuckySwap_DeFi-106664148141202/', '-1001431242902', 3),
(46, 'khachhang0011', 1, ':globe_with_meridians: Reddit Link: https://www.reddit.com/user/LuckySwap_DeFi', '-1001431242902', 3),
(47, 'khachhang0011', 1, ':globe_with_meridians: Twitter Link: https://twitter.com/LuckySwap_DeFi', '-1001431242902', 3),
(48, 'khachhang0011', 1, ':globe_with_meridians: Link Intagram: https://www.instagram.com/luckyswap_defi/', '-1001431242902', 3),
(49, 'khachhang0011', 1, ':globe_with_meridians: Link https://docs.luckyswap.io', '-1001431242902', 3),
(50, 'khachhang0011', 1, ':globe_with_meridians: Link https://luckyswap.finance/buy', '-1001431242902', 3),
(51, 'khachhang0011', 1, ':globe_with_meridians: Ecosystem Link: https://luckyswap.finance', '-1001431242902', 3),
(52, 'khachhang0011', 1, ':cross_mark: Join Channel LUCKY: https://t.me/luckyswap_Nfts', '-1001431242902', 3),
(53, 'khachhang0011', 1, ':cross_mark: Join the LUCKY Group: https://t.me/luckyswap_finance', '-1001431242902', 60),
(54, 'khachhang0011', 11, 'Thank you.', '-1001431242902', 1);

-- --------------------------------------------------------

--
-- Table structure for table `group`
--
DROP TABLE IF EXISTS `group`;
CREATE TABLE `group` (
  `id` int(11) NOT NULL,
  `customer` varchar(80) CHARACTER SET utf8mb4 DEFAULT NULL,
  `group_id` varchar(255) CHARACTER SET utf8mb4 DEFAULT NULL,
  `group_title` text CHARACTER SET utf8mb4 DEFAULT NULL,
  `group_link` text CHARACTER SET utf8mb4 DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Dumping data for table `group`
--

INSERT INTO `group` (`id`, `customer`, `group_id`, `group_title`, `group_link`) VALUES
(16, 'admin', '-1001158850531', 'Test BOT', 'https://t.me/joinchat/RRKn42EldGgpKvq0'),
(24, 'quannm', '-1001158850531', 'Test BOT', 'https://t.me/joinchat/RRKn42EldGgpKvq0'),
(25, 'quannm', '-1001274866902', 'Test Interact', 'https://t.me/joinchat/S_zs1utdBAhakiYt'),
(26, 'quannm', '-563690107', '+1 Group Test', 'https://t.me/joinchat/IZk6e7P52S4M0CA6'),
(27, 'admin', '-1001274866902', 'Test Interact', 'https://t.me/joinchat/S_zs1utdBAhakiYt'),
(28, 'admin', '-563690107', '+1 Group Test', 'https://t.me/joinchat/IZk6e7P52S4M0CA6'),
(29, 'nmq', '-1001158850531', 'Test BOT', 'https://t.me/joinchat/RRKn42EldGgpKvq0'),
(30, 'khachhang001', '-1001431242902', 'LuckySwap_Defi Community', 'https://t.me/luckyswap_finance'),
(31, 'khachhang0011', '-1001431242902', 'LuckySwap_Defi Community', 'https://t.me/luckyswap_finance');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `dialog`
--
ALTER TABLE `dialog`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- AUTO_INCREMENT for table `group`
--
ALTER TABLE `group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

ALTER DATABASE mqm_seeding_tool CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;


