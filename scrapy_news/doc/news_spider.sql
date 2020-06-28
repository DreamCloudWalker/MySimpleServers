SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for article_info
-- ----------------------------
DROP TABLE IF EXISTS `article_info`;
CREATE TABLE `article_info` (
  `article_id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT '文章id',
  `source` varchar(50) DEFAULT NULL COMMENT '文章来源',
  `title` varchar(600) DEFAULT NULL COMMENT '文章标题',
  `url` varchar(200) DEFAULT NULL COMMENT '文章url',
  `status` varchar(50) DEFAULT '0' COMMENT '状态 0:禁用，1:正常',
  `remark` varchar(600) DEFAULT NULL COMMENT '备注',
  `date` datetime DEFAULT NULL,
  `create_time` datetime DEFAULT NULL COMMENT '创建时间',
  `category` varchar(50) DEFAULT NULL COMMENT '文章类别',
  `author_name` varchar(50) DEFAULT NULL COMMENT '文章作者',
  `thumbnail_pic_s` varchar(200) DEFAULT NULL COMMENT '文章缩图url',
  `thumbnail_pic_s02` varchar(200) DEFAULT NULL COMMENT '文章缩图url',
  `thumbnail_pic_s03` varchar(200) DEFAULT NULL COMMENT '文章缩图url',
  PRIMARY KEY (`article_id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8 COMMENT='文章相关';