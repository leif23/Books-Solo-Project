-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema book_solo_project
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `book_solo_project` ;

-- -----------------------------------------------------
-- Schema book_solo_project
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `book_solo_project` DEFAULT CHARACTER SET utf8 ;
USE `book_solo_project` ;

-- -----------------------------------------------------
-- Table `book_solo_project`.`users`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `book_solo_project`.`users` ;

CREATE TABLE IF NOT EXISTS `book_solo_project`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(145) NULL DEFAULT NULL,
  `last_name` VARCHAR(145) NULL DEFAULT NULL,
  `email` VARCHAR(145) NULL DEFAULT NULL,
  `password` VARCHAR(145) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 4
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `book_solo_project`.`books`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `book_solo_project`.`books` ;

CREATE TABLE IF NOT EXISTS `book_solo_project`.`books` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(145) NULL DEFAULT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `creator_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_books_users1_idx` (`creator_id` ASC) VISIBLE,
  CONSTRAINT `fk_books_users1`
    FOREIGN KEY (`creator_id`)
    REFERENCES `book_solo_project`.`users` (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 17
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `book_solo_project`.`favorite_books`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `book_solo_project`.`favorite_books` ;

CREATE TABLE IF NOT EXISTS `book_solo_project`.`favorite_books` (
  `user_id` INT NOT NULL,
  `book_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `book_id`),
  INDEX `fk_users_has_books_users1_idx` (`user_id` ASC) VISIBLE,
  INDEX `fk_favorite_books_books1_idx` (`book_id` ASC) VISIBLE,
  CONSTRAINT `fk_favorite_books_books1`
    FOREIGN KEY (`book_id`)
    REFERENCES `book_solo_project`.`books` (`id`),
  CONSTRAINT `fk_users_has_books_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `book_solo_project`.`users` (`id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
