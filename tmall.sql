# Host: 127.0.0.1  (Version: 5.5.15)
# Date: 2017-05-07 14:35:18
# Generator: MySQL-Front 5.3  (Build 4.269)

/*!40101 SET NAMES utf8 */;

#
# Structure for table "auth_group"
#

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "auth_group"
#


#
# Structure for table "captcha_captchastore"
#

DROP TABLE IF EXISTS `captcha_captchastore`;
CREATE TABLE `captcha_captchastore` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `challenge` varchar(32) NOT NULL,
  `response` varchar(32) NOT NULL,
  `hashkey` varchar(40) NOT NULL,
  `expiration` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `hashkey` (`hashkey`)
) ENGINE=InnoDB AUTO_INCREMENT=66 DEFAULT CHARSET=utf8;

#
# Data for table "captcha_captchastore"
#

INSERT INTO `captcha_captchastore` VALUES (53,'XBDQ','xbdq','264c7b84b36a2aee3f3ef144558215cdd68f21bf','2017-05-07 00:34:41'),(56,'XNAP','xnap','0344ae0f9e4390e11593e433a3500f814860830d','2017-05-07 00:42:09'),(57,'LSNA','lsna','6d1603aa50223405d92489ae9de44196578d6d1f','2017-05-07 00:42:10'),(58,'KOWU','kowu','47aabd6c576c390751e1c605995008aef1f2f331','2017-05-07 00:42:11'),(59,'ZOTG','zotg','304bf1903cde0d9e76a6375c774de51bb2054ca7','2017-05-07 00:42:13'),(60,'YCRC','ycrc','afb13b13694ab23139a346f810c1c62e64d4ea60','2017-05-07 00:42:14'),(61,'ZIJV','zijv','22a193af870fe3fc97a0845d02b564ad224e169a','2017-05-07 12:44:44'),(62,'EFMS','efms','ccc81d30e65ba0718c435ce45b685230e7ad747e','2017-05-07 12:44:46'),(63,'YMTV','ymtv','87c1d25da811eb7f3cc98e16ac91a38c3625716b','2017-05-07 12:46:18'),(64,'EQBW','eqbw','4f0a7e935d0c7a9be8688eae250cab589a27ed39','2017-05-07 12:46:19'),(65,'UXOX','uxox','e47b7df5902fbbc8d4c8b8f378fc8c6f428c225a','2017-05-07 12:46:34');

#
# Structure for table "django_content_type"
#

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;

#
# Data for table "django_content_type"
#

INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(2,'auth','permission'),(3,'auth','group'),(4,'contenttypes','contenttype'),(5,'sessions','session'),(6,'users','userprofile'),(7,'users','emailverifyrecord'),(8,'product','category'),(9,'product','property'),(10,'product','product'),(11,'product','propertyvalue'),(12,'product','productimage'),(13,'product','review'),(14,'operation','order'),(15,'operation','orderitem'),(16,'xadmin','bookmark'),(17,'xadmin','usersettings'),(18,'xadmin','userwidget'),(19,'xadmin','log'),(20,'captcha','captchastore');

#
# Structure for table "auth_permission"
#

DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=80 DEFAULT CHARSET=utf8;

#
# Data for table "auth_permission"
#

INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can add group',3,'add_group'),(9,'Can change group',3,'change_group'),(10,'Can delete group',3,'delete_group'),(11,'Can view group',3,'view_group'),(12,'Can view permission',2,'view_permission'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add 用户信息',6,'add_userprofile'),(22,'Can change 用户信息',6,'change_userprofile'),(23,'Can delete 用户信息',6,'delete_userprofile'),(24,'Can add 邮件验证码',7,'add_emailverifyrecord'),(25,'Can change 邮件验证码',7,'change_emailverifyrecord'),(26,'Can delete 邮件验证码',7,'delete_emailverifyrecord'),(27,'Can view 邮件验证码',7,'view_emailverifyrecord'),(28,'Can view 用户信息',6,'view_userprofile'),(29,'Can add 商品分类',8,'add_category'),(30,'Can change 商品分类',8,'change_category'),(31,'Can delete 商品分类',8,'delete_category'),(32,'Can add 属性',9,'add_property'),(33,'Can change 属性',9,'change_property'),(34,'Can delete 属性',9,'delete_property'),(35,'Can add 产品表',10,'add_product'),(36,'Can change 产品表',10,'change_product'),(37,'Can delete 产品表',10,'delete_product'),(38,'Can add 属性值',11,'add_propertyvalue'),(39,'Can change 属性值',11,'change_propertyvalue'),(40,'Can delete 属性值',11,'delete_propertyvalue'),(41,'Can add 产品图片',12,'add_productimage'),(42,'Can change 产品图片',12,'change_productimage'),(43,'Can delete 产品图片',12,'delete_productimage'),(44,'Can add 产品评价',13,'add_review'),(45,'Can change 产品评价',13,'change_review'),(46,'Can delete 产品评价',13,'delete_review'),(47,'Can view 商品分类',8,'view_category'),(48,'Can view 产品表',10,'view_product'),(49,'Can view 产品图片',12,'view_productimage'),(50,'Can view 属性',9,'view_property'),(51,'Can view 属性值',11,'view_propertyvalue'),(52,'Can view 产品评价',13,'view_review'),(53,'Can add 订单',14,'add_order'),(54,'Can change 订单',14,'change_order'),(55,'Can delete 订单',14,'delete_order'),(56,'Can add 订单项',15,'add_orderitem'),(57,'Can change 订单项',15,'change_orderitem'),(58,'Can delete 订单项',15,'delete_orderitem'),(59,'Can view 订单',14,'view_order'),(60,'Can view 订单项',15,'view_orderitem'),(61,'Can add Bookmark',16,'add_bookmark'),(62,'Can change Bookmark',16,'change_bookmark'),(63,'Can delete Bookmark',16,'delete_bookmark'),(64,'Can add User Setting',17,'add_usersettings'),(65,'Can change User Setting',17,'change_usersettings'),(66,'Can delete User Setting',17,'delete_usersettings'),(67,'Can add User Widget',18,'add_userwidget'),(68,'Can change User Widget',18,'change_userwidget'),(69,'Can delete User Widget',18,'delete_userwidget'),(70,'Can add log entry',19,'add_log'),(71,'Can change log entry',19,'change_log'),(72,'Can delete log entry',19,'delete_log'),(73,'Can view Bookmark',16,'view_bookmark'),(74,'Can view log entry',19,'view_log'),(75,'Can view User Setting',17,'view_usersettings'),(76,'Can view User Widget',18,'view_userwidget'),(77,'Can add captcha store',20,'add_captchastore'),(78,'Can change captcha store',20,'change_captchastore'),(79,'Can delete captcha store',20,'delete_captchastore');

#
# Structure for table "auth_group_permissions"
#

DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "auth_group_permissions"
#


#
# Structure for table "django_migrations"
#

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;

#
# Data for table "django_migrations"
#

INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-05-06 08:36:15'),(2,'contenttypes','0002_remove_content_type_name','2017-05-06 08:36:15'),(3,'auth','0001_initial','2017-05-06 08:36:15'),(4,'auth','0002_alter_permission_name_max_length','2017-05-06 08:36:15'),(5,'auth','0003_alter_user_email_max_length','2017-05-06 08:36:15'),(6,'auth','0004_alter_user_username_opts','2017-05-06 08:36:15'),(7,'auth','0005_alter_user_last_login_null','2017-05-06 08:36:15'),(8,'auth','0006_require_contenttypes_0002','2017-05-06 08:36:15'),(9,'auth','0007_alter_validators_add_error_messages','2017-05-06 08:36:15'),(10,'users','0001_initial','2017-05-06 08:36:15'),(11,'admin','0001_initial','2017-05-06 08:36:16'),(12,'admin','0002_logentry_remove_auto_add','2017-05-06 08:36:16'),(13,'captcha','0001_initial','2017-05-06 08:36:16'),(14,'product','0001_initial','2017-05-06 08:36:16'),(15,'product','0002_auto_20170506_0829','2017-05-06 08:36:16'),(16,'operation','0001_initial','2017-05-06 08:36:16'),(17,'sessions','0001_initial','2017-05-06 08:36:16'),(18,'xadmin','0001_initial','2017-05-06 08:36:16'),(19,'xadmin','0002_log','2017-05-06 08:36:16'),(20,'xadmin','0003_auto_20160715_0100','2017-05-06 08:36:16'),(21,'users','0002_auto_20170507_0008','2017-05-07 00:08:12');

#
# Structure for table "django_session"
#

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "django_session"
#

INSERT INTO `django_session` VALUES ('pxbj1lp6olf5tyzdbxyev7cxtg7mh0a3','NTYzOWE3ZTk0MTA0OWQ5YzQ2MmNmZTk5ZTY4NWNmNGYwZGJiZTU4Mjp7Il9hdXRoX3VzZXJfaGFzaCI6ImM0YTEyMDFlYWU0MDBiMDRkNmY0ZmQ2YmNkNTIzMzY1NTZhYmY4YzQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJ1c2Vycy52aWV3cy5DdXN0b21CYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6IjgifQ==','2017-05-21 13:09:18');

#
# Structure for table "product_category"
#

DROP TABLE IF EXISTS `product_category`;
CREATE TABLE `product_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "product_category"
#


#
# Structure for table "product_product"
#

DROP TABLE IF EXISTS `product_product`;
CREATE TABLE `product_product` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `subTitle` varchar(500) NOT NULL,
  `orignalPrice` double NOT NULL,
  `promoteprice` double NOT NULL,
  `stock` double NOT NULL,
  `createData` datetime NOT NULL,
  `Category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_product_e9c8a574` (`Category_id`),
  CONSTRAINT `product_product_Category_id_bde4ff97_fk_product_category_id` FOREIGN KEY (`Category_id`) REFERENCES `product_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "product_product"
#


#
# Structure for table "product_productimage"
#

DROP TABLE IF EXISTS `product_productimage`;
CREATE TABLE `product_productimage` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type` varchar(100) NOT NULL,
  `Product_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_productimage_1a28406a` (`Product_id`),
  CONSTRAINT `product_productimage_Product_id_e2542d25_fk_product_product_id` FOREIGN KEY (`Product_id`) REFERENCES `product_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "product_productimage"
#


#
# Structure for table "product_property"
#

DROP TABLE IF EXISTS `product_property`;
CREATE TABLE `product_property` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `Category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_property_e9c8a574` (`Category_id`),
  CONSTRAINT `product_property_Category_id_ddb69b58_fk_product_category_id` FOREIGN KEY (`Category_id`) REFERENCES `product_category` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "product_property"
#


#
# Structure for table "product_propertyvalue"
#

DROP TABLE IF EXISTS `product_propertyvalue`;
CREATE TABLE `product_propertyvalue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `value` varchar(200) NOT NULL,
  `Product_id` int(11) NOT NULL,
  `property_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_propertyvalue_1a28406a` (`Product_id`),
  KEY `product_propertyvalue_6bb837ff` (`property_id`),
  CONSTRAINT `product_propertyvalu_property_id_e78cfcc7_fk_product_property_id` FOREIGN KEY (`property_id`) REFERENCES `product_property` (`id`),
  CONSTRAINT `product_propertyvalue_Product_id_ff65ea77_fk_product_product_id` FOREIGN KEY (`Product_id`) REFERENCES `product_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "product_propertyvalue"
#


#
# Structure for table "users_emailverifyrecord"
#

DROP TABLE IF EXISTS `users_emailverifyrecord`;
CREATE TABLE `users_emailverifyrecord` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(80) NOT NULL,
  `email` varchar(50) NOT NULL,
  `send_type` varchar(10) NOT NULL,
  `send_time` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

#
# Data for table "users_emailverifyrecord"
#

INSERT INTO `users_emailverifyrecord` VALUES (1,'cQg69LKm3RdQnVeX','18500611672@163.com','register','2017-05-07 00:10:45'),(2,'qjyin0Dgi2hTb538','2410250284@qq.com','register','2017-05-07 00:19:27'),(3,'7iS4w0Bbo1pC98kd','2410250284@qq.com','register','2017-05-07 00:23:23'),(4,'eFdkZOPeOjzxVvM7','1131108499@qq.com','register','2017-05-07 00:27:36'),(5,'CT1qjLj5tZIMvq86','1131108499@qq.com','register','2017-05-07 00:30:49'),(6,'PR8kZXtVdNSzXQoH','18500611672@163.com','register','2017-05-07 00:32:31');

#
# Structure for table "users_userprofile"
#

DROP TABLE IF EXISTS `users_userprofile`;
CREATE TABLE `users_userprofile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `nick_name` varchar(50) NOT NULL,
  `birday` date DEFAULT NULL,
  `gender` varchar(6) NOT NULL,
  `address` varchar(100) NOT NULL,
  `mobile` varchar(11) DEFAULT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

#
# Data for table "users_userprofile"
#

INSERT INTO `users_userprofile` VALUES (1,'pbkdf2_sha256$24000$nxq4kXUYTJYk$xLswH5i/K5HVPThvRP8Y+s0CRi3duhC0mWyFu4www0g=','2017-05-06 13:28:15',1,'admin','','','2410250284@qq.com',1,1,'2017-05-06 12:55:19','',NULL,'unknow','',NULL,'image/default.png'),(7,'pbkdf2_sha256$24000$xIuOB4KJR5U9$xIBYMjB0Sm+1TwCTeeAMmaSpQ4MGjpxMUDrBAg7kKtE=',NULL,0,'1131108499@qq.com','','','1131108499@qq.com',0,1,'2017-05-07 00:30:49','',NULL,'unknow','',NULL,'image/default.png'),(8,'pbkdf2_sha256$24000$kJpufFnFflor$Kq2NAdv1kdvJhPKuh+SkBJhpi04Rqjx2buqin16ilbI=','2017-05-07 13:09:18',0,'18500611672@163.com','','','18500611672@163.com',0,1,'2017-05-07 00:32:31','',NULL,'unknow','',NULL,'image/default.png');

#
# Structure for table "product_review"
#

DROP TABLE IF EXISTS `product_review`;
CREATE TABLE `product_review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` longtext NOT NULL,
  `createDate` datetime NOT NULL,
  `Product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `product_review_Product_id_588e6606_fk_product_product_id` (`Product_id`),
  KEY `product_review_e8701ad4` (`user_id`),
  CONSTRAINT `product_review_user_id_101f565f_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `product_review_Product_id_588e6606_fk_product_product_id` FOREIGN KEY (`Product_id`) REFERENCES `product_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "product_review"
#


#
# Structure for table "operation_order"
#

DROP TABLE IF EXISTS `operation_order`;
CREATE TABLE `operation_order` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `orderCode` varchar(100) NOT NULL,
  `address` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `receiver` varchar(100) NOT NULL,
  `mobile` varchar(100) NOT NULL,
  `userMessage` varchar(100) NOT NULL,
  `createDate` datetime NOT NULL,
  `payDate` datetime NOT NULL,
  `deliveryDate` datetime NOT NULL,
  `confirmDate` datetime NOT NULL,
  `status` varchar(100) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_order_user_id_fe675451_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `operation_order_user_id_fe675451_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "operation_order"
#


#
# Structure for table "operation_orderitem"
#

DROP TABLE IF EXISTS `operation_orderitem`;
CREATE TABLE `operation_orderitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `number` int(11) NOT NULL,
  `order_id` int(11) NOT NULL,
  `product_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `operation_orderitem_order_id_e8b3b783_fk_operation_order_id` (`order_id`),
  KEY `operation_orderitem_product_id_984f03e6_fk_product_product_id` (`product_id`),
  KEY `operation_orderitem_user_id_b5fb8724_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `operation_orderitem_user_id_b5fb8724_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `operation_orderitem_order_id_e8b3b783_fk_operation_order_id` FOREIGN KEY (`order_id`) REFERENCES `operation_order` (`id`),
  CONSTRAINT `operation_orderitem_product_id_984f03e6_fk_product_product_id` FOREIGN KEY (`product_id`) REFERENCES `product_product` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "operation_orderitem"
#


#
# Structure for table "django_admin_log"
#

DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "django_admin_log"
#


#
# Structure for table "users_userprofile_groups"
#

DROP TABLE IF EXISTS `users_userprofile_groups`;
CREATE TABLE `users_userprofile_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_groups_userprofile_id_823cf2fc_uniq` (`userprofile_id`,`group_id`),
  KEY `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` (`group_id`),
  CONSTRAINT `users_userprofile_groups_group_id_3de53dbf_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `users_userprofil_userprofile_id_a4496a80_fk_users_userprofile_id` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "users_userprofile_groups"
#


#
# Structure for table "users_userprofile_user_permissions"
#

DROP TABLE IF EXISTS `users_userprofile_user_permissions`;
CREATE TABLE `users_userprofile_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `userprofile_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `users_userprofile_user_permissions_userprofile_id_d0215190_uniq` (`userprofile_id`,`permission_id`),
  KEY `users_userprofile_u_permission_id_393136b6_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `users_userprofile_u_permission_id_393136b6_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `users_userprofil_userprofile_id_34544737_fk_users_userprofile_id` FOREIGN KEY (`userprofile_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "users_userprofile_user_permissions"
#


#
# Structure for table "xadmin_bookmark"
#

DROP TABLE IF EXISTS `xadmin_bookmark`;
CREATE TABLE `xadmin_bookmark` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(128) NOT NULL,
  `url_name` varchar(64) NOT NULL,
  `query` varchar(1000) NOT NULL,
  `is_share` tinyint(1) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_bookma_content_type_id_60941679_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_bookmark_user_id_42d307fc_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`),
  CONSTRAINT `xadmin_bookma_content_type_id_60941679_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "xadmin_bookmark"
#


#
# Structure for table "xadmin_log"
#

DROP TABLE IF EXISTS `xadmin_log`;
CREATE TABLE `xadmin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `ip_addr` char(39) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` varchar(32) NOT NULL,
  `message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` (`content_type_id`),
  KEY `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_log_content_type_id_2a6cb852_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `xadmin_log_user_id_bb16a176_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "xadmin_log"
#


#
# Structure for table "xadmin_usersettings"
#

DROP TABLE IF EXISTS `xadmin_usersettings`;
CREATE TABLE `xadmin_usersettings` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(256) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_usersettings_user_id_edeabe4a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

#
# Data for table "xadmin_usersettings"
#

INSERT INTO `xadmin_usersettings` VALUES (1,'dashboard:home:pos','',1);

#
# Structure for table "xadmin_userwidget"
#

DROP TABLE IF EXISTS `xadmin_userwidget`;
CREATE TABLE `xadmin_userwidget` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` varchar(256) NOT NULL,
  `widget_type` varchar(50) NOT NULL,
  `value` longtext NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` (`user_id`),
  CONSTRAINT `xadmin_userwidget_user_id_c159233a_fk_users_userprofile_id` FOREIGN KEY (`user_id`) REFERENCES `users_userprofile` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

#
# Data for table "xadmin_userwidget"
#

