-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: listas
-- ------------------------------------------------------
-- Server version	11.5.2-MariaDB

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add administrador',7,'add_administrador'),(26,'Can change administrador',7,'change_administrador'),(27,'Can delete administrador',7,'delete_administrador'),(28,'Can view administrador',7,'view_administrador'),(29,'Can add directivos',8,'add_directivos'),(30,'Can change directivos',8,'change_directivos'),(31,'Can delete directivos',8,'delete_directivos'),(32,'Can view directivos',8,'view_directivos'),(33,'Can add horario',9,'add_horario'),(34,'Can change horario',9,'change_horario'),(35,'Can delete horario',9,'delete_horario'),(36,'Can view horario',9,'view_horario'),(37,'Can add periodo escolar',10,'add_periodoescolar'),(38,'Can change periodo escolar',10,'change_periodoescolar'),(39,'Can delete periodo escolar',10,'delete_periodoescolar'),(40,'Can view periodo escolar',10,'view_periodoescolar'),(41,'Can add dia asistencia',11,'add_diaasistencia'),(42,'Can change dia asistencia',11,'change_diaasistencia'),(43,'Can delete dia asistencia',11,'delete_diaasistencia'),(44,'Can view dia asistencia',11,'view_diaasistencia'),(45,'Can add justificacion',12,'add_justificacion'),(46,'Can change justificacion',12,'change_justificacion'),(47,'Can delete justificacion',12,'delete_justificacion'),(48,'Can view justificacion',12,'view_justificacion'),(49,'Can add pd fhorario',13,'add_pdfhorario'),(50,'Can change pd fhorario',13,'change_pdfhorario'),(51,'Can delete pd fhorario',13,'delete_pdfhorario'),(52,'Can view pd fhorario',13,'view_pdfhorario'),(53,'Can add profesor',14,'add_profesor'),(54,'Can change profesor',14,'change_profesor'),(55,'Can delete profesor',14,'delete_profesor'),(56,'Can view profesor',14,'view_profesor');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'GestionAsistencias','administrador'),(11,'GestionAsistencias','diaasistencia'),(8,'GestionAsistencias','directivos'),(9,'GestionAsistencias','horario'),(12,'GestionAsistencias','justificacion'),(13,'GestionAsistencias','pdfhorario'),(10,'GestionAsistencias','periodoescolar'),(14,'GestionAsistencias','profesor'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'GestionAsistencias','0001_initial','2024-10-24 13:16:29.869940'),(2,'contenttypes','0001_initial','2024-10-24 13:16:30.856280'),(3,'auth','0001_initial','2024-10-24 13:16:41.939890'),(4,'admin','0001_initial','2024-10-24 13:16:43.713851'),(5,'admin','0002_logentry_remove_auto_add','2024-10-24 13:16:43.773824'),(6,'admin','0003_logentry_add_action_flag_choices','2024-10-24 13:16:43.804806'),(7,'contenttypes','0002_remove_content_type_name','2024-10-24 13:16:45.167109'),(8,'auth','0002_alter_permission_name_max_length','2024-10-24 13:16:46.033456'),(9,'auth','0003_alter_user_email_max_length','2024-10-24 13:16:46.609343'),(10,'auth','0004_alter_user_username_opts','2024-10-24 13:16:46.692901'),(11,'auth','0005_alter_user_last_login_null','2024-10-24 13:16:47.475817'),(12,'auth','0006_require_contenttypes_0002','2024-10-24 13:16:47.502529'),(13,'auth','0007_alter_validators_add_error_messages','2024-10-24 13:16:47.537875'),(14,'auth','0008_alter_user_username_max_length','2024-10-24 13:16:47.984972'),(15,'auth','0009_alter_user_last_name_max_length','2024-10-24 13:16:48.574936'),(16,'auth','0010_alter_group_name_max_length','2024-10-24 13:16:48.995150'),(17,'auth','0011_update_proxy_permissions','2024-10-24 13:16:49.083599'),(18,'auth','0012_alter_user_first_name_max_length','2024-10-24 13:16:49.550445'),(19,'sessions','0001_initial','2024-10-24 13:16:51.624935'),(20,'GestionAsistencias','0002_alter_periodoescolar_idperiodo','2024-11-03 14:39:59.780928'),(21,'GestionAsistencias','0003_alter_periodoescolar_fechafin_and_more','2024-11-03 15:34:05.980646');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('0pl95iu7e093956d3mwxwo68c9veewgq','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t5Pdj:VF_PqRxhyIimx2Hcuwo8j_VZQf3N6F1Da06Rd675xto','2024-11-11 07:18:35.155021'),('0vsunnvzmt775flox3w308j2dvnkrc1x','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkRpcmVjdGl2byJ9:1t7P6g:QyAoV0e675LFrvg-45A4s6X8SWyzmuEqMTZkdVBVuAM','2024-11-16 19:08:42.304798'),('3zcn05azx3uwkh2n4gthvkt1exobhs4g','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t5Pwg:iGmrH2o4KDMLt0F5rREtsxRDEflnYHK_C45JkwQM7MQ','2024-11-11 07:38:10.780826'),('3zoltkkp3kenui7id3l87jcas73xhlz5','e30:1t7QEl:cxNr8S03HtMp5Xj005YLoX2qWTg2uRovuGKo9nbrIlI','2024-11-16 20:21:07.450175'),('5zpd5r30pczs9au2zznyhjd83y8rr0yq','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t5qgw:3MxStCdt5u_TIh4XvP0oL9WsAqy6LpC6DA2la2-QVk8','2024-11-12 12:11:42.573214'),('6de88yp938p4p6g1c158lpn9mta5t0ve','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkRpcmVjdGl2byJ9:1t7QFo:2T3M5wN47QI1Qb2Vy2Z45RtUhHBt5hgFPn75aX_A438','2024-11-16 20:22:12.653105'),('6ya6pmnxqdsc5warys0d4d1eyteany1v','e30:1t7R8o:APipyRXJEo8DzR96eL9EByPpdCwQWLStWw4kPr5Byfw','2024-11-16 21:19:02.841964'),('834z0xv1p28el437ixvvfcplrxkcggv2','eyJ1c2VyX2lkIjo5LCJ1c2VyX3JvbCI6IlByb2Zlc29yIn0:1t7yMw:0wdoxFqmXBtSYC0X157j8d4eyHAXATOMUmWrDXvr4UM','2024-11-18 08:47:50.921418'),('90iv0bp4ooowvuuohjzi7qbkp7grcdpb','e30:1t7yiR:OslFj3JU7R7AdLfzveAxYEFdGyEuMieYBD2RGi47IiA','2024-11-18 09:10:03.117239'),('a7u1fjmi8fx8ygt119epvy0zd78bu5mw','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t5QBT:0VE78W1qHxAKlhmc1LuEy0i0qw-d8CgUATDs7CV-l-M','2024-11-11 07:53:27.135970'),('gcfzg2kkej0gl5j2fl5jyhyr822a8kyk','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkRpcmVjdGl2byJ9:1t6zt3:khaUGI1W4AlbLiq4dx8Ppn6KcfDswD_5HcxOsZ_GTQo','2024-11-15 16:12:57.373401'),('hanqbhq8toqwwkb4vkis9a0yu5745dei','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t5DeW:wx7EMahDSWbrRzA01DEYhwJsRPDMYMohQXowYRlSNSY','2024-11-10 18:30:36.718313'),('i71x96q8zj5ajhynjcpuhzgdois6mato','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t5Q6Q:2kESixaXrt_YBfiGRBJz_pM-P5AVau8kJXg0BY4-0ho','2024-11-11 07:48:14.807089'),('ifnz5d6f0dgaqxig63z2kjbndmji5xql','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IlByb2Zlc29yIn0:1t5RYR:RIMcgjanVO4FiNPy7nQkfKX1BelCD8zShxFlNASzmQk','2024-11-11 09:21:15.817129'),('k7nfsk2pvcmy45w66qmwjqxqm926vk0j','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IlByb2Zlc29yIn0:1t5Rx0:eRQuKekv-BGG8bTd0cC5-T8K6iBJXoQqjKfhMIHn3WI','2024-11-11 09:46:38.413460'),('k934w90zp1bkpnck8l7kwghlcsz9fjj2','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkRpcmVjdGl2byJ9:1t7Qay:757vtFAT9YM1k0eQfEh70og9M0xWsruRfKk33zeJp1U','2024-11-16 20:44:04.228283'),('qn10rcgrblmrwdnio93dkx7maflhb6k6','eyJ1c2VyX2lkIjoyLCJ1c2VyX3JvbCI6IlByb2Zlc29yIn0:1t5RBq:XuGICwNhDCmTK8wQ0gS4LfDERPCwFjpq4XcwKkyqgJE','2024-11-11 08:57:54.820272'),('sm2wx0zkgj1abnmcfuefd6u05z8pf4lf','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkRpcmVjdGl2byJ9:1t6zVN:7SEnXViyWuFUp5s_PyoBhW-4O5BQJkjYX_tuqaoJm5c','2024-11-15 15:48:29.035379'),('tcp8m3oug0kc87ko480a3a5ofu1s4d7q','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkRpcmVjdGl2byJ9:1t7zJ6:5mBXC_oEkX_n6jI7GZFiMpOTw4pwM_A5B78oGjp790M','2024-11-18 09:47:56.549597'),('utmgyekl4xc2jor67abkx8q4xa3j54xy','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t5S1O:hBhCburyFtdJnr7GG3_5Atj_p3DJD5sTc0m-k2TezCc','2024-11-11 09:51:10.526911'),('wjcmsm1045b4ferslgp5zvxg3cdaerrr','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t4tYD:kavjl_zzmm-ENZZlSSPOsHgR9EAx2SC9LSj1Kg7TSn4','2024-11-09 21:02:45.052772'),('wsf4t7bv4xbukoz7wo8tbiwj0t9aewh7','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IlByb2Zlc29yIn0:1t5ULq:6jsE-7CIrALZ7mdvSZZCN5w367D1qtgT6O7RKO10L-g','2024-11-11 12:20:26.156244'),('wu4l9qz9g4axa6k4nd4qrmjsvkiinn6c','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkRpcmVjdGl2byJ9:1t7Qc5:BFAULBtIPNBDBCALKptn54aQEjB6cTcmYIYDSVFwiZ0','2024-11-16 20:45:13.069402'),('xhwz0samg0hq9tvreh8jbli0dsov8cpl','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t5ocx:OKxDhvyRIqiu8RhsdPlYTKXbqCoecredQPXs-6962R4','2024-11-12 09:59:27.363773'),('xnovrkt4e6genjz2ce2oihls6d3ckj6o','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t5qMQ:yEtMIqGbqUAA9IIc1BHpkeI1BX_hvnhV4vv3P7QYlqU','2024-11-12 11:50:30.685146'),('xqw3cw0v80hjudndfyvbp6ntwoh64poh','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t5pCA:3JnrIKAlufvrAJZcB98UL9b5-Qbwy_oYoN0fzkwplnU','2024-11-12 10:35:50.253570'),('xur93s2qvpp851507wcts6io1l5qdgyj','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkRpcmVjdGl2byJ9:1t6zj4:Wx5GgjwRHKuSjcm86GcZnyOi8pAA3sAFh_kRcSHQ65g','2024-11-15 16:02:38.013614'),('yjzfyj3eebco7gpf31yj6paivby3cbnl','eyJ1c2VyX2lkIjoxLCJ1c2VyX3JvbCI6IkFkbWluaXN0cmFkb3IifQ:1t5Q9M:hFAP3mRthTfQ6LK2pAj1x_Hx0Uc4Z1eyd4N-Om8HB4U','2024-11-11 07:51:16.944913');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionasistencias_administrador`
--

DROP TABLE IF EXISTS `gestionasistencias_administrador`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionasistencias_administrador` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50) NOT NULL,
  `Matricula` varchar(200) NOT NULL,
  `Contrasena` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionasistencias_administrador`
--

LOCK TABLES `gestionasistencias_administrador` WRITE;
/*!40000 ALTER TABLE `gestionasistencias_administrador` DISABLE KEYS */;
INSERT INTO `gestionasistencias_administrador` VALUES (1,'Carlos Martínez','CM','admin1');
/*!40000 ALTER TABLE `gestionasistencias_administrador` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionasistencias_diaasistencia`
--

DROP TABLE IF EXISTS `gestionasistencias_diaasistencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionasistencias_diaasistencia` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `fecha_y_hora` datetime(6) NOT NULL,
  `Tipo` varchar(45) NOT NULL,
  `idHorario_id` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `GestionAsistencias_d_idHorario_id_8fa5b0da_fk_GestionAs` (`idHorario_id`),
  CONSTRAINT `GestionAsistencias_d_idHorario_id_8fa5b0da_fk_GestionAs` FOREIGN KEY (`idHorario_id`) REFERENCES `gestionasistencias_horario` (`idHorario`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionasistencias_diaasistencia`
--

LOCK TABLES `gestionasistencias_diaasistencia` WRITE;
/*!40000 ALTER TABLE `gestionasistencias_diaasistencia` DISABLE KEYS */;
INSERT INTO `gestionasistencias_diaasistencia` VALUES (1,'2024-09-25 08:15:00.000000','Asistencia',1),(2,'2024-09-25 17:00:00.000000','Retardo',1),(3,'2024-09-25 08:15:00.000000','Asistencia',2),(4,'2024-09-25 17:00:00.000000','Retardo',2),(14,'2024-11-04 09:44:05.256091','Asistencia',12);
/*!40000 ALTER TABLE `gestionasistencias_diaasistencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionasistencias_directivos`
--

DROP TABLE IF EXISTS `gestionasistencias_directivos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionasistencias_directivos` (
  `idDirectivos` bigint(20) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Apellidos` varchar(45) NOT NULL,
  `Matricula` varchar(200) NOT NULL,
  `Correo` varchar(150) NOT NULL,
  `Contrasena` varchar(200) NOT NULL,
  PRIMARY KEY (`idDirectivos`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionasistencias_directivos`
--

LOCK TABLES `gestionasistencias_directivos` WRITE;
/*!40000 ALTER TABLE `gestionasistencias_directivos` DISABLE KEYS */;
INSERT INTO `gestionasistencias_directivos` VALUES (1,'Sony','dasdas','hola1','no@s','1234'),(3,'Jose','dasdas','JDS','hola','432432'),(6,'Jose','dasdas','hola123','dasdsa@da','12345'),(8,'Jose','dsad','CM12323','dasds@das','1234');
/*!40000 ALTER TABLE `gestionasistencias_directivos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionasistencias_horario`
--

DROP TABLE IF EXISTS `gestionasistencias_horario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionasistencias_horario` (
  `idHorario` bigint(20) NOT NULL AUTO_INCREMENT,
  `Lunes` time(6) DEFAULT NULL,
  `Martes` time(6) DEFAULT NULL,
  `Miercoles` time(6) DEFAULT NULL,
  `Jueves` time(6) DEFAULT NULL,
  `Viernes` time(6) DEFAULT NULL,
  `idPeriodo_id` bigint(20) NOT NULL,
  `idProfesor_id` bigint(20) NOT NULL,
  PRIMARY KEY (`idHorario`),
  KEY `GestionAsistencias_h_idPeriodo_id_276be164_fk_GestionAs` (`idPeriodo_id`),
  KEY `GestionAsistencias_h_idProfesor_id_daccb80d_fk_GestionAs` (`idProfesor_id`),
  CONSTRAINT `GestionAsistencias_h_idPeriodo_id_276be164_fk_GestionAs` FOREIGN KEY (`idPeriodo_id`) REFERENCES `gestionasistencias_periodoescolar` (`idPeriodo`),
  CONSTRAINT `GestionAsistencias_h_idProfesor_id_daccb80d_fk_GestionAs` FOREIGN KEY (`idProfesor_id`) REFERENCES `gestionasistencias_profesor` (`idProfesor`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionasistencias_horario`
--

LOCK TABLES `gestionasistencias_horario` WRITE;
/*!40000 ALTER TABLE `gestionasistencias_horario` DISABLE KEYS */;
INSERT INTO `gestionasistencias_horario` VALUES (1,'08:30:00.000000',NULL,NULL,NULL,NULL,2,2),(2,'08:30:00.000000','22:52:00.000000','21:08:00.000000',NULL,NULL,1,1),(11,'21:11:00.000000',NULL,NULL,NULL,NULL,1,3),(12,'08:09:00.000000',NULL,NULL,NULL,NULL,2,1);
/*!40000 ALTER TABLE `gestionasistencias_horario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionasistencias_justificacion`
--

DROP TABLE IF EXISTS `gestionasistencias_justificacion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionasistencias_justificacion` (
  `idJustificacion` bigint(20) NOT NULL AUTO_INCREMENT,
  `motivo` varchar(300) NOT NULL,
  `estado` varchar(50) NOT NULL,
  `idDiaAsistencia_id` bigint(20) NOT NULL,
  PRIMARY KEY (`idJustificacion`),
  KEY `GestionAsistencias_j_idDiaAsistencia_id_20267745_fk_GestionAs` (`idDiaAsistencia_id`),
  CONSTRAINT `GestionAsistencias_j_idDiaAsistencia_id_20267745_fk_GestionAs` FOREIGN KEY (`idDiaAsistencia_id`) REFERENCES `gestionasistencias_diaasistencia` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionasistencias_justificacion`
--

LOCK TABLES `gestionasistencias_justificacion` WRITE;
/*!40000 ALTER TABLE `gestionasistencias_justificacion` DISABLE KEYS */;
INSERT INTO `gestionasistencias_justificacion` VALUES (3,'Me enferme','Aprobado',3),(4,'Me atropellaron','Pendiente',4),(5,'Trafico','Aprobado',14);
/*!40000 ALTER TABLE `gestionasistencias_justificacion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionasistencias_pdfhorario`
--

DROP TABLE IF EXISTS `gestionasistencias_pdfhorario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionasistencias_pdfhorario` (
  `idPDFhorario` bigint(20) NOT NULL AUTO_INCREMENT,
  `FechaModificacion` datetime(6) NOT NULL,
  `Nombre` varchar(300) NOT NULL,
  `horario_pdf` varchar(255) DEFAULT NULL,
  `idHorario_id` bigint(20) NOT NULL,
  PRIMARY KEY (`idPDFhorario`),
  KEY `GestionAsistencias_p_idHorario_id_ee2e356c_fk_GestionAs` (`idHorario_id`),
  CONSTRAINT `GestionAsistencias_p_idHorario_id_ee2e356c_fk_GestionAs` FOREIGN KEY (`idHorario_id`) REFERENCES `gestionasistencias_horario` (`idHorario`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionasistencias_pdfhorario`
--

LOCK TABLES `gestionasistencias_pdfhorario` WRITE;
/*!40000 ALTER TABLE `gestionasistencias_pdfhorario` DISABLE KEYS */;
/*!40000 ALTER TABLE `gestionasistencias_pdfhorario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionasistencias_periodoescolar`
--

DROP TABLE IF EXISTS `gestionasistencias_periodoescolar`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionasistencias_periodoescolar` (
  `idPeriodo` bigint(20) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(60) NOT NULL,
  `FechaInicio` date NOT NULL,
  `FechaFin` date NOT NULL,
  PRIMARY KEY (`idPeriodo`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionasistencias_periodoescolar`
--

LOCK TABLES `gestionasistencias_periodoescolar` WRITE;
/*!40000 ALTER TABLE `gestionasistencias_periodoescolar` DISABLE KEYS */;
INSERT INTO `gestionasistencias_periodoescolar` VALUES (1,'Otoño 2024','2024-01-15','2024-04-30'),(2,'Verano 2026','2024-05-01','2024-12-19'),(5,'Inviernos 2025','2024-11-04','2024-11-30');
/*!40000 ALTER TABLE `gestionasistencias_periodoescolar` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gestionasistencias_profesor`
--

DROP TABLE IF EXISTS `gestionasistencias_profesor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gestionasistencias_profesor` (
  `idProfesor` bigint(20) NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Apellidos` varchar(45) NOT NULL,
  `Contrasena` varchar(200) NOT NULL,
  `Matricula` varchar(200) NOT NULL,
  `Correo` varchar(150) NOT NULL,
  `imagen_rostro` varchar(255) DEFAULT NULL,
  `idDirectivos_id` bigint(20) NOT NULL,
  PRIMARY KEY (`idProfesor`),
  KEY `GestionAsistencias_p_idDirectivos_id_b89b531f_fk_GestionAs` (`idDirectivos_id`),
  CONSTRAINT `GestionAsistencias_p_idDirectivos_id_b89b531f_fk_GestionAs` FOREIGN KEY (`idDirectivos_id`) REFERENCES `gestionasistencias_directivos` (`idDirectivos`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gestionasistencias_profesor`
--

LOCK TABLES `gestionasistencias_profesor` WRITE;
/*!40000 ALTER TABLE `gestionasistencias_profesor` DISABLE KEYS */;
INSERT INTO `gestionasistencias_profesor` VALUES (1,'Sony','Mendieta Chimal','1234','SN1','no@dsa','C:\\Users\\Jessica\\Desktop\\Estancia II\\media\\rostros\\rostro_1.jpeg',1),(2,'Elon','Musk','123','ELMSK','no','C:\\Users\\Jessica\\Desktop\\Estancia II\\media\\rostros\\rostro_2.jpeg',1),(3,'Vegetaa','Luque','123','VG777','no','C:\\Users\\Jessica\\Desktop\\Estancia II\\media\\rostros\\rostro_3.jpeg',1),(4,'alberg','Perez','123454','P555','dasdsa@da','C:\\Users\\Jessica\\Desktop\\Estancia II\\media\\rostros\\rostro_4.jpeg',1),(9,'Jorge','Alejandro','123','JGA','SI','C:\\Users\\Jessica\\Desktop\\Estancia II\\media\\rostros\\rostro_9.jpeg',1);
/*!40000 ALTER TABLE `gestionasistencias_profesor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'listas'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-11-04 10:06:29
