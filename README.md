# EySpider #
## 适合新手的基础爬虫框架  ##
### 改自Python爬虫开发与项目实战（范传辉） ###
![](https://i.imgur.com/xxMKM16.png)
## 模块功能分析 ##
1. 爬虫调度器： 负责统筹其他四个模块的的协调工作
2. URL管理器:  负责管理URL
3. HTML下载器：负责网页的下载，分为动态页面和静态页面
4. HTML解析器：负责网页的解析
5. 数据存储器：负责数据的存储，里面封装了对没意思mysql数据库的存储

## py文件简要介绍 ##
1. HtmlDownloader.py：
 
	1. 针对静态网页，使用Requests库
	2. 针对动态网页使用 selenium和phantomjs


2. DataSave.py:

	 使用pymysql 封装mysql的基本操作主要分装了插入操作

3. EySpider

	 使用示例
## 如何使用 ##

直接下载，在HtmlParser.py文件中定制你的爬虫规则。

推荐使用Beautiful解析网页

在EySpider.py中统筹各个模块



**如果觉得有点帮助，给个Star**