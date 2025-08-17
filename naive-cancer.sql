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

 Date: 17/08/2025 15:56:11
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for dataset
-- ----------------------------
DROP TABLE IF EXISTS `dataset`;
CREATE TABLE `dataset`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `Age` int NULL DEFAULT NULL,
  `Gender` enum('Laki-laki','Perempuan') CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Air_Pollution` int NULL DEFAULT NULL,
  `Obesity` int NULL DEFAULT NULL,
  `Passive_Smoker` int NULL DEFAULT NULL,
  `Fatigue` int NULL DEFAULT NULL,
  `Weight_Loss` int NULL DEFAULT NULL,
  `Wheezing` int NULL DEFAULT NULL,
  `Swallowing_Difficulty` int NULL DEFAULT NULL,
  `Clubbing_of_Finger_Nails` int NULL DEFAULT NULL,
  `status` int NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of dataset
-- ----------------------------
INSERT INTO `dataset` VALUES (1, 23, 'Laki-laki', 4, 1, 0, 1, 0, 1, 0, 1, 1);

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
