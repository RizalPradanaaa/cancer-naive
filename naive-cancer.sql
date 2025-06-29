/*
 Navicat Premium Data Transfer

 Source Server         : coba
 Source Server Type    : MySQL
 Source Server Version : 80030 (8.0.30)
 Source Host           : localhost:3306
 Source Schema         : naive-cancer

 Target Server Type    : MySQL
 Target Server Version : 80030 (8.0.30)
 File Encoding         : 65001

 Date: 29/06/2025 15:19:31
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for dataset
-- ----------------------------
DROP TABLE IF EXISTS `dataset`;
CREATE TABLE `dataset`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `AGE` int NULL DEFAULT NULL,
  `GENDER` tinyint NULL DEFAULT NULL,
  `SMOKING` tinyint NULL DEFAULT NULL,
  `FINGER_DISCOLORATION` tinyint NULL DEFAULT NULL,
  `MENTAL_STRESS` tinyint NULL DEFAULT NULL,
  `EXPOSURE_TO_POLLUTION` tinyint NULL DEFAULT NULL,
  `LONG_TERM_ILLNESS` tinyint NULL DEFAULT NULL,
  `ENERGY_LEVEL` int NULL DEFAULT NULL,
  `IMMUNE_WEAKNESS` tinyint NULL DEFAULT NULL,
  `BREATHING_ISSUE` tinyint NULL DEFAULT NULL,
  `ALCOHOL_CONSUMPTION` tinyint NULL DEFAULT NULL,
  `THROAT_DISCOMFORT` tinyint NULL DEFAULT NULL,
  `OXYGEN_SATURATION` int NULL DEFAULT NULL,
  `CHEST_TIGHTNESS` tinyint NULL DEFAULT NULL,
  `FAMILY_HISTORY` tinyint NULL DEFAULT NULL,
  `SMOKING_FAMILY_HISTORY` tinyint NULL DEFAULT NULL,
  `STRESS_IMMUNE` tinyint NULL DEFAULT NULL,
  `status` tinyint NULL DEFAULT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dataset
-- ----------------------------
INSERT INTO `dataset` VALUES (1, 23, 1, 0, 1, 0, 1, 0, 25, 0, 1, 0, 1, 30, 1, 0, 1, 0, 1, '2025-06-29 09:56:40');
INSERT INTO `dataset` VALUES (2, 23, 1, 0, 1, 0, 1, 0, 24, 0, 1, 1, 1, 45, 0, 0, 1, 1, 1, '2025-06-29 09:59:19');
INSERT INTO `dataset` VALUES (3, 25, 1, 0, 1, 0, 1, 0, 36, 1, 0, 0, 1, 29, 0, 0, 1, 0, 1, '2025-06-29 10:02:18');
INSERT INTO `dataset` VALUES (4, 23, 1, 1, 1, 1, 1, 1, 90, 1, 1, 1, 1, 89, 1, 1, 1, 1, 1, '2025-06-29 10:04:07');
INSERT INTO `dataset` VALUES (5, 23, 1, 1, 1, 1, 1, 1, 30, 0, 1, 0, 1, 30, 1, 1, 1, 1, 1, '2025-06-29 10:07:18');
INSERT INTO `dataset` VALUES (6, 23, 0, 1, 0, 0, 1, 0, 200, 0, 0, 0, 0, 23, 0, 0, 1, 0, 0, '2025-06-29 10:09:49');
INSERT INTO `dataset` VALUES (7, 23, 1, 0, 0, 1, 0, 0, 25, 0, 1, 0, 1, 90, 0, 1, 0, 1, 0, '2025-06-29 10:14:53');
INSERT INTO `dataset` VALUES (8, 23, 1, 0, 0, 1, 0, 0, 25, 0, 1, 0, 1, 90, 0, 1, 0, 1, 0, '2025-06-29 10:17:41');
INSERT INTO `dataset` VALUES (9, 23, 1, 0, 1, 0, 1, 1, 20, 0, 1, 0, 1, 23, 0, 1, 0, 1, 1, '2025-06-29 10:24:46');
INSERT INTO `dataset` VALUES (10, 23, 1, 0, 1, 1, 1, 0, 23, 0, 1, 0, 1, 90, 0, 1, 1, 0, 0, '2025-06-29 10:29:59');
INSERT INTO `dataset` VALUES (11, 23, 1, 0, 1, 0, 1, 0, 23, 0, 1, 0, 1, 23, 0, 1, 0, 1, 1, '2025-06-29 10:37:43');
INSERT INTO `dataset` VALUES (12, 23, 1, 0, 1, 0, 1, 0, 46, 0, 0, 1, 0, 96, 1, 0, 1, 0, 0, '2025-06-29 10:45:48');
INSERT INTO `dataset` VALUES (13, 23, 1, 0, 1, 1, 0, 1, 89, 1, 0, 1, 0, 78, 0, 0, 1, 0, 0, '2025-06-29 10:49:35');
INSERT INTO `dataset` VALUES (14, 23, 0, 1, 0, 1, 0, 1, 80, 0, 1, 0, 1, 90, 0, 1, 0, 1, 1, '2025-06-29 10:53:03');
INSERT INTO `dataset` VALUES (15, 23, 1, 0, 1, 0, 1, 0, 23, 0, 1, 0, 1, 96, 1, 0, 1, 0, 0, '2025-06-29 10:54:49');
INSERT INTO `dataset` VALUES (16, 23, 1, 0, 1, 0, 1, 0, 89, 0, 0, 0, 0, 90, 1, 0, 0, 0, 0, '2025-06-29 10:56:31');
INSERT INTO `dataset` VALUES (17, 23, 1, 0, 1, 0, 1, 0, 80, 0, 1, 1, 1, 90, 0, 1, 1, 1, 1, '2025-06-29 10:58:06');
INSERT INTO `dataset` VALUES (18, 23, 1, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, '2025-06-29 10:58:37');
INSERT INTO `dataset` VALUES (19, 28, 1, 0, 0, 0, 0, 0, 70, 0, 0, 0, 0, 99, 0, 0, 1, 0, 0, '2025-06-29 14:04:04');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(225) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 3 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (2, 'admin@gmail.com', 'pbkdf2:sha256:600000$MLz6HgXR5q4bNO6q$bae97159b7beaa4b489a3db8ffda9638a0d4f255a54ca8cc2ea8daa4200d3fe5');

SET FOREIGN_KEY_CHECKS = 1;
