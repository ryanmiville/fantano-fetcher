-- Current sql file was generated after introspecting the database
-- If you want to run this migration please uncomment this code before executing migrations
/*
CREATE TABLE `reviews` (
	`id` integer PRIMARY KEY AUTOINCREMENT,
	`video_id` text NOT NULL,
	`title` text NOT NULL,
	`artist` text NOT NULL,
	`album` text NOT NULL,
	`description` text NOT NULL,
	`thumbnail_url` text NOT NULL,
	`publish_date` text NOT NULL,
	`watch_url` text NOT NULL,
	`yellow_flannel` integer DEFAULT (NULL),
	`rating` text DEFAULT (NULL)
);

*/