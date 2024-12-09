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
) ENGINE=InnoDB AUTO_INCREMENT=254 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `courses`
--

LOCK TABLES `courses` WRITE;
/*!40000 ALTER TABLE `courses` DISABLE KEYS */;
INSERT INTO `courses` VALUES (200,'CS Elective','computer theory with engineering.'),(201,'Data Science','summarizes the data in a meaningful way which enables us to generate insights from it.');
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
) ENGINE=InnoDB AUTO_INCREMENT=151 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrollments`
--

LOCK TABLES `enrollments` WRITE;
/*!40000 ALTER TABLE `enrollments` DISABLE KEYS */;
INSERT INTO `enrollments` VALUES (100,1,200,'2024-12-09','2024-12-09'),(101,2,200,'2024-12-09','2024-12-14'),(102,3,201,'2024-12-09','2024-12-10'),(103,4,201,'2024-12-09','2024-12-10'),(104,5,201,'2024-12-09','2024-12-10'),(105,6,200,'2024-12-09','2024-12-14'),(106,7,200,'2024-12-09','2024-12-14'),(107,8,200,'2024-12-09','2024-12-14'),(108,9,200,'2024-12-09','2024-12-14'),(109,10,200,'2024-12-09','2024-12-14'),(111,11,200,'2024-12-10','2026-12-10'),(112,12,201,'2024-12-09','2024-12-10'),(113,13,201,'2024-12-09','2024-12-10'),(114,14,200,'2024-12-09','2024-12-14'),(115,15,200,'2024-12-09','2024-12-14'),(116,16,200,'2024-12-09','2024-12-14'),(117,17,201,'2024-12-09','2024-12-10'),(118,18,200,'2024-12-09','2024-12-14'),(119,19,201,'2024-12-09','2024-12-10'),(120,20,201,'2024-12-09','2024-12-10'),(121,21,201,'2024-12-09','2024-12-10'),(122,22,201,'2024-12-09','2024-12-10'),(123,23,201,'2024-12-09','2024-12-10'),(124,24,200,'2024-12-09','2024-12-14'),(125,25,200,'2024-12-09','2024-12-14'),(126,26,200,'2024-12-09','2024-12-14'),(127,27,201,'2024-12-09','2024-12-10'),(128,28,201,'2024-12-09','2024-12-10'),(129,29,200,'2024-12-09','2024-12-14'),(130,30,200,'2024-12-09','2024-12-10');
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
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Karen Angela','Realubit','angela@gmail.com','ftgbnutwqa'),(2,'Jadelyn','Bernabe','bernabe@gmail.com','gtghtswaff'),(3,'Rashel','Gadiano','gadiano@gmail.com','yhrewqahkh'),(4,'Denz Kayla Marie','Gabaldon','gabaldon@gmail.com','hopfrabnmd'),(5,'Jose Wilson','Almonte','almonte@gmail.com','yugrdswqaz'),(6,'Mark Danielle','Lucero','lucero@gmail.com','grewxvbmop'),(7,'Cassandra','Cayao','cayao@gmail.com','plmnjkoiuh'),(8,'Juliet','Rey','rey@gmail.com','bvgytfcxdr'),(9,'Chinnie Mae','Abad','abad@gmail.com','eszaqwesxc'),(10,'Issa Mae','Rustia','rustia@gmail.com','vbgtrfhjki'),(11,'Mark Joseph','Alilano','alilano@gmail.com','htfedsqazx'),(12,'John Rafael','Macalinao','macalinao@gmail.com','hjmngtdesx'),(13,'John Vincent','Labotoy','labotoy@gmail.com','hknlydswcg'),(14,'Mary Jobelle','Abreu','abreu@gmail.com','hnvfredswq'),(15,'Stephanie Rose','Aguda','aguda@gmail.com','gbnmvvfdes'),(16,'Dansel','Ranola','ranola@gmail.com','ftgplokiuj'),(17,'Dm','Dalanon','dalanon@gmail.com','jjuuhhtfgr'),(18,'Irish Cristel','Roll','roll@gmail.com','gtyffedsww'),(19,'Ivan Darry','Pono','pono@gmail.com','ftrdeewsjk'),(20,'Kyla','Decatoria','decatoria@gmail.com','kkjygbnmvv'),(21,'Siradz','Sahiddin','sahiddin@gmail.com','gthnbvfred'),(22,'Mary Mae','Apilan','apilan@gmail.com','ghnbvcdewq'),(23,'Kurt Justine','Realubit','justine@gmail.com','aszxdrtyui'),(24,'Rianne','Gardoce','gardoce@gmail.com','gtyhnbgtrf'),(25,'Judy','Visabella','visabella@gmail.com','erfvplmnju'),(26,'John Wynne','Jeresano','jeresano@gmail.com','ceswqghbtr'),(27,'Darwin','Velasco','velasco@gmail.com','decswercv'),(28,'Shai Mae','Andes','andes@gmail.com','frghjklmnb'),(29,'Krisha Chynna','Realubit','chynna@gmail.com','vcxzasdfgh'),(30,'Michael','Austria','austria@gmail.com','ghtbnhfdde');
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
) ENGINE=InnoDB AUTO_INCREMENT=344 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_results`
--

LOCK TABLES `test_results` WRITE;
/*!40000 ALTER TABLE `test_results` DISABLE KEYS */;
INSERT INTO `test_results` VALUES (301,1,90.00,'2022-12-02'),(302,2,67.00,'2022-12-02'),(303,3,99.00,'2022-12-02'),(304,4,90.00,'2022-12-02'),(305,5,98.00,'2022-12-02'),(306,6,96.00,'2022-12-02'),(307,7,94.00,'2022-12-02'),(308,8,99.00,'2022-12-02'),(309,9,98.00,'2022-12-02'),(310,10,93.00,'2022-12-02'),(311,11,90.00,'2022-12-02'),(312,12,90.00,'2022-12-02'),(313,13,91.00,'2022-12-02'),(314,14,99.00,'2022-12-02'),(315,15,89.00,'2022-12-02'),(316,16,87.00,'2022-12-02'),(317,17,81.00,'2022-12-02'),(318,18,89.00,'2022-12-02'),(319,19,89.00,'2022-12-02'),(320,20,98.00,'2022-12-02'),(321,21,93.00,'2022-12-02'),(322,22,92.00,'2022-12-02'),(323,23,91.00,'2022-12-02'),(324,24,99.00,'2022-12-02'),(325,25,91.00,'2022-12-02'),(326,26,98.00,'2022-12-02'),(327,27,96.00,'2022-12-02'),(328,28,94.00,'2022-12-02'),(329,29,96.00,'2022-12-02'),(330,30,90.00,'2022-12-02');
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

-- Dump completed on 2024-12-10  7:40:01
