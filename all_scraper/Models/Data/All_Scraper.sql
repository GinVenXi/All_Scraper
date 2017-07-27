-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: 2017-06-30 15:57:13
-- 服务器版本： 5.7.18-0ubuntu0.16.04.1
-- PHP Version: 7.0.15-0ubuntu0.16.04.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `All_Scraper`
--

-- --------------------------------------------------------

--
-- 表的结构 `amazon_product`
--

CREATE TABLE `amazon_product` (
  `id` int(10) UNSIGNED NOT NULL,
  `region` enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') NOT NULL DEFAULT 'com',
  `asin` char(10) NOT NULL,
  `variation_parentage` enum('Parent','Child','N/A') NOT NULL DEFAULT 'N/A',
  `parent_asin` char(10) DEFAULT NULL,
  `status` tinyint(3) UNSIGNED NOT NULL DEFAULT '1',
  `title` text,
  `description` text,
  `detail_page_url` text,
  `category` varchar(64) DEFAULT NULL,
  `browse_node` varchar(64) DEFAULT NULL,
  `sales_rank` int(10) UNSIGNED DEFAULT NULL,
  `rating` tinyint(3) UNSIGNED DEFAULT NULL,
  `review_count` int(5) UNSIGNED DEFAULT NULL,
  `price` int(10) UNSIGNED DEFAULT NULL,
  `shipping` varchar(64) DEFAULT NULL,
  `list_price` int(10) UNSIGNED DEFAULT NULL,
  `fulfillment` enum('AFN','MFN') DEFAULT NULL,
  `seller_id` varchar(14) DEFAULT NULL,
  `seller_name` varchar(64) DEFAULT NULL,
  `first_available_date` date DEFAULT NULL,
  `last_updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `bestseller_node_id` bigint(20) UNSIGNED DEFAULT NULL,
  `is_fba` tinyint(1) UNSIGNED DEFAULT '0',
  `offer_count` smallint(5) UNSIGNED NOT NULL DEFAULT '1',
  `variation_count` smallint(5) UNSIGNED NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `amazon_product_image`
--

CREATE TABLE `amazon_product_image` (
  `id` bigint(20) UNSIGNED NOT NULL,
  `region` enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') NOT NULL DEFAULT 'com',
  `asin` char(10) NOT NULL,
  `url` varchar(128) NOT NULL,
  `width` smallint(5) UNSIGNED DEFAULT NULL,
  `height` smallint(5) UNSIGNED DEFAULT NULL,
  `position` tinyint(3) UNSIGNED NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `amazon_product_keywords_ad`
--

CREATE TABLE `amazon_product_keywords_ad` (
  `id` int(10) UNSIGNED NOT NULL,
  `region` enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') NOT NULL DEFAULT 'com',
  `asin` char(10) NOT NULL,
  `keywords` varchar(128) NOT NULL,
  `node_id` bigint(20) UNSIGNED NOT NULL,
  `position` smallint(5) UNSIGNED NOT NULL,
  `page_id` smallint(5) UNSIGNED NOT NULL DEFAULT '1',
  `page_position` smallint(5) UNSIGNED NOT NULL,
  `ad_position_type` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `ad_position` tinyint(3) UNSIGNED NOT NULL,
  `last_updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `amazon_product_keywords_rank`
--

CREATE TABLE `amazon_product_keywords_rank` (
  `id` int(10) UNSIGNED NOT NULL,
  `region` enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') NOT NULL DEFAULT 'com',
  `asin` char(10) NOT NULL,
  `keywords` varchar(128) NOT NULL,
  `node_id` bigint(20) UNSIGNED NOT NULL,
  `rank` smallint(5) UNSIGNED NOT NULL,
  `page_id` smallint(5) UNSIGNED NOT NULL DEFAULT '1',
  `page_position` smallint(5) UNSIGNED NOT NULL,
  `last_updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `amazon_product_review`
--

CREATE TABLE `amazon_product_review` (
  `id` int(10) UNSIGNED NOT NULL,
  `region` enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') NOT NULL DEFAULT 'com',
  `review_id` varchar(16) NOT NULL,
  `asin` char(10) NOT NULL,
  `customer_id` varchar(32) DEFAULT NULL,
  `customer_name` varchar(128) DEFAULT NULL,
  `title` varchar(128) DEFAULT NULL,
  `description` text,
  `rating` tinyint(3) UNSIGNED DEFAULT NULL,
  `date` date DEFAULT NULL,
  `helpful_yes` int(10) UNSIGNED DEFAULT NULL,
  `helpful_no` int(10) UNSIGNED DEFAULT NULL,
  `is_verified` tinyint(1) DEFAULT NULL,
  `is_image_included` tinyint(1) DEFAULT NULL,
  `is_video_included` tinyint(1) DEFAULT NULL,
  `last_updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `amazon_product_review_image`
--

CREATE TABLE `amazon_product_review_image` (
  `id` int(10) UNSIGNED NOT NULL,
  `region` enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') NOT NULL DEFAULT 'com',
  `review_id` varchar(16) NOT NULL,
  `url` varchar(128) NOT NULL,
  `width` smallint(5) UNSIGNED DEFAULT NULL,
  `height` smallint(5) UNSIGNED DEFAULT NULL,
  `position` tinyint(3) UNSIGNED NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `amazon_product_review_video`
--

CREATE TABLE `amazon_product_review_video` (
  `id` int(10) UNSIGNED NOT NULL,
  `region` enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') NOT NULL DEFAULT 'com',
  `review_id` varchar(16) NOT NULL,
  `url` varchar(128) NOT NULL,
  `image_url` varchar(128) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `amazon_seller`
--

CREATE TABLE `amazon_seller` (
  `id` int(10) UNSIGNED NOT NULL,
  `region` enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') NOT NULL DEFAULT 'com',
  `seller_id` varchar(32) NOT NULL,
  `name` varchar(128) DEFAULT NULL,
  `logo_url` varchar(128) DEFAULT NULL,
  `rating` tinyint(3) UNSIGNED DEFAULT NULL,
  `last_30_days_positive_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `last_90_days_positive_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `last_12_months_positive_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `lifetime_positive_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `last_30_days_neutral_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `last_90_days_neutral_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `last_12_months_neutral_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `lifetime_neutral_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `last_30_days_negative_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `last_90_days_negative_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `last_12_months_negative_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `lifetime_negative_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `last_30_days_feedback_count` int(10) UNSIGNED DEFAULT NULL,
  `last_90_days_feedback_count` int(10) UNSIGNED DEFAULT NULL,
  `last_12_months_feedback_count` int(10) UNSIGNED DEFAULT NULL,
  `lifetime_feedback_count` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `amazon_seller_product`
--

CREATE TABLE `amazon_seller_product` (
  `id` int(10) UNSIGNED NOT NULL,
  `region` enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') NOT NULL DEFAULT 'com',
  `seller_id` varchar(32) NOT NULL,
  `asin` char(10) NOT NULL,
  `status` tinyint(3) UNSIGNED NOT NULL DEFAULT '1',
  `rank` smallint(5) UNSIGNED DEFAULT NULL,
  `price` int(10) UNSIGNED DEFAULT NULL,
  `list_price` int(10) UNSIGNED DEFAULT NULL,
  `seller_name` varchar(128) DEFAULT NULL,
  `seller_logo_url` varchar(128) DEFAULT NULL,
  `seller_logo_width` smallint(5) UNSIGNED DEFAULT NULL,
  `seller_logo_height` smallint(5) UNSIGNED DEFAULT NULL,
  `seller_rating` tinyint(3) UNSIGNED DEFAULT NULL,
  `seller_last_12_months_positive_feedback_ratio` tinyint(3) UNSIGNED DEFAULT NULL,
  `seller_lifetime_feedback_count` int(10) UNSIGNED DEFAULT NULL,
  `search_index` varchar(32) DEFAULT NULL,
  `bestseller_node_id` bigint(20) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `amazon_seller_product_offer`
--

CREATE TABLE `amazon_seller_product_offer` (
  `id` int(10) UNSIGNED NOT NULL,
  `region` enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') NOT NULL DEFAULT 'com',
  `seller_id` varchar(32) NOT NULL,
  `asin` char(10) NOT NULL,
  `item_id` varchar(32) DEFAULT NULL,
  `status` tinyint(3) UNSIGNED NOT NULL DEFAULT '1',
  `price` int(10) UNSIGNED DEFAULT NULL,
  `shipping` varchar(64) DEFAULT NULL,
  `condition` enum('New','UsedLikeNew','UsedVeryGood','UsedGood','UsedAcceptable','CollectibleLikeNew','CollectibleVeryGood','CollectibleGood','CollectibleAcceptable','Refurbished','Club') DEFAULT NULL,
  `fulfillment` enum('AFN','MFN') DEFAULT NULL,
  `inventory` smallint(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `download_queue`
--

CREATE TABLE `download_queue` (
  `id` int(10) UNSIGNED NOT NULL,
  `ac_download_queue_id` int(10) UNSIGNED NOT NULL DEFAULT '0',
  `region` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `type` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `value` varchar(64) NOT NULL,
  `status` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `priority` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `scrape_count` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `upload_status` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `upload_count` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `last_updated_time` datetime DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `jd_keywords`
--

CREATE TABLE `jd_keywords` (
  `id` int(11) NOT NULL,
  `keyword` varchar(45) CHARACTER SET utf8 COLLATE utf8_swedish_ci NOT NULL,
  `sku` varchar(45) DEFAULT NULL,
  `productpage_url` varchar(1000) DEFAULT NULL,
  `page_id` int(11) DEFAULT NULL,
  `page_position` int(11) DEFAULT NULL,
  `last_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `jd_products`
--

CREATE TABLE `jd_products` (
  `id` int(11) NOT NULL,
  `sku` varchar(45) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `shop_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `shop_id` varchar(45) DEFAULT NULL,
  `shop_link` varchar(1000) DEFAULT NULL,
  `price` varchar(45) DEFAULT NULL,
  `review_count` varchar(45) DEFAULT NULL,
  `sellerpage_url` varchar(255) DEFAULT NULL,
  `shipping` varchar(45) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `shop_score` varchar(45) DEFAULT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `last_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `jd_product_image`
--

CREATE TABLE `jd_product_image` (
  `id` int(11) NOT NULL,
  `sku` varchar(45) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `last_update_time` datetime NOT NULL,
  `position` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `jd_product_review`
--

CREATE TABLE `jd_product_review` (
  `id` int(11) NOT NULL,
  `reviewer_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `reviewer_id` varchar(45) DEFAULT NULL,
  `product_information` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `review_content` varchar(2550) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `review_time` varchar(45) DEFAULT NULL,
  `product_id` varchar(45) DEFAULT NULL,
  `review_json_link` varchar(1000) DEFAULT NULL,
  `review_count` varchar(45) DEFAULT NULL,
  `goodrate` varchar(45) DEFAULT NULL,
  `poor_count` varchar(45) DEFAULT NULL,
  `general_count` varchar(45) DEFAULT NULL,
  `good_count` varchar(45) DEFAULT NULL,
  `last_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `jd_product_review_image`
--

CREATE TABLE `jd_product_review_image` (
  `id` int(11) NOT NULL,
  `reviewer_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `reviewer_id` varchar(45) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `last_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `jd_seller_page`
--

CREATE TABLE `jd_seller_page` (
  `id` int(11) NOT NULL,
  `seller_id` int(11) DEFAULT NULL,
  `seller_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `seller_location` varchar(45) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `seller_logo_url` varchar(255) DEFAULT NULL,
  `seller_total` varchar(45) DEFAULT NULL,
  `seller_quality` varchar(45) DEFAULT NULL,
  `seller_attitude` varchar(45) DEFAULT NULL,
  `seller_speed` varchar(45) DEFAULT NULL,
  `seller_discription` varchar(45) DEFAULT NULL,
  `seller_return` varchar(45) DEFAULT NULL,
  `seller_processtime` varchar(45) DEFAULT NULL,
  `seller_dispute` varchar(45) DEFAULT NULL,
  `seller_rework` varchar(45) DEFAULT NULL,
  `seller_hegui` varchar(45) DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `last_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `jingdong_downloadqueue`
--

CREATE TABLE `jingdong_downloadqueue` (
  `id` int(10) UNSIGNED NOT NULL,
  `ac_download_queue_id` int(10) UNSIGNED NOT NULL,
  `region` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `type` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `value` varchar(64) NOT NULL,
  `status` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `priority` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `scrape_count` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `upload_status` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `upload_count` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `last_updated_time` datetime DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `keywords`
--

CREATE TABLE `keywords` (
  `id` int(10) UNSIGNED NOT NULL,
  `region` enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') NOT NULL DEFAULT 'com',
  `name` varchar(128) NOT NULL,
  `monthly_amazon_search_volume` int(10) UNSIGNED DEFAULT NULL,
  `amazon_product_search_count` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `scrape`
--

CREATE TABLE `scrape` (
  `id` int(10) UNSIGNED NOT NULL,
  `download_queue_id` int(10) UNSIGNED NOT NULL,
  `method` tinyint(3) UNSIGNED DEFAULT NULL,
  `url` varchar(255) NOT NULL,
  `proxy_id` smallint(5) UNSIGNED DEFAULT NULL,
  `begin_time` datetime DEFAULT NULL,
  `end_time` datetime DEFAULT NULL,
  `status` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `comment` text,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `search_keywords`
--

CREATE TABLE `search_keywords` (
  `id` int(11) NOT NULL,
  `keyword` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- 表的结构 `sina_download_queue`
--

CREATE TABLE `sina_download_queue` (
  `id` int(11) NOT NULL,
  `url_id` varchar(64) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci NOT NULL,
  `url` varchar(255) NOT NULL,
  `type` varchar(64) NOT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '0',
  `last_updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- 表的结构 `sina_pages`
--

CREATE TABLE `sina_pages` (
  `id` int(11) NOT NULL,
  `url_id` varchar(64) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci NOT NULL,
  `url` varchar(255) NOT NULL,
  `summary` varchar(500) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `keywords` varchar(255) CHARACTER SET utf32 COLLATE utf32_swedish_ci DEFAULT NULL,
  `published_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `last_updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- 表的结构 `taobao_downloadqueue`
--

CREATE TABLE `taobao_downloadqueue` (
  `id` int(10) UNSIGNED NOT NULL,
  `ac_download_queue_id` int(10) UNSIGNED NOT NULL,
  `region` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `type` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `value` varchar(64) NOT NULL,
  `status` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `priority` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `scrape_count` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `upload_status` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `upload_count` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `last_updated_time` datetime DEFAULT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `taobao_keywords`
--

CREATE TABLE `taobao_keywords` (
  `id` int(11) NOT NULL,
  `product_id` varchar(45) NOT NULL,
  `keyword` varchar(45) CHARACTER SET utf8 COLLATE utf8_swedish_ci NOT NULL,
  `seller_id` varchar(45) NOT NULL,
  `productpage_url` varchar(1024) DEFAULT NULL,
  `page_id` int(11) DEFAULT NULL,
  `page_position` int(11) DEFAULT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `last_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `taobao_products`
--

CREATE TABLE `taobao_products` (
  `id` int(11) NOT NULL,
  `product_id` varchar(45) DEFAULT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `shop_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `before_price` varchar(45) DEFAULT NULL,
  `current_price` varchar(45) DEFAULT NULL,
  `discription` varchar(45) DEFAULT NULL,
  `service` varchar(45) DEFAULT NULL,
  `logistics` varchar(45) DEFAULT NULL,
  `shop_location` varchar(45) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `shipping` varchar(45) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `sell_count` varchar(45) DEFAULT NULL,
  `collect_count` varchar(45) DEFAULT NULL,
  `review_count` varchar(45) DEFAULT NULL,
  `shop_link` varchar(255) DEFAULT NULL,
  `sellerpage_url` varchar(255) DEFAULT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `last_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `taobao_product_image`
--

CREATE TABLE `taobao_product_image` (
  `id` int(11) NOT NULL,
  `product_id` varchar(45) DEFAULT NULL,
  `image_url` varchar(255) DEFAULT NULL,
  `last_update_time` datetime NOT NULL,
  `position` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `taobao_product_review`
--

CREATE TABLE `taobao_product_review` (
  `id` int(11) NOT NULL,
  `reviewer_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `reviewer_id` varchar(45) DEFAULT NULL,
  `product_information` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `review_content` varchar(2550) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `review_time` varchar(45) DEFAULT NULL,
  `review_json_link` varchar(1000) DEFAULT NULL,
  `seller_id` varchar(45) DEFAULT NULL,
  `append_comment` varchar(2550) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `review_count` varchar(45) DEFAULT NULL,
  `image_count` varchar(45) DEFAULT NULL,
  `last_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `taobao_product_review_image`
--

CREATE TABLE `taobao_product_review_image` (
  `id` int(11) NOT NULL,
  `reviewer_name` varchar(45) DEFAULT NULL,
  `reviewer_id` varchar(45) DEFAULT NULL,
  `image_url` varchar(255) NOT NULL,
  `time` timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `last_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `taobao_seller_page`
--

CREATE TABLE `taobao_seller_page` (
  `id` int(11) NOT NULL,
  `seller_name` varchar(45) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `seller_id` varchar(45) DEFAULT NULL,
  `seller_location` varchar(45) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `seller_credit` varchar(45) DEFAULT NULL,
  `seller_conform` varchar(45) DEFAULT NULL,
  `seller_service` varchar(45) DEFAULT NULL,
  `seller_logistics` varchar(45) DEFAULT NULL,
  `favorable_rate` varchar(45) DEFAULT NULL,
  `csspeed` varchar(45) DEFAULT NULL,
  `csrate` varchar(45) DEFAULT NULL,
  `dispute_rate` varchar(45) DEFAULT NULL,
  `penalty_num` varchar(45) DEFAULT NULL,
  `seller_page_link` varchar(255) DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL ON UPDATE CURRENT_TIMESTAMP,
  `last_update_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `tencent_download_queue`
--

CREATE TABLE `tencent_download_queue` (
  `id` int(11) NOT NULL,
  `url_id` varchar(64) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci NOT NULL,
  `url` varchar(255) NOT NULL,
  `type` varchar(64) NOT NULL,
  `status` tinyint(4) NOT NULL DEFAULT '0',
  `last_updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- 表的结构 `tencent_pages`
--

CREATE TABLE `tencent_pages` (
  `id` int(11) NOT NULL,
  `url_id` varchar(64) NOT NULL,
  `title` varchar(255) CHARACTER SET utf8 COLLATE utf8_swedish_ci NOT NULL,
  `url` varchar(255) NOT NULL,
  `summary` varchar(500) CHARACTER SET utf8 COLLATE utf8_swedish_ci DEFAULT NULL,
  `keywords` varchar(255) CHARACTER SET utf32 COLLATE utf32_swedish_ci DEFAULT NULL,
  `review_count` int(11) DEFAULT NULL,
  `review_link` varchar(255) DEFAULT NULL,
  `published_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `last_updated_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- 表的结构 `upload_queue`
--

CREATE TABLE `upload_queue` (
  `id` int(10) UNSIGNED NOT NULL,
  `region` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `type` tinyint(3) UNSIGNED NOT NULL DEFAULT '0',
  `value` varchar(64) NOT NULL,
  `time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `amazon_product`
--
ALTER TABLE `amazon_product`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IDX_AMAZON_PRODUCT_REGION_ASIN` (`region`,`asin`),
  ADD KEY `IDX_AMAZON_PRODUCT_REGION` (`region`),
  ADD KEY `IDX_AMAZON_PRODUCT_ASIN` (`asin`);

--
-- Indexes for table `amazon_product_image`
--
ALTER TABLE `amazon_product_image`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IDX_AMAZON_PRODUCT_IMAGE_REGION_ASIN_URL` (`region`,`asin`,`url`),
  ADD KEY `IDX_AMAZON_PRODUCT_IMAGE_REGION` (`region`),
  ADD KEY `IDX_AMAZON_PRODUCT_IMAGE_ASIN` (`asin`),
  ADD KEY `IDX_AMAZON_PRODUCT_IMAGE_URL` (`url`);

--
-- Indexes for table `amazon_product_keywords_ad`
--
ALTER TABLE `amazon_product_keywords_ad`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_AMAZON_KEYWORDS_AD_REGION` (`region`),
  ADD KEY `IDX_AMAZON_KEYWORDS_AD_KEYWORDS` (`keywords`),
  ADD KEY `IDX_AMAZON_KEYWORDS_AD_NODE_ID` (`node_id`);

--
-- Indexes for table `amazon_product_keywords_rank`
--
ALTER TABLE `amazon_product_keywords_rank`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_AMAZON_KEYWORDS_RANK_REGION` (`region`),
  ADD KEY `IDX_AMAZON_KEYWORDS_RANK_KEYWORDS` (`keywords`),
  ADD KEY `IDX_AMAZON_KEYWORDS_RANK_NODE_ID` (`node_id`);

--
-- Indexes for table `amazon_product_review`
--
ALTER TABLE `amazon_product_review`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IDX_AMAZON_PRODUCT_REVIEW_REGION_REVIEW_ID` (`region`,`review_id`),
  ADD KEY `IDX_AMAZON_PRODUCT_REVIEW_REGION` (`region`),
  ADD KEY `IDX_AMAZON_PRODUCT_REVIEW_REVIEW_ID` (`review_id`),
  ADD KEY `IDX_AMAZON_PRODUCT_REVIEW_ASIN` (`asin`);

--
-- Indexes for table `amazon_product_review_image`
--
ALTER TABLE `amazon_product_review_image`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IDX_AMAZON_PRODUCT_REVIEW_IMAGE_REGION_REVIEW_ID_URL` (`region`,`review_id`,`url`),
  ADD KEY `IDX_AMAZON_PRODUCT_REVIEW_IMAGE_REGION` (`region`),
  ADD KEY `IDX_AMAZON_PRODUCT_REVIEW_IMAGE_REVIEW_ID` (`review_id`),
  ADD KEY `IDX_AMAZON_PRODUCT_REVIEW_IMAGE_URL` (`url`);

--
-- Indexes for table `amazon_product_review_video`
--
ALTER TABLE `amazon_product_review_video`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IDX_AMAZON_PRODUCT_REVIEW_VIDEO_REGION_REVIEW_ID_URL` (`region`,`review_id`,`url`),
  ADD KEY `IDX_AMAZON_PRODUCT_REVIEW_VIDEO_REGION` (`region`),
  ADD KEY `IDX_AMAZON_PRODUCT_REVIEW_VIDEO_REVIEW_ID` (`review_id`),
  ADD KEY `IDX_AMAZON_PRODUCT_REVIEW_VIDEO_URL` (`url`);

--
-- Indexes for table `amazon_seller`
--
ALTER TABLE `amazon_seller`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IDX_AMAZON_SELLER_REGION_SELLER_ID` (`region`,`seller_id`),
  ADD KEY `IDX_AMAZON_SELLER_REGION` (`region`),
  ADD KEY `IDX_AMAZON_SELLER_SELLER_ID` (`seller_id`);

--
-- Indexes for table `amazon_seller_product`
--
ALTER TABLE `amazon_seller_product`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IDX_AMAZON_SELLER_REGION_SELLER_ID_ASIN` (`region`,`seller_id`,`asin`),
  ADD KEY `IDX_AMAZON_SELLER_PRODUCT_REGION` (`region`),
  ADD KEY `IDX_AMAZON_SELLER_PRODUCT_SELLER_ID` (`seller_id`),
  ADD KEY `IDX_AMAZON_SELLER_PRODUCT_ASIN` (`asin`);

--
-- Indexes for table `amazon_seller_product_offer`
--
ALTER TABLE `amazon_seller_product_offer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IDX_AMAZON_SELLER_PRODUCT_OFFER_REGION_SELLER_ASIN_ITEM_ID` (`region`,`seller_id`,`asin`,`item_id`),
  ADD KEY `IDX_AMAZON_SELLER_PRODUCT_OFFER_REGION` (`region`),
  ADD KEY `IDX_AMAZON_SELLER_PRODUCT_OFFER_SELLER_ID` (`seller_id`),
  ADD KEY `IDX_AMAZON_SELLER_PRODUCT_OFFER_ASIN` (`asin`),
  ADD KEY `IDX_AMAZON_SELLER_PRODUCT_OFFER_ITEM_ID` (`item_id`);

--
-- Indexes for table `download_queue`
--
ALTER TABLE `download_queue`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_DOWNLOAD_QUEUE_VALUE` (`value`);

--
-- Indexes for table `jd_keywords`
--
ALTER TABLE `jd_keywords`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jd_products`
--
ALTER TABLE `jd_products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jd_product_image`
--
ALTER TABLE `jd_product_image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jd_product_review`
--
ALTER TABLE `jd_product_review`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jd_product_review_image`
--
ALTER TABLE `jd_product_review_image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jd_seller_page`
--
ALTER TABLE `jd_seller_page`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `jingdong_downloadqueue`
--
ALTER TABLE `jingdong_downloadqueue`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_DOWNLOAD_QUEUE_VALUE` (`value`);

--
-- Indexes for table `keywords`
--
ALTER TABLE `keywords`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `IDX_KEYWORDS_NAME` (`name`,`region`) USING BTREE;

--
-- Indexes for table `scrape`
--
ALTER TABLE `scrape`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `search_keywords`
--
ALTER TABLE `search_keywords`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sina_download_queue`
--
ALTER TABLE `sina_download_queue`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `sina_pages`
--
ALTER TABLE `sina_pages`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `url_id` (`url_id`);

--
-- Indexes for table `taobao_downloadqueue`
--
ALTER TABLE `taobao_downloadqueue`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_DOWNLOAD_QUEUE_VALUE` (`value`);

--
-- Indexes for table `taobao_keywords`
--
ALTER TABLE `taobao_keywords`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `taobao_products`
--
ALTER TABLE `taobao_products`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `taobao_product_image`
--
ALTER TABLE `taobao_product_image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `taobao_product_review`
--
ALTER TABLE `taobao_product_review`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `taobao_product_review_image`
--
ALTER TABLE `taobao_product_review_image`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `taobao_seller_page`
--
ALTER TABLE `taobao_seller_page`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tencent_download_queue`
--
ALTER TABLE `tencent_download_queue`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `tencent_pages`
--
ALTER TABLE `tencent_pages`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `url_id` (`url_id`);

--
-- Indexes for table `upload_queue`
--
ALTER TABLE `upload_queue`
  ADD PRIMARY KEY (`id`),
  ADD KEY `IDX_UPLOAD_QUEUE_VALUE` (`value`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `amazon_product`
--
ALTER TABLE `amazon_product`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=301;
--
-- 使用表AUTO_INCREMENT `amazon_product_image`
--
ALTER TABLE `amazon_product_image`
  MODIFY `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=410;
--
-- 使用表AUTO_INCREMENT `amazon_product_keywords_ad`
--
ALTER TABLE `amazon_product_keywords_ad`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
--
-- 使用表AUTO_INCREMENT `amazon_product_keywords_rank`
--
ALTER TABLE `amazon_product_keywords_rank`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;
--
-- 使用表AUTO_INCREMENT `amazon_product_review`
--
ALTER TABLE `amazon_product_review`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `amazon_product_review_image`
--
ALTER TABLE `amazon_product_review_image`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `amazon_product_review_video`
--
ALTER TABLE `amazon_product_review_video`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `amazon_seller`
--
ALTER TABLE `amazon_seller`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `amazon_seller_product`
--
ALTER TABLE `amazon_seller_product`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `amazon_seller_product_offer`
--
ALTER TABLE `amazon_seller_product_offer`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `download_queue`
--
ALTER TABLE `download_queue`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43446;
--
-- 使用表AUTO_INCREMENT `jd_keywords`
--
ALTER TABLE `jd_keywords`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18840;
--
-- 使用表AUTO_INCREMENT `jd_products`
--
ALTER TABLE `jd_products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=281;
--
-- 使用表AUTO_INCREMENT `jd_product_image`
--
ALTER TABLE `jd_product_image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=275;
--
-- 使用表AUTO_INCREMENT `jd_product_review`
--
ALTER TABLE `jd_product_review`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36421;
--
-- 使用表AUTO_INCREMENT `jd_product_review_image`
--
ALTER TABLE `jd_product_review_image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `jd_seller_page`
--
ALTER TABLE `jd_seller_page`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=555;
--
-- 使用表AUTO_INCREMENT `jingdong_downloadqueue`
--
ALTER TABLE `jingdong_downloadqueue`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- 使用表AUTO_INCREMENT `keywords`
--
ALTER TABLE `keywords`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1186;
--
-- 使用表AUTO_INCREMENT `scrape`
--
ALTER TABLE `scrape`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19667;
--
-- 使用表AUTO_INCREMENT `search_keywords`
--
ALTER TABLE `search_keywords`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=577280;
--
-- 使用表AUTO_INCREMENT `sina_download_queue`
--
ALTER TABLE `sina_download_queue`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1362;
--
-- 使用表AUTO_INCREMENT `sina_pages`
--
ALTER TABLE `sina_pages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1361;
--
-- 使用表AUTO_INCREMENT `taobao_downloadqueue`
--
ALTER TABLE `taobao_downloadqueue`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
--
-- 使用表AUTO_INCREMENT `taobao_keywords`
--
ALTER TABLE `taobao_keywords`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36052;
--
-- 使用表AUTO_INCREMENT `taobao_products`
--
ALTER TABLE `taobao_products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;
--
-- 使用表AUTO_INCREMENT `taobao_product_image`
--
ALTER TABLE `taobao_product_image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=171;
--
-- 使用表AUTO_INCREMENT `taobao_product_review`
--
ALTER TABLE `taobao_product_review`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5667;
--
-- 使用表AUTO_INCREMENT `taobao_product_review_image`
--
ALTER TABLE `taobao_product_review_image`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- 使用表AUTO_INCREMENT `taobao_seller_page`
--
ALTER TABLE `taobao_seller_page`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3049;
--
-- 使用表AUTO_INCREMENT `tencent_download_queue`
--
ALTER TABLE `tencent_download_queue`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1470;
--
-- 使用表AUTO_INCREMENT `tencent_pages`
--
ALTER TABLE `tencent_pages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1442;
--
-- 使用表AUTO_INCREMENT `upload_queue`
--
ALTER TABLE `upload_queue`
  MODIFY `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33072;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
