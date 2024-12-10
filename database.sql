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
) ENGINE=InnoDB AUTO_INCREMENT=267 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (262,'Detail action behavior','Why change wear front director above.'),(263,'Truth','Move travel organization firm treat.'),(264,'Music safe enter','Art expect catch suffer lawyer force.'),(265,'Name sport','Option others investment issue myself poor.'),(266,'Physical bag','Fly herself choose stay chance catch four.');
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
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollments`
--

LOCK TABLES `enrollments` WRITE;
/*!40000 ALTER TABLE `enrollments` DISABLE KEYS */;
INSERT INTO `enrollments` VALUES (151,137,266,'2022-11-13','2025-05-25'),(152,158,266,'2020-12-14','2025-11-11'),(153,150,263,'2023-10-15','2025-02-28'),(154,159,262,'2020-08-28','2023-07-07'),(155,149,262,'2020-10-31','2025-06-06'),(156,160,266,'2022-09-29','2025-08-27'),(157,135,263,'2021-02-09','2024-10-19'),(158,145,265,'2021-05-16','2021-06-13'),(159,149,263,'2020-12-06','2022-06-06'),(160,151,266,'2021-07-27','2025-07-30'),(161,131,264,'2022-06-28','2023-07-11'),(162,154,263,'2020-02-15','2022-11-08'),(163,144,262,'2020-01-07','2024-12-03'),(164,132,263,'2023-04-06','2024-03-07'),(165,148,265,'2024-08-07','2025-03-27'),(166,151,266,'2021-06-13','2022-05-29'),(167,131,262,'2021-04-08','2021-08-20'),(168,143,264,'2021-07-18','2023-01-12'),(169,156,266,'2022-11-17','2024-05-01'),(170,139,263,'2022-10-23','2025-08-31'),(171,138,263,'2022-07-28','2024-05-11'),(172,142,262,'2023-11-13','2023-12-23'),(173,133,262,'2020-05-07','2022-01-31'),(174,159,263,'2024-04-15','2024-12-22'),(175,151,266,'2021-02-11','2025-09-20'),(176,149,266,'2023-07-11','2025-03-11'),(177,145,266,'2022-10-24','2024-10-19'),(178,135,264,'2020-07-03','2021-03-02'),(179,136,264,'2020-10-08','2025-06-06'),(180,150,266,'2024-01-31','2025-01-17');
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
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (131,'Regina','Jackson','kellymitchell@example.net','LKac0YZf)T'),(132,'Allison','Benson','waltonjennifer@example.com','YU*m9Yn4@S'),(133,'Walter','Green','laura99@example.net','#l&mLAFOg2'),(134,'Jimmy','Aguilar','hillcourtney@example.com','(M5VYzt@c%'),(135,'Thomas','Sawyer','boltonrobert@example.net','wnyFBYjN&1'),(136,'Dale','Lam','dsilva@example.org','3_y7d@ug*B'),(137,'Catherine','Ingram','andrew33@example.org','a#7KgXp$A!'),(138,'Laurie','Andrews','colin29@example.net','_+6CvHv#%V'),(139,'Christopher','Raymond','cynthiabarnett@example.com','I9sbGq8d#r'),(140,'Daniel','Thompson','curryconnie@example.com','2(o4)wkh^Q'),(141,'Stephanie','Gaines','elizabeth85@example.net','&e4a(CHkP*'),(142,'Kathy','Nelson','zbass@example.org','x)aKp0j7@5'),(143,'Erika','Guzman','mooreapril@example.com','gvNFtXzG^3'),(144,'Brooke','Mcdonald','melissajones@example.org','(BEd9UqmW)'),(145,'Sarah','Smith','randydavis@example.com','@g3Zp*171%'),(146,'Jennifer','Hernandez','john22@example.org','2BRePXBQ%z'),(147,'Chelsea','Jackson','ikeller@example.org','a$#6%MsZG4'),(148,'Thomas','Gonzalez','debbiecameron@example.org','I9I@AQIr_S'),(149,'Jonathan','Henderson','jacobslindsay@example.net','!27Xueovcg'),(150,'Desiree','Allen','ibarratracy@example.com','2dbU3@o1_0'),(151,'David','Lewis','jeffrey69@example.net','$yMOY!%oo8'),(152,'Kim','Martinez','allisonamy@example.org','!#4WLZaDz%'),(153,'Matthew','Cantu','tammy51@example.org','GbzC^8Yie&'),(154,'Dale','Bush','michaeljackson@example.com','m9m1ZBd@!q'),(155,'Richard','Williams','veronica45@example.net','+J+9ofVsC8'),(156,'Christopher','Poole','davidporter@example.net','B(8PyHx)#g'),(157,'Jody','Walker','fieldskatie@example.org','ME*F9tGi*g'),(158,'Timothy','Guzman','nfrench@example.net','6MI8QDwt(b'),(159,'Jessica','Hall','dpeck@example.com','_jU0MCqvu_'),(160,'Robert','White','andersonlisa@example.com','$VR7yo%tJ5');
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
  `student_id` int NOT NULL,
  `test_score` decimal(5,2) NOT NULL,
  `test_date` date NOT NULL,
  PRIMARY KEY (`test_result_id`),
  KEY `test_results_ibfk_1` (`student_id`),
  CONSTRAINT `test_results_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=474 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_results`
--

LOCK TABLES `test_results` WRITE;
/*!40000 ALTER TABLE `test_results` DISABLE KEYS */;
INSERT INTO `test_results` VALUES (444,155,91.00,'2024-07-10'),(445,133,98.00,'2024-09-26'),(446,131,94.00,'2024-03-23'),(447,160,92.00,'2024-01-13'),(448,153,94.00,'2024-06-16'),(449,154,99.00,'2024-08-31'),(450,147,97.00,'2024-04-09'),(451,146,95.00,'2024-02-06'),(452,160,89.00,'2024-04-17'),(453,151,92.00,'2024-01-27'),(454,134,100.00,'2024-10-04'),(455,138,98.00,'2024-10-30'),(456,139,89.00,'2024-02-09'),(457,159,97.00,'2024-10-30'),(458,136,93.00,'2024-05-20'),(459,137,93.00,'2024-02-29'),(460,132,88.00,'2024-06-09'),(461,140,100.00,'2024-06-19'),(462,152,97.00,'2024-08-04'),(463,141,97.00,'2024-09-12'),(464,150,91.00,'2024-06-10'),(465,146,94.00,'2024-08-11'),(466,136,99.00,'2024-11-13'),(467,145,89.00,'2024-02-05'),(468,141,92.00,'2024-05-04'),(469,136,91.00,'2024-11-25'),(470,142,95.00,'2024-01-18'),(471,132,98.00,'2024-02-02'),(472,145,95.00,'2024-09-06'),(473,160,97.00,'2024-03-14');
/*!40000 ALTER TABLE `test_results` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-12-10 14:18:38
