-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: e-learning
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `courses`
--

DROP TABLE IF EXISTS `courses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `courses` (
  `course_id` int NOT NULL AUTO_INCREMENT,
  `course_name` varchar(255) NOT NULL,
  `course_description` text,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=273 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (100,'Programming Language','structure of compilers and interpreters.'),(101,'Value address','Wrong building item agreement benefit movement feel. Represent blood which rock keep enter rise. Glass prepare feel forward mission health especially. Animal best green play poor practice case. Move wife heavy risk age class low. Nothing media time perform.'),(102,'Seem few material','Radio alone third price. Class treatment magazine news specific. Work ground another science.'),(103,'Blue line technology turn','Information give vote seven become. Property trip task sign sure sell. Avoid accept attorney condition point enough you. Organization do church hand onto free no. Line place left say almost store. Food action other necessary action apply society.'),(104,'Exactly only','Role another strong issue risk wide record. Let prevent hour body open. Eight where stage six end. Pm get idea then with there visit pretty.'),(105,'Join too foot','Reveal age art wide. Watch rule ok authority head. Nature protect not school color show evening. Small level agreement street free establish tell money. Respond upon difference fish including relate. End leader attorney wife effect.');
/*!40000 ALTER TABLE `courses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `enrollments`
--

DROP TABLE IF EXISTS `enrollments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrollments` (
  `enrollment_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int NOT NULL,
  `course_id` int NOT NULL,
  `enrollment_date` date NOT NULL,
  `completion_date` date NOT NULL,
  PRIMARY KEY (`enrollment_id`),
  KEY `enrollments_ibfk_1` (`student_id`),
  KEY `enrollments_ibfk_2` (`course_id`),
  CONSTRAINT `enrollments_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`),
  CONSTRAINT `enrollments_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `courses` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=213 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollments`
--

LOCK TABLES `enrollments` WRITE;
/*!40000 ALTER TABLE `enrollments` DISABLE KEYS */;
INSERT INTO `enrollments` VALUES (31,6,105,'2020-05-10','2020-06-24'),(32,16,103,'2020-03-28','2024-09-01'),(33,17,102,'2022-03-11','2022-12-25'),(34,20,104,'2021-10-02','2023-02-15'),(35,4,101,'2022-02-02','2024-11-08'),(36,28,104,'2023-04-11','2024-03-28'),(37,18,103,'2021-08-01','2022-03-23'),(38,9,102,'2024-05-31','2025-08-25'),(39,22,101,'2023-06-14','2025-06-23'),(40,16,100,'2020-07-06','2024-07-29'),(41,2,100,'2021-02-27','2022-01-28'),(42,30,105,'2020-11-21','2024-10-07'),(43,21,100,'2020-01-17','2025-02-19'),(44,11,100,'2021-05-20','2025-11-02'),(45,22,105,'2022-09-01','2025-07-25'),(46,23,103,'2020-07-29','2022-06-05'),(47,13,104,'2022-07-06','2025-07-20'),(48,29,100,'2021-04-03','2023-01-08'),(49,7,101,'2024-09-14','2025-06-26'),(50,21,102,'2022-10-30','2023-09-01'),(51,23,104,'2020-01-10','2020-02-23'),(52,21,105,'2021-08-29','2022-10-15'),(53,12,100,'2022-06-05','2024-07-17'),(54,6,103,'2024-07-03','2025-07-24'),(55,21,105,'2022-08-29','2023-11-21'),(56,16,100,'2024-06-15','2024-10-15'),(57,25,105,'2024-03-29','2025-04-11'),(58,7,104,'2022-04-04','2023-05-16'),(59,12,102,'2023-06-30','2023-08-06'),(60,3,103,'2024-06-11','2025-10-24');
/*!40000 ALTER TABLE `enrollments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `student_id` int NOT NULL AUTO_INCREMENT,
  `student_firstName` varchar(100) NOT NULL,
  `student_lastName` varchar(100) NOT NULL,
  `student_email` varchar(100) DEFAULT NULL,
  `student_password` varchar(10) NOT NULL,
  PRIMARY KEY (`student_id`),
  UNIQUE KEY `student_password_UNIQUE` (`student_password`),
  UNIQUE KEY `student_email` (`student_email`)
) ENGINE=InnoDB AUTO_INCREMENT=193 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Roberto','Ruiz','johnathan32@example.net','%GET&mzAF3'),(2,'James','Robertson','danielwilson@example.org','^!P1Zx02^$'),(3,'Laura','Brewer','alansanders@example.com','k1)j&6Miba'),(4,'Richard','Bartlett','anna44@example.net','2$40BocQp*'),(5,'Colton','Stanley','kcampbell@example.net','Wk7!gId5u!'),(6,'James','Weiss','shannon20@example.net','B_8JPaurkc'),(7,'Hannah','Smith','stephanie07@example.net','D^s4X(ye3A'),(8,'Erin','West','cassandra83@example.com','0#6RAFQy8W'),(9,'Sandra','Pope','vschmitt@example.org','YD%0#@Ao7E'),(10,'Katie','Johnson','christopher45@example.com','v1+L1(6v#Q'),(11,'Jennifer','Dawson','charlotteriley@example.net','IzDwMZXw+4'),(12,'Nicole','Day','martinbryan@example.com','B*6Gv&vG$t'),(13,'Alyssa','Jones','ggray@example.net','U6C&^uIj+7'),(14,'Charles','Rhodes','nicholas85@example.org','apI44EGy*H'),(15,'Margaret','Lowe','ccarter@example.org','A3OIB@la*k'),(16,'Anthony','Ruiz','qwilliams@example.net','a0e)t@QsR*'),(17,'Nina','Hodges','kathrynarroyo@example.org','_cy67Xaj_i'),(18,'Gail','Cook','jensenpaul@example.com','1b5NQc(ey%'),(19,'Bruce','Moran','wongann@example.com','n_J03HhiC%'),(20,'Benjamin','Campbell','williamsamy@example.org','@YO%qROk@6'),(21,'Isaac','Smith','elowe@example.net','n)4QTyWq@t'),(22,'Natasha','Wagner','hughesnicole@example.net','!Ys8Jw5mzS'),(23,'Neil','Solis','hgonzalez@example.com','25T%@Nr&%3'),(24,'Shelby','Henry','sierrabyrd@example.com','Iz(zWzXT@4'),(25,'Greg','Sanchez','hernandezterrance@example.net','7Y^r3Oh3(!'),(26,'Riley','Marshall','joshuahall@example.net','C%@3!NGppz'),(27,'Bobby','Torres','ortegakeith@example.org','^y5D7hFw8R'),(28,'Sarah','Lowe','smithamy@example.net','jwo%5RiKR5'),(29,'Aaron','Hoffman','nnichols@example.net','$nPLOfVu$0'),(30,'Cody','Lopez','lisa39@example.com','gg)5kRFfD*');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_results`
--

DROP TABLE IF EXISTS `test_results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `test_results` (
  `test_result_id` int NOT NULL AUTO_INCREMENT,
  `student_id` int DEFAULT NULL,
  `test_score` decimal(5,2) NOT NULL,
  `test_date` date NOT NULL,
  PRIMARY KEY (`test_result_id`),
  KEY `test_results_ibfk_1` (`student_id`),
  CONSTRAINT `test_results_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=506 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_results`
--

LOCK TABLES `test_results` WRITE;
/*!40000 ALTER TABLE `test_results` DISABLE KEYS */;
INSERT INTO `test_results` VALUES (80,25,94.00,'2024-08-06'),(81,25,89.00,'2024-10-27'),(82,28,98.00,'2024-07-11'),(83,7,98.00,'2024-09-03'),(84,30,98.00,'2024-02-17'),(85,11,100.00,'2024-11-26'),(86,24,92.00,'2024-07-20'),(87,26,100.00,'2024-04-24'),(89,24,94.00,'2024-11-13'),(90,11,97.00,'2024-07-31'),(91,3,93.00,'2024-07-02'),(92,13,94.00,'2024-09-03'),(93,4,95.00,'2024-08-22'),(94,25,93.00,'2024-11-09'),(95,14,98.00,'2024-10-06'),(96,29,100.00,'2024-10-01'),(97,23,99.00,'2024-09-10'),(98,2,98.00,'2024-09-20'),(99,26,99.00,'2024-08-14'),(100,14,96.00,'2024-07-28'),(101,7,91.00,'2024-03-29'),(102,14,91.00,'2024-01-29'),(103,12,100.00,'2024-09-02'),(104,23,90.00,'2024-08-03'),(105,14,93.00,'2024-11-09'),(106,28,93.00,'2024-07-29'),(107,9,88.00,'2024-08-20'),(108,12,99.00,'2024-05-28'),(109,16,96.00,'2024-07-10'),(110,14,95.00,'2024-02-10');
/*!40000 ALTER TABLE `test_results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `role` enum('admin','student') NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'student@student.com','student123','student'),(2,'admin@admin.com','admin123','admin'),(12,'stunt@examp.com','$2b$12$Lk2sfvOM4uZkFB0qWNUmqu88XC484.YVo1PtBKm/fo5Qbwn0NoGUq','student'),(14,'stunt@amp.com','$2b$12$aQ9KdtePMU1BernoE.7tletOUNgy5MzU9DeBgTHJwZTj8Bn2B4oDK','admin');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-11 12:29:56
