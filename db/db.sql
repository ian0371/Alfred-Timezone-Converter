DROP TABLE `continent`;
DROP TABLE `country`;
DROP TABLE `timezone`;
DROP TABLE `city`;

CREATE TABLE IF NOT EXISTS `continent` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL UNIQUE,
    `code` TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS `country` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL UNIQUE,
    `code` TEXT NOT NULL UNIQUE,
    `continent_code` INTEGER NOT NULL,
    FOREIGN KEY(`continent_code`) REFERENCES continent(`code`)
);

CREATE TABLE IF NOT EXISTS `timezone` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `timezone` TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS `city` (
    `id` INTEGER PRIMARY KEY AUTOINCREMENT,
    `name` TEXT NOT NULL,
    `country_code` INTEGER NOT NULL,
    `subdiv1_name` TEXT,
    `subdiv1_code` TEXT,
    `subdiv2_name` TEXT,
    `subdiv2_code` TEXT,
    `timezone` INTEGER NOT NULL,
    FOREIGN KEY(`country_code`) REFERENCES country(`code`),
    FOREIGN KEY(`timezone`) REFERENCES timezone(`timezone`)
);

