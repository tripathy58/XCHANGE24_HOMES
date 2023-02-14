

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";




--
-- Table structure for table `admin_login`
--

CREATE TABLE `admin_login` (
  `name` text NOT NULL,
  `email` varchar(500) NOT NULL,
  `password` varchar(100) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `image` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_login`
--

INSERT INTO `admin_login` (`name`, `email`, `password`, `mobile`, `image`) VALUES
('Ashish Tripathy', 'tripathysonu59@gmail.com', 'Sonu@143', '9337407649', 'ashish.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `ads`
--

CREATE TABLE `ads` (
  `id` int(11) NOT NULL,
  `uniid` varchar(20) NOT NULL,
  `title` varchar(50) NOT NULL,
  `house_type` varchar(10) NOT NULL,
  `bhk_type` varchar(10) NOT NULL,
  `bathroom` int(11) NOT NULL,
  `car` int(11) NOT NULL,
  `tenant` varchar(30) NOT NULL,
  `bachelor` varchar(10) NOT NULL,
  `total_floor` int(11) DEFAULT NULL,
  `floor_no` int(11) DEFAULT NULL,
  `facing` varchar(10) DEFAULT NULL,
  `furnishing` varchar(20) NOT NULL,
  `area` varchar(20) DEFAULT NULL,
  `city` varchar(50) NOT NULL,
  `locality` varchar(50) NOT NULL,
  `pg` varchar(10) DEFAULT NULL,
  `sharing` varchar(10) DEFAULT NULL,
  `rent` int(11) NOT NULL,
  `owner_name` text NOT NULL,
  `owner_mobile` varchar(10) NOT NULL,
  `owner_whatsapp` varchar(10) DEFAULT NULL,
  `listed_by` varchar(100) NOT NULL,
  `date` date NOT NULL DEFAULT current_timestamp(),
  `month` int(2) NOT NULL,
  `year` int(4) NOT NULL,
  `time` time(6) NOT NULL DEFAULT current_timestamp(),
  `description` varchar(2000) NOT NULL,
  `status` varchar(20) NOT NULL,
  `reason` varchar(1000) NOT NULL,
  `disable_by` varchar(50) NOT NULL,
  `image` varchar(200) NOT NULL,
  `image2` varchar(1000) DEFAULT NULL,
  `image3` varchar(200) DEFAULT NULL,
  `image4` varchar(200) DEFAULT NULL,
  `image5` varchar(200) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `ads`
--

INSERT INTO `ads` (`id`, `uniid`, `title`, `house_type`, `bhk_type`, `bathroom`, `car`, `tenant`, `bachelor`, `total_floor`, `floor_no`, `facing`, `furnishing`, `area`, `city`, `locality`, `pg`, `sharing`, `rent`, `owner_name`, `owner_mobile`, `owner_whatsapp`, `listed_by`, `date`, `month`, `year`, `time`, `description`, `status`, `reason`, `disable_by`, `image`, `image2`, `image3`, `image4`, `image5`) VALUES
(139, '2ghllij15', '2 bhk flat', 'Appartment', '2bhk', 2, 2, 'Both', 'Working', 3, 1, 'East', 'Un-Furnished', '1200', 'none', 'AG Colony', 'No', 'No', 14000, 'Ashish Tripathy', '9556406021', '9556406021', 'Broker', '2023-01-30', 1, 0, '06:36:50.000000', 'xyz', 'Enable', '', '', '', 'Computer_Programmer1920X10180.jpg,house2.jpeg,house3_-_Copy.jpeg,house3.jpeg,house4.jpeg,house5.jpeg', NULL, NULL, NULL),
(140, '2ghllmanb', '3 bhk flat', 'Appartment', '3bhk', 2, 2, 'Family', 'Bachelor N', 2, 1, 'East', 'Un-Furnished', '1600', 'none', 'Adrash Vihar Patia', 'No', 'No', 32000, 'Ashish Tripathy', '9556406021', '9556406021', 'Broker', '2023-01-30', 1, 0, '06:38:29.000000', 'abc', 'Disable', 'Coming soon', '', '', 'beautiful-modern-house-20294138_-_Copy.jpg,images_1_-_Copy.jpeg,images.jpeg,types-of-homes-hero.jpg,w620x413.jpg', NULL, NULL, NULL),
(141, 'q178wqah', '2 bhk house', 'House', '2bhk', 2, 2, 'Family', 'Bachelor N', 1, 1, 'East', 'Semi-Furnished', '1200', 'none', 'BJB Nagar', 'No', 'No', 32000, 'Ashish Tripathy', '9556406021', '9556406021', 'Broker', '2023-01-30', 1, 0, '06:40:42.000000', 'xyz', 'Enable', '', '', '', 'beautiful-modern-house-20294138_-_Copy.jpg,images_1_-_Copy.jpeg,w620x413.jpg', NULL, NULL, NULL),
(142, 'e221a4fb2d', '4 bhk flat', 'Appartment', '4bhk', 4, 3, 'Family', 'Bachelor N', 4, 3, 'North', 'Un-Furnished', '1800', 'none', 'Arya Village', 'Yes', 'Yes', 32000, 'Ashish Tripathy', '9556406021', '9556406021', 'Broker', '2023-01-30', 1, 0, '06:43:26.000000', 'xyz', 'Enable', 'Product Enabled By Admin', 'Ashish Tripathy', '', 'house1_-_Copy.jpeg,house1.jpeg,house2_-_Copy.jpeg,house3.jpeg,house4.jpeg,house5.jpeg,land1.jpeg,land2.jpeg,land3.jpeg,land4.jpeg', NULL, NULL, NULL),
(147, '2262434b84', '2 bhk flat at Patia', 'Appartment', '2bhk', 2, 2, 'Family', 'Bachelor N', 2, 1, 'East', 'Un-Furnished', '1200', 'none', 'Damana', 'No', 'No', 14000, 'Ashish Tripathy', '9556406021', '9556406021', 'Owner', '2023-02-01', 2, 0, '03:03:53.000000', 'new house', 'Enable', '', '', '', 'house1.jpeg,house2.jpeg,house3.jpeg,house4.jpeg,house5.jpeg,villa2.jpeg,villa3.jpeg,villa4.jpeg,villa5.jpeg', NULL, NULL, NULL),
(148, 'e22a10860f', '3 bhk House', 'House', '3bhk', 3, 2, 'Family', 'Bachelor N', 0, 0, 'East', 'Un-Furnished', 'N/A', 'none', 'Chandrasekharpur', 'N/A', 'N/A', 32000, 'Ashish Tripathy', '9556406021', '9556406021', 'Owner', '2023-02-01', 2, 0, '15:23:40.000000', 'new house', 'Enable', 'Product Enabled By Admin', '', '', 'villa1.jpeg,villa2.jpeg,villa3.jpeg,villa4.jpeg,villa5.jpeg', NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `chat`
--

CREATE TABLE `chat` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `name` text NOT NULL,
  `message` varchar(10000) NOT NULL,
  `admin_email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `chat`
--

INSERT INTO `chat` (`id`, `email`, `name`, `message`, `admin_email`) VALUES
(9, '', '', 'hii', ''),
(10, 'devilisback226@gmail.com', 'Sonu Tripathy', 'hii', ''),
(11, '', '', 'hello', 'tripathysonu59@gmail.com'),
(12, '', '', 'how are you', 'tripathysonu59@gmail.com'),
(13, 'devilisback226@gmail.com', 'Sonu Tripathy', 'i\'m fine , how are you', ''),
(14, '', '', 'im fine . do u want any thing', 'tripathysonu59@gmail.com'),
(15, 'sudeptalenka94@gmail.com', 'Ashish Tripathy', 'is any 1 bhk available', ''),
(16, 'sudeptalenka94@gmail.com', '', 'yes available', 'tripathysonu59@gmail.com'),
(17, 'sudeptalenka94@gmail.com', '', 'want it', 'tripathysonu59@gmail.com'),
(18, 'sudeptalenka94@gmail.com', 'Ashish Tripathy', 'i need a 2 bhk flat near patia', '');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password` varchar(20) NOT NULL,
  `image` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`id`, `name`, `mobile`, `email`, `password`, `image`) VALUES
(8, 'Ashish Tripathy', '9337407649', 'tripathysonu58@gmail.com', 'Ashish1234', 'WhatsApp_Image_2021-03-29_at_2.34.01_PM.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `images`
--

CREATE TABLE `images` (
  `id` int(11) NOT NULL,
  `uni` varchar(20) NOT NULL,
  `photo` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `images`
--

INSERT INTO `images` (`id`, `uni`, `photo`) VALUES
(80, '2ghllij15', 'Computer_Programmer1920X10180.jpg'),
(81, '2ghllij15', 'house2.jpeg'),
(82, '2ghllij15', 'house3_-_Copy.jpeg'),
(83, '2ghllij15', 'house3.jpeg'),
(84, '2ghllij15', 'house4.jpeg'),
(85, '2ghllij15', 'house5.jpeg'),
(86, '2ghllmanb', 'beautiful-modern-house-20294138_-_Copy.jpg'),
(87, '2ghllmanb', 'images_1_-_Copy.jpeg'),
(88, '2ghllmanb', 'images.jpeg'),
(89, '2ghllmanb', 'types-of-homes-hero.jpg'),
(90, '2ghllmanb', 'w620x413.jpg'),
(91, 'q178wqah', 'beautiful-modern-house-20294138_-_Copy.jpg'),
(92, 'q178wqah', 'images_1_-_Copy.jpeg'),
(93, 'q178wqah', 'w620x413.jpg'),
(94, 'e221a4fb2d', 'house1_-_Copy.jpeg'),
(95, 'e221a4fb2d', 'house1.jpeg'),
(96, 'e221a4fb2d', 'house2_-_Copy.jpeg'),
(97, 'e221a4fb2d', 'house3.jpeg'),
(98, 'e221a4fb2d', 'house4.jpeg'),
(99, 'e221a4fb2d', 'house5.jpeg'),
(100, 'e221a4fb2d', 'land1.jpeg'),
(101, 'e221a4fb2d', 'land2.jpeg'),
(102, 'e221a4fb2d', 'land3.jpeg'),
(103, 'e221a4fb2d', 'land4.jpeg'),
(104, '80ell4c6a', 'villa2.jpeg'),
(105, '80ell4c6a', 'villa3.jpeg'),
(106, '80ell4c6a', 'villa4.jpeg'),
(107, '80ell4c6a', 'villa5.jpeg'),
(108, '2262434b84', 'house1.jpeg'),
(109, '2262434b84', 'house2.jpeg'),
(110, '2262434b84', 'house3.jpeg'),
(111, '2262434b84', 'house4.jpeg'),
(112, '2262434b84', 'house5.jpeg'),
(113, '2262434b84', 'villa2.jpeg'),
(114, '2262434b84', 'villa3.jpeg'),
(115, '2262434b84', 'villa4.jpeg'),
(116, '2262434b84', 'villa5.jpeg'),
(117, 'e22a10860f', 'villa1.jpeg'),
(118, 'e22a10860f', 'villa2.jpeg'),
(119, 'e22a10860f', 'villa3.jpeg'),
(120, 'e22a10860f', 'villa4.jpeg'),
(121, 'e22a10860f', 'villa5.jpeg');

-- --------------------------------------------------------

--
-- Table structure for table `location`
--

CREATE TABLE `location` (
  `city` varchar(100) NOT NULL,
  `locality` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `products`
--

CREATE TABLE `products` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `house_type` varchar(10) NOT NULL,
  `bhk_type` varchar(10) NOT NULL,
  `bathroom` int(2) NOT NULL,
  `car` int(2) NOT NULL,
  `tenant` varchar(10) NOT NULL,
  `bachelor` varchar(50) NOT NULL,
  `total_floor` int(2) NOT NULL,
  `floor_no` int(2) NOT NULL,
  `facing` varchar(10) NOT NULL,
  `furnishing` varchar(20) NOT NULL,
  `area` varchar(20) NOT NULL,
  `city` varchar(50) NOT NULL,
  `locality` varchar(50) NOT NULL,
  `pg` varchar(10) NOT NULL,
  `sharing` varchar(10) NOT NULL,
  `rent` int(20) NOT NULL,
  `listed_by` varchar(10) NOT NULL,
  `description` varchar(5000) NOT NULL,
  `photo` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `products`
--

INSERT INTO `products` (`id`, `title`, `house_type`, `bhk_type`, `bathroom`, `car`, `tenant`, `bachelor`, `total_floor`, `floor_no`, `facing`, `furnishing`, `area`, `city`, `locality`, `pg`, `sharing`, `rent`, `listed_by`, `description`, `photo`) VALUES
(3, '2 Bhk House Near patia', 'Appartment', '2 BHK', 2, 1, 'Both', 'Working', 4, 1, 'East', 'Furnished', '1200', 'Patia', 'Ahalya Nagar', 'No', 'No', 20000, 'Owner', 'added by ashish tripathy', '2.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `review`
--

CREATE TABLE `review` (
  `id` int(11) NOT NULL,
  `rank` varchar(100) NOT NULL,
  `name` text DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `date` varchar(10) NOT NULL,
  `about` varchar(100) NOT NULL,
  `message` varchar(10000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `review`
--

INSERT INTO `review` (`id`, `rank`, `name`, `email`, `date`, `about`, `message`) VALUES
(16, '', 'Ashish Tripathy', 'devilisback226@gmail.com', '2023-01-25', 'About the houses ', 'You have premium houses. A great experiences ');

-- --------------------------------------------------------

--
-- Table structure for table `status`
--

CREATE TABLE `status` (
  `id` int(11) NOT NULL,
  `image` varchar(1000) NOT NULL,
  `text` varchar(10000) NOT NULL,
  `date` date DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `status`
--

INSERT INTO `status` (`id`, `image`, `text`, `date`) VALUES
(10, 'house3.jpeg', 'new house added to list go and check it out', '2023-01-10'),
(11, 'house1.jpeg', 'duplex near patia', '2023-01-10'),
(12, 'house2.jpeg', 'this house is amezing', '2023-01-10'),
(13, 'house4.jpeg', 'New house added to catlog', '2023-01-10'),
(14, 'house1.jpeg', 'for sell', '2023-01-10'),
(15, 'ashish1.jpeg', 'hey', '2023-01-10'),
(16, 'ashish1.jpeg', 'hey', '2023-01-10'),
(17, 'ashish1.jpeg', 'hey', '2023-01-05'),
(18, 'ashish1.jpeg', 'hey', '2023-01-05'),
(19, '491-4915738_dress-png-woman-in-dress-no-background-transparent.png', 'hii', '2023-01-05'),
(20, 'banner1.jpg', 'hi hey', '2023-01-05'),
(21, 'banner1.jpg', 'hi hey', '2023-01-05'),
(22, 'banner1.jpg', 'hi hey', '2023-01-05'),
(23, 'banner1.jpg', 'hi hey', '2023-01-05'),
(24, 'banner1.jpg', 'hi hey', '2023-01-05'),
(25, 'banner4.jpg', 'bbbb', '2023-01-05'),
(26, 'WhatsApp_Image_2021-03-30_at_11.43.27_AM_1.jpeg', 'hi ashish', '2023-01-05'),
(27, 'WhatsApp_Image_2021-03-30_at_11.43.27_AM_1.jpeg', 'hi ashish', '2023-01-05'),
(28, 'WhatsApp_Image_2021-03-30_at_11.43.27_AM_1.jpeg', 'hi ashish', '2023-01-05'),
(29, 'house4.jpeg', 'new home', '2023-01-06'),
(30, 'bitcoin.jpeg', 'bit coin', '2023-01-06'),
(31, 'registration3.jpg', 'reg', '2023-01-06'),
(32, 'registration3.jpg', 'reg', '2023-01-06'),
(33, 'registration3.jpg', 'reg', '2023-01-06'),
(34, 'ashish1.jpeg', 'hey sonu', '2023-01-06'),
(35, 'WhatsApp_Image_2021-03-30_at_11.40.35_AM.jpeg', 'mmmmmm', '2023-01-06'),
(36, 'villa5.jpeg', 'hey house', '2023-01-06'),
(37, 'WhatsApp_Image_2022-05-04_at_2.10.47_PM_1.jpeg', 'bihari', '2023-01-06'),
(38, 'WhatsApp_Image_2022-05-04_at_2.10.47_PM_1.jpeg', 'bihari', '2023-01-06'),
(39, 'ashish.jpeg', 'hi baby', '2023-01-06'),
(40, 'ashish.jpeg', 'hi baby', '2023-01-06'),
(41, 'banner1_-_Copy.jpg', 'nnn', '2023-01-06'),
(42, 'ashish.jpeg', 'new product', '2023-01-25'),
(43, 'house4.jpeg', 'new house in Patia', '2023-02-01'),
(44, 'house1.jpeg', 'xyz', '2023-02-02'),
(45, 'house3.jpeg', 'new house', '2023-02-02'),
(46, 'login.jpeg', 'abc', '2023-02-02'),
(47, 'villa4.jpeg', 'hiii', '2023-02-02');

-- --------------------------------------------------------

--
-- Table structure for table `user_login`
--

CREATE TABLE `user_login` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(500) NOT NULL,
  `password` varchar(100) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `address1` varchar(1000) DEFAULT NULL,
  `address2` varchar(1000) DEFAULT NULL,
  `pin` int(6) NOT NULL,
  `city` varchar(20) DEFAULT NULL,
  `image` varchar(1000) NOT NULL,
  `location` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_login`
--

INSERT INTO `user_login` (`id`, `name`, `email`, `password`, `mobile`, `address1`, `address2`, `pin`, `city`, `image`, `location`) VALUES
(1, 'Ashish Tripathy', 'sudeptalenka94@gmail.com', 'Sonu@143', '', NULL, NULL, 0, '', '', ''),
(3, 'Manoranjan Muduli ', 'mmjk@gmail.com', 'Sonu@1024', '', NULL, NULL, 0, '', '', ''),
(4, 'Ashish Tripathy', 'devilisback226@gmail.com', 'Sonu@955640', '9556406021', 'Sishu Vihar', 'Patia', 751024, 'Bhubaneswar', 'portfolio.jpeg', 'AG Colony');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_chat`
--
ALTER TABLE `admin_chat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ads`
--
ALTER TABLE `ads`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `chat`
--
ALTER TABLE `chat`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `images`
--
ALTER TABLE `images`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `products`
--
ALTER TABLE `products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `review`
--
ALTER TABLE `review`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `status`
--
ALTER TABLE `status`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_login`
--
ALTER TABLE `user_login`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_chat`
--
ALTER TABLE `admin_chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `ads`
--
ALTER TABLE `ads`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=149;

--
-- AUTO_INCREMENT for table `chat`
--
ALTER TABLE `chat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `employee`
--
ALTER TABLE `employee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `images`
--
ALTER TABLE `images`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=122;

--
-- AUTO_INCREMENT for table `products`
--
ALTER TABLE `products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `review`
--
ALTER TABLE `review`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `status`
--
ALTER TABLE `status`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;

--
-- AUTO_INCREMENT for table `user_login`
--
ALTER TABLE `user_login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
