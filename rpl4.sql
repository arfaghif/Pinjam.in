-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: rpldatabase
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `akun`
--

DROP TABLE IF EXISTS `akun`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `akun` (
  `username` varchar(16) NOT NULL,
  `password` varchar(16) NOT NULL,
  `namalengkap` varchar(45) DEFAULT NULL,
  `alamat` varchar(45) DEFAULT NULL,
  `noktp` varchar(16) DEFAULT NULL,
  `tanggallahir` date DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `akun`
--

LOCK TABLES `akun` WRITE;
/*!40000 ALTER TABLE `akun` DISABLE KEYS */;
INSERT INTO `akun` VALUES ('arpa','tasiq','nopal arpa','tasik','13518000','2000-05-25'),('daprut','inipassword','daffa pp','sby','13518033','2000-09-02'),('ibnu','cahkopo','ibnu sidqi','kopo','13518072','2000-07-05'),('pals','123456','daffa pp','sby','13518033','2000-09-02');
/*!40000 ALTER TABLE `akun` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kendaraan`
--

DROP TABLE IF EXISTS `kendaraan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kendaraan` (
  `IDKend` int NOT NULL AUTO_INCREMENT,
  `username` varchar(16) NOT NULL,
  `namakendaraan` varchar(16) NOT NULL,
  `tahun` year NOT NULL,
  `alamat` varchar(64) NOT NULL,
  `harga` int NOT NULL,
  `deskripsi` varchar(255) NOT NULL,
  `tersediasupir` varchar(8) NOT NULL,
  `tambahan` int NOT NULL,
  PRIMARY KEY (`IDKend`),
  KEY `username` (`username`),
  CONSTRAINT `kendaraan_ibfk_1` FOREIGN KEY (`username`) REFERENCES `akun` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kendaraan`
--

LOCK TABLES `kendaraan` WRITE;
/*!40000 ALTER TABLE `kendaraan` DISABLE KEYS */;
INSERT INTO `kendaraan` VALUES (1,'ibnu','avanza',2004,'Surabayar',170000,'AC dingin, gps built in, audio kencang','n',0),(2,'ibnu','kijang',2011,'Surabayar',250000,'Kijang versi GT Fasilitas lengkap','y',20),(4,'daprut','mersi buluk',1999,'Kopo',70000,'Asik buat pacaran, harga murah, ac dingin','y',20),(6,'ibnu','bmw',2020,'bandung',200000,'Keren bgt','y',20),(7,'ibnu','hino dutro',2002,'kalimantan',20000,'Tangguh','n',0),(8,'ibnu','vespa',2001,'bali',28000,'mad','y',15),(9,'ibnu','alphard',2009,'wuhan',1000000,'nyaman dan mewah','n',0);
/*!40000 ALTER TABLE `kendaraan` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `kontak`
--

DROP TABLE IF EXISTS `kontak`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `kontak` (
  `username` varchar(16) NOT NULL,
  `no_hp` varchar(16) NOT NULL,
  `email` varchar(36) NOT NULL,
  KEY `username` (`username`),
  CONSTRAINT `kontak_ibfk_1` FOREIGN KEY (`username`) REFERENCES `akun` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `kontak`
--

LOCK TABLES `kontak` WRITE;
/*!40000 ALTER TABLE `kontak` DISABLE KEYS */;
INSERT INTO `kontak` VALUES ('daprut','08122202301','daprutkopo@gmail.com'),('ibnu','08122202302','ibnusuroboy@gmail.com');
/*!40000 ALTER TABLE `kontak` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `penyewa`
--

DROP TABLE IF EXISTS `penyewa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `penyewa` (
  `IDPenyewa` int NOT NULL AUTO_INCREMENT,
  `username` varchar(16) NOT NULL,
  PRIMARY KEY (`IDPenyewa`),
  KEY `username` (`username`),
  CONSTRAINT `penyewa_ibfk_1` FOREIGN KEY (`username`) REFERENCES `akun` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `penyewa`
--

LOCK TABLES `penyewa` WRITE;
/*!40000 ALTER TABLE `penyewa` DISABLE KEYS */;
INSERT INTO `penyewa` VALUES (3,'arpa'),(2,'daprut'),(1,'ibnu');
/*!40000 ALTER TABLE `penyewa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supir`
--

DROP TABLE IF EXISTS `supir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supir` (
  `IDSupir` int NOT NULL AUTO_INCREMENT,
  `namalengkap` varchar(45) NOT NULL,
  `noSIM` varchar(16) NOT NULL,
  `notelepon` varchar(12) NOT NULL,
  `IDKend` int NOT NULL,
  PRIMARY KEY (`IDSupir`),
  KEY `IDKend` (`IDKend`),
  CONSTRAINT `supir_ibfk_1` FOREIGN KEY (`IDKend`) REFERENCES `kendaraan` (`IDKend`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supir`
--

LOCK TABLES `supir` WRITE;
/*!40000 ALTER TABLE `supir` DISABLE KEYS */;
INSERT INTO `supir` VALUES (1,'evan kopo','13444444412','082234333433',2);
/*!40000 ALTER TABLE `supir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transaksi`
--

DROP TABLE IF EXISTS `transaksi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transaksi` (
  `IDTransaksi` int NOT NULL AUTO_INCREMENT,
  `IDKend` int NOT NULL,
  `nominal` int NOT NULL,
  `unamepenyewa` varchar(16) NOT NULL,
  `unamepembeli` varchar(16) NOT NULL,
  `konfirmasi` tinyint(1) NOT NULL,
  `status` varchar(16) NOT NULL,
  PRIMARY KEY (`IDTransaksi`),
  KEY `unamepenyewa` (`unamepenyewa`),
  KEY `unamepembeli` (`unamepembeli`),
  CONSTRAINT `transaksi_ibfk_1` FOREIGN KEY (`unamepenyewa`) REFERENCES `akun` (`username`),
  CONSTRAINT `transaksi_ibfk_2` FOREIGN KEY (`unamepembeli`) REFERENCES `akun` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transaksi`
--

LOCK TABLES `transaksi` WRITE;
/*!40000 ALTER TABLE `transaksi` DISABLE KEYS */;
INSERT INTO `transaksi` VALUES (1,6,20000,'ibnu','pals',1,'DITERIMA');
/*!40000 ALTER TABLE `transaksi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ulasan`
--

DROP TABLE IF EXISTS `ulasan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ulasan` (
  `IDUlasan` int NOT NULL AUTO_INCREMENT,
  `IDKend` int NOT NULL,
  `unamepembeli` varchar(16) NOT NULL,
  `review` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`IDUlasan`),
  KEY `IDKend` (`IDKend`),
  KEY `unamepembeli` (`unamepembeli`),
  CONSTRAINT `ulasan_ibfk_1` FOREIGN KEY (`IDKend`) REFERENCES `kendaraan` (`IDKend`),
  CONSTRAINT `ulasan_ibfk_2` FOREIGN KEY (`unamepembeli`) REFERENCES `akun` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ulasan`
--

LOCK TABLES `ulasan` WRITE;
/*!40000 ALTER TABLE `ulasan` DISABLE KEYS */;
INSERT INTO `ulasan` VALUES (1,6,'pals','Nyaman mobilnya, seller rekomen!!');
/*!40000 ALTER TABLE `ulasan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-04-13 14:16:30
