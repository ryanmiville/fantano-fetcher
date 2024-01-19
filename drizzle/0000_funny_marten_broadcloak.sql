-- Current sql file was generated after introspecting the database
-- If you want to run this migration please uncomment this code before executing migrations
/*
CREATE TABLE `reviews` (
	`id` int AUTO_INCREMENT NOT NULL,
	`video_id` varchar(255) NOT NULL,
	`title` varchar(255) NOT NULL,
	`artist` varchar(255) NOT NULL,
	`album` varchar(255) NOT NULL,
	`description` text NOT NULL,
	`thumbnail_url` varchar(255) NOT NULL,
	`publish_date` date NOT NULL,
	`watch_url` varchar(255) NOT NULL,
	`yellow_flannel` tinyint,
	`rating` int,
	CONSTRAINT `reviews_id` PRIMARY KEY(`id`),
	CONSTRAINT `video_id` UNIQUE(`video_id`)
);

*/