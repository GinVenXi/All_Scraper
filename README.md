我们系统核心部分的优越性和其他团队相比，主要在于：

1  系统抓取平台更广：主要有亚马逊，淘宝，京东，新浪和腾讯五大平台。

2、系统抓取内容更丰富：电商类主要包含产品信息、关键词信息、卖家信息、卖家产品信息、评论信息等；新闻类主要包括新闻编号、链接、标题、摘要、正文、关键词、类型等。

3、多进程抓取，效率更高：采用多进程技术，可同时进行五大平台的混合抓取，但数据互不干扰，高效、智能。

4、高效反爬虫策略：不管是针对图片验证码，滑块验证码，弹窗还是ip封禁，系统都可以有针对性的应对，丝毫不影响抓取效率。

5、URL高效去重：使用高效算法对URL进行去重，保证URL不会重复。

基于初赛结果，此次挑战赛，我们保持系统以上强劲性能的同时，着力于用户操作界面的设计，形成了用户友好的操作界面，提高了用户的可操作性，主要在于：

1、任务队列管理：用户可以对后台数据队列进行操作和分布式管理。

2、电商类和新闻类爬虫的队列任务条件抓取：用户可以根据需求获取满足条件的数据。

3、即时任务抓取：根据用户添加的URL，即时进行网络采集，并将抓取结果实时展示。

管理平台地址：104.156.229.82:8000:login1

用户名：javen

密码：123456

* [优势与特色：](#优势与特色)
    * [1. 抓取数量大，范围广](#1-抓取数量大范围广)
    * [2. 分布式调度策略](#2-分布式调度策略)
    * [3. 高效反爬虫策略](#3-高效反爬虫策略)
    * [4. 网页结构自动化](#4-网页结构自动化)
    * [5. URL去重](#5-url去重)


## 目录
* [1. 背景](#1-背景)
* [2. 目的](#2-目的)
* [3. 相关技术](#3-相关技术)
    * [3.1 Selenium(浏览器自动化测试框架)](#31-selenium浏览器自动化测试框架) 
    * [3.2 PhantomJS](#32-phantomjs)
        * [(1) 简介](#1-简介) 
        * [(2) PhantomJS安装](#2-phantomjs安装) 
        * [(3) 测试](#3-测试)
    * [3.3 XPath选择器](#33-xpath选择器)
        * [(1) 简介](#1-简介-1)
        * [(2) 使用](#2-使用)
* [4. 分布式爬虫系统抓取算法](#4-分布式爬虫系统抓取算法)
    * [(1) 新闻博客类抓取算法](#1-新闻博客类抓取算法)
* [5. 总体架构](#5-总体架构) 
    * [(1) 设计方法](#1-设计方法)
    * [(2) 总体结构](#2-总体结构)
    * [(3) 文件约束](#3-文件约束)
    * [(4) 目录约定](#4-目录约定)
* [6. 数据库设计](#6-数据库设计)
    * [6.1 购物网站数据库相关设计(以亚马逊为例)](#61-购物网站数据库相关设计以亚马逊为例)
        * [(1) amazon_product](#1-amazon_product)
        * [(2) amazon_product_image](#2-amazon_product_image)
        * [(3) amazon_product_keywords_ad](#3-amazon_product_keywords_ad)
        * [(4) amazon_product_keywords_rank](#4-amazon_product_keywords_rank)
        * [(5) amazon_product_review](#5-amazon_product_review)
        * [(6) amazon_product_review_image](#6-amazon_product_review_image)
        * [(7) amazon_product_review_video](#7-amazon_product_review_video)
        * [(8) amazon_seller](#8-amazon_seller)
        * [(9) amazon_seller_product](#9-amazon_seller_product)
        * [(10) amazon_seller_product_offer](#10-amazon_seller_product_offer)
        * [(11) download_queue](#11-download_queue)
    * [6.2 博客网站数据库相关设计(以新浪微博为例)](#62-博客网站数据库相关设计以新浪微博为例)
        * [(1) sina_download_queue](#1-sina_download_queue)
        * [(2) sina_pages](#2-sina_pages)
* [7. 接口设计](#7-接口设计)
* [8. 爬虫逻辑架构图](#8-爬虫逻辑架构图)
* [9. 爬虫物理分布简化架构图](#9-爬虫物理分布简化架构图) 
* [参考资料](#参考资料)


# 1. 背景

随着互联网中数据量的不断增加，以及大数据、云计算、人工智能等新兴技术的发展，数据成为众多公司竞相追逐的目标，而高效地海量数据抓取作为数据分析的前提也受到了相关领域的关注。搜索引擎技术虽然已有很大的进步，能够满足正常用户的需求，但对于一些特殊数据搜索或复杂搜索的需求，搜索引擎的数据已经不能满足。网络安全，产品调研等问题都需要数据支持，而这些数据无法直接获取，需要手动去搜索、分析、提炼，格式化为满足需求的数据，而利用网络爬虫能够自动完成数据获取，汇总的工作，大大提升了工作效率。 在当前新的环境下，对网络爬虫的要求也不断提高，甚至需要对网络爬虫的框架以及爬取策略做出调整，以满足不断发展的行业需求。此外，网络爬虫声名远播的同时，也提高了业内对数据保护和反爬技术的关注，国内外各大网站纷纷采取了相应的反爬虫技术，增加了爬取数据的难度，对网络爬虫提出了新的挑战。

网络爬虫是一个自动获取网页的程序，它能够从互联网上下载指定 URL 的网页，是搜索引擎的重要组成。在功能上，通用的网络爬虫一般分为数据采集，处理，储存三个部分。爬虫的工作原理是：从一个或者多个初始 URL 开始，下载网页内容，然后通过搜索或是内容匹配手段（比如正则表达式），获取网页中感兴趣的内容，同时不断从当前页面提取新的 URL，根据网页抓取策略，按一定的顺序放入待抓取 URL 队列中，整个过程循环执行，一直到满足系统相应的停止条件，然后对这些被抓取的数据进行清洗，整理，并建立索引，存入数据库或文件中，最后根据查询需要，从数据库或文件中提取相应的数据，以文本或图表的方式显示出来。

目前网络爬虫技术面临的问题在于数据异构性和反爬虫机制。前者是由于不同网站的结构具有差异，甚至同一目标数据分布在不同的页面中。这些问题要求网络爬虫能够提供面向不同网站结构的，具有针对性的解析策略。反爬虫机制作为网站的一种安全防护措施，同样阻拦着网络爬虫的数据采集。反爬虫机制通常可以分为：IP封锁、验证码和登录验证三种方式。其中验证码作为最主要的反爬虫机制在近几年发生了较大的改变。从最简单的图像验证码，到弹窗验证码和滑块验证码，验证码的改变不断地促使着网络爬虫技术的更新。

基于上述问题的考虑，我们设计并实现了分布式爬虫系统，能够对新浪微博、亚马逊、淘宝、京东多个网站的分布式抓取。其中，针对这几家网站不同的反爬虫机制和不同的网页结构，本系统提供了相应的方法策略，并提供详细的代码实现。


# 2. 目的

- 互联网是企业进行发布信息的渠道，是个人共享和获取信息的工具，同时也为政府提供大量有价值的信息，用于监管企业和个人。通过互联网例如新闻博客类信息的抓取，能够发现舆论倾向，建立征信体系，发现犯罪行为等。
- 电商网站是个体户及企业进行网上销售的平台。电商网站中的数据有重要的价值，通过抓取电商网站数据，能够体现经济发展趋势，居民消费水平等。同时，可以为后续的个性化推荐提供数据支持。

# 3. 相关技术
## 3.1 Selenium(浏览器自动化测试框架)

Selenium是一个用于Web应用程序测试的工具。Selenium测试直接运行在浏览器中，就像真正的用户在操作一样。支持的浏览器包括IE（7, 8, 9, 10, 11），Mozilla Firefox，Safari，Google Chrome，Opera等。这个工具的主要功能包括：测试与浏览器的兼容性——测试你的应用程序看是否能够很好得工作在不同浏览器和操作系统之上。测试系统功能——创建回归测试检验软件功能和用户需求。支持自动录制动作和自动生成 .Net、Java、Perl等不同语言的测试脚本。

**功能：**
- 框架底层使用JavaScript模拟真实用户对浏览器进行操作。测试脚本执行时，浏览器自动按照脚本代码做出点击，输入，打开，验证等操作，就像真实用户所做的一样，从终端用户的角度测试应用程序。
- 使浏览器兼容性测试自动化成为可能，尽管在不同的浏览器上依然有细微的差别。
- 使用简单，可使用Java，Python等多种语言编写用例脚本。

**优势：**
- Selenium测试直接在浏览器中运行，就像真实用户所做的一样。Selenium 测试可以在 Windows、Linux 和 Macintosh上的 Internet Explorer、Mozilla 和 Firefox 中运行。其他测试工具都不能覆盖如此多的平台。使用 Selenium 和在浏览器中运行测试还有很多其他好处。
- Selenium模块让Python直接控制浏览器，实际点击链接，填写登录信息，几乎就像是有一个人类用户在与页面交互。与Request和Beautiful Soup相比，Selenium允许你用高级得多的方式与网页交互。附录A有安装第三方模块的详细步骤。

导入Selenium的模块需要一点技巧。不是import Selenium，而是要运行可以用Selenium启动FireFox浏览器。之后，可以用selenium启动FireFox浏览器。在交互式环境中输入以下代码：
```
1.	>>>from selenium import webdriver 
2.	>>>brower = webdriver.Firefox() 
3.	>>>type(brower) 
4.	<class 'selenium.webdriver.firefox.webdriver.WebDriver'> 
5.	>>>brower.get('http://www.amazon.com')
```

你会注意到，当webdriver.Firefox()被调用时，FireFox浏览器启动了。对值webdriver.Firefox()调用type()，揭示它具有WebDriver数据类型。调用brower.get(‘http://www.amazon.com’)
将浏览器指向
[Amazon](http://www.amazon.com)
。浏览器应该看起来如下图所示：

![图 命令行中调用webdriver.Firfox()和get()后，Firefox浏览器出现了](http://i1.buimg.com/1949/5de8ffd686896e19.png)

## 3.2 PhantomJS
### (1) 简介

PhantomJS是一个基于webkit的JavaScript API。它使用QtWebKit作为它核心浏览器的功能，使用webkit来编译解释执行JavaScript代码。任何你可以在基于webkit浏览器 做的事情，它都能做到。它不仅是个隐形的浏览器，提供了诸如CSS选择器、支持Web标准、DOM操作、JSON、HTML5、Canvas、SVG等， 同时也提供了处理文件I/O的操作，从而使你可以向操作系统读写文件等。PhantomJS的用处可谓非常广泛，诸如前端无界面自动化测试（需要结合 Jasmin）、网络监测、网页截屏等。

### (2) PhantomJS安装

- ubuntu下面可以直接使用命令安装：
```
1.	>>>sudo apt-get install phantomjs
```

- 在终端执行phantomjs命令，如果跟下图的结果一样就表示安装成功了。
```
1.	javen@javen-virtual-machine:~$ phantomjs 
2.	phantomjs>
```

### (3) 测试
命令行中输入以下代码，即可使用phantomjs抓取界面，测试结果如图所示：
```
1.	from selenium import webdriver 
2.	driver = webdriver.PhantomJS() 
3.	driver.get("http://www.taobao.com/") 
4.	data = driver.title 
5.	print data
```
![图 phantomjs测试结果](http://i1.buimg.com/1949/64116be6687a517c.png)

## 3.3 XPath选择器
### (1) 简介

XPath是一门在XML文档上查找信息的语言。XPath可用来在XML文档中对元素和属性进行遍历。XPath含有超过100个內建的函数。这些函数用于字符串值、数值、日期和时间比较、节点和QName处理、序列处理、逻辑值等等。在网络爬虫中只需要利用XPath“采集”数据。

在XPath中，有7中类型的节点：元素、属性、文本、命名空间、处理指令、注释以及文档节点(或称为根节点)。XML文档是被作为节点树来对待的。树的根被称为文档节点或者根节点。表中列出了最常用的路径表达式。

表达式 | 文档描述
:-:|:-:
nodeName | 选取此节点的所有子节点
/ | 从根节点选取
// | 从匹配选择的当前节点选择文档中的节点，不考虑它们的位置
. | 选取当前节点
.. | 选取当前节点的父节点
@ | 选取属性
* | 匹配任何元素节点
@* | 匹配任何属性节点
Node() | 匹配任何类型的节点

### (2) 使用

在使用xpath前需要先导入lxml包，然后将html源码作为参数传入，即可用xpath提取数据。代码设计如下：
```
1.	from lxml import etree 
2.	tree = etree.HTML(html) 
3.	# 标题 title 
4.	title = tree.xpath("//*[@id='productTitle']/text()") 
5.	try: 
6.	    if(title): 
7.	        if (title[0] != ''): 
8.	            data['title'] = title[0].strip() 
9.	            # print (data['title']) 
10.	    else: 
11.	        print ("no title") 
12.	except Exception as err: 
13.	    print (err)

```

# 4. 分布式爬虫系统抓取算法
## (1) 新闻博客类抓取算法

![图 宽度优先遍历过程](http://i2.kiimg.com/1949/637689c5562e1e51.png)


操作 | 备注
:-:|:-:
初始	| 空
A入队列	| A
A出队列	| 空
BCDEF入队列|BCDEF
B出队列	|CDEF
C出队列	|DEF
D出队列	|EF
E出队列	|F
H入队列	|FH
F出队列	|H
G入队列	|HG
H出队列	|G
I入队列	|GI
G出队列	|I
I出队列	|空

在上表所示遍历过程中，出队列的节点顺序即是图的宽度优先遍历的访问顺序。由此可以看出，上图所示的宽度优先遍历的访问顺序如下：

**A->B->C->D->E->F->H->G->I**

上述介绍的宽度优先遍历是从一个种子节点开始的，而实际的爬虫项目是从一系列的种子链接开始的。所谓种子链接，就好比宽度优先遍历中的种子节点。实际项目中种子链接可以有多个，比如在本项目中我们在抓取新浪新闻和腾讯新闻时，就选用了[www.sina.com](www.sina.com)和[www.qq.com](www.qq.com)两个种子链接。

如何定义一个链接的子节点？每个链接对应一个HTML页面或者其他文件(Word、Excel、PDF、JPG等)，在这些文件中，只有HTML页面有相应的子节点，这些字节点就是HTML页面上对应的超链接。例如在[www.sina.com](www.sina.com)页面中，“新闻”、“财经”、“科技”等都是[www.sina.com](www.sina.com)的子节点。这些子节点本身又是一个链接。

在新浪新闻和腾讯新闻的抓取过程中，可以看作是整个的宽度优先遍历爬虫过程，就是从一系列的种子节点开始，把这些网页中的字节点(也就是超链接)提取出来，放入队列中依次进行抓取。被处理过的链接需要放入一张表(通常称为Visited表)中。每次新处理一个链接之前，需要查看这个链接是否已经存在于Visited表中。如果存在，证明链接已经处理过，跳过，不作处理，否则进行下一步处理。实际的过程如图所示。

![图 宽度优先爬虫过程](http://i1.buimg.com/1949/a3e7a9d7f0edd880.png)

下图是我们使用python实现的程序结构：

![图 宽度优先遍历爬虫(针对新闻博客类网站抓取)](http://i1.buimg.com/1949/2f31eee95d607720.png)

# 5. 总体架构
## (1) 设计方法

1. 采用面向对象的设计方法；
2. 采用MVC的设计思想；
3. 采用从业务而下的系统分解，从技术至上的系统抽象方法。

## (2) 总体结构

![图 分布式爬虫系统架构](http://i1.buimg.com/1949/09a3b4ce959f7304.png)

我们团队开发的分布式爬虫系统架构如上图..所示，所有的调度都是从Service开始：首先，从Data Queue数据队列中提取待抓取数据(例如一些URL等)；接着，将其发送给抓取器Scraper，Scraper会先调用下载器Downloader下载接收到的URL或是由数据拼接而成URL所对应的页面信息；然后，Scraper调用解析器Processor解析下载好的HTML并将解析好的结构化数据返回给Service，最后，Service会调用数据映射层Mapper进行一系列数据库操作，将有效的结构化数据存储到数据库DBTable中。

## (3) 文件约束

遵循开发规范，包括工程资源文件、日志文件、MVC配置文件、数据库事务配置文件、配置文件、异常配置文件等，完全遵循所制定的规范。

## (4) 目录约定

- Cronjob：主入口目录，管理各个进程
	- ProcessPendingDownloadQueue  --->亚马逊抓取进程
    - ProcessPendingJingdongDownloadQueue   --->京东抓取进程
	- ProcessPendingTaobaoDownloadQueue   --->淘宝抓取进程
	- ProcessPendingSinaDownloadQueue   --->新浪抓取进程
	- ProcessPendingTencentDownloadQueue   --->腾讯抓取进程
	- ProcessPendingMobileDownloadQueue   --->移动端抓取进程

- Service：服务层目录，取数据队列任务，调用抓取器，调用数据映射层
	- Service\Cronjob   --->各平台主调用目录
	- Service\Taobao   --->淘宝各页面服务层目录
	- Service\Jingdong   --->京东各页面服务层目录
	- Service\Sina   --->新浪各页面服务层目录
	- Service\Tencent   --->腾讯各页面服务层目录

- Model：实现数据解析和数据映射
	- Model\Scraper   --->抓取器目录
	- Model\Processor   --->解析器目录 
	- Model\Static   --->静态文件目录
	- Model\Mapper   --->数据映射目录
	- Model\DBTable   --->底层数据库目录
	- Model\Downloader_Method  --->下载方法选择文件

- Downloader：下载器
	- Downloader\Selenium   --->selenium工具层源文件

- Learn：web工程(Django实现)
	- learn\learn\urls.py --->网址入口，关联到对应的views.py中的一个函数（或者generic类），访问网址就对应一个函数。
	- learn\learn_app\views.py
	--->处理用户发出的请求，从urls.py中对应过来, 通过渲染templates中的网页可以将显示内容，比如登陆后的用户名，用户请求的数据，输出到网页。
    - learn\learn_app\models.py   --->与数据库操作相关，存入或读取数据时用到这个，当然用不到数据库的时候 你可以不使用。
    - learn\learn_app\templates   --->views.py中的函数渲染templates中的Html模板，得到动态内容的网页，当然可以用缓存来提高速度。
	- learn\learn\setting.py
	--->Django的设置，配置文件，比如 DEBUG 的开关，静态文件的位置等。

# 6. 数据库设计
## 6.1 购物网站数据库相关设计(以亚马逊为例)
### (1) amazon_product

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-: 
id | int(10) unsigned | NO | PRI | NULL | auto_increment
region | enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') | NO | MUL | com | 
asin | char(10) | NO | MUL | NULL | 
variation_parentage | enum('Parent','Child','N/A') | NO |  | N/A | 
parent_asin | char(10) | YES |  | NULL | 
status | tinyint(3) unsigned | NO |  | 1 | 
title | text | YES |  |  | 
description | text | YES |  |  | 
detail_page_url | text | YES |  |  | 
category | varchar(64) | YES |  |  | 
browse_node | varchar(64) | YES |  |  | 
sales_rank | int(10) unsigned | YES |  |  | 
rating | tinyint(3) unsigned | YES |  |  | 
review_count | int(5) unsigned | YES |  |  | 
price | int(10) unsigned | YES |  |  | 
shipping | varchar(64) | YES |  |  | 
list_price | int(10) unsigned | YES |  |  | 
fulfillment | enum(‘AFN’,’MFN’) | YES |  |  | 
seller_id | varchar(14) | YES |  |  | 
first_available_date | date | YES |  |  | 
last_updated_time | timestamp | NO |  | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP
bestseller_node_id | bigint(20) unsigned | YES |  |  | 
is_fba | tinyint(1) unsigned | YES |  | 0 | 
offer_count | smallint(5) unsigned | NO |  | 1 | 
variation_count | smallint(5) unsigned | NO |  | 1	

### (2) amazon_product_image

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-: 
id | bigint(20) unsigned | NO | PRI | NULL | auto_increment
region | enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') | NO | MUL | com | 
asin | char(10) | NO | MUL | NULL | 
url | varchar(128) | NO | MUL | NULL | 
width | smallint(5) unsigned | YES |  | NULL | 
height | smallint(5) unsigned | YES |  | NULL | 
position | tinyint(3) unsigned | NO |  | 0 | 

### (3) amazon_product_keywords_ad

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-: 
id | int(10) unsigned | NO | PRI | NULL | auto_increment
region | enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') | NO | MUL | com | 
asin | char(10) | NO |  | NULL | 
keywords | varchar(128) | NO | MUL | NULL | 
node_id | bigint(20) unsigned | NO | MUL | NULL | 
position | smallint(5) unsigned | NO |  | NULL | 
page_id | smallint(5) unsigned | NO |  | 1 | 
page_position | smallint(5) unsigned | NO |  | NULL | 
ad_position_type | tinyint(3) unsigned | NO |  | 0 | 
ad_position | tinyint(3) unsigned | NO |  | NULL | 
last_updated_time | timestamp | NO |  | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP

### (4) amazon_product_keywords_rank

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-: 
id | int(10) unsigned | NO | PRI | NULL | auto_increment
region | enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') | NO | MUL | com | 
asin | char(10) | NO |  | NULL | 
keywords | varchar(128) | NO | MUL | NULL | 
node_id | bigint(20) unsigned | NO | MUL | NULL | 
rank | smallint(5) unsigned | NO |  | NULL | 
page_id | smallint(5) unsigned | NO |  | 1 | 
page_position | smallint(5) unsigned | NO |  | NULL | 
last_updated_time | timestamp | NO |  | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP

### (5) amazon_product_review

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-: 
id | int(10) unsigned | NO | PRI | NULL | auto_increment
region | enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') | NO | MUL | com | 
review_id | varchar(16) | NO | MUL | NULL | 
asin | char(10) | NO | MUL | NULL | 
customer_id | varchar(32) | YES |  | NULL | 
customer_name | varchar(128) | YES |  | NULL | 
title | varchar(128) | YES |  | NULL | 
description | text | YES |  | NULL | 
rating | tinyint(3) unsigned | YES |  | NULL | 
date | date | YES |  | NULL | 
helpful_yes | int(10) unsigned | YES |  | NULL | 
helpful_no | int(10) unsigned | YES |  | NULL | 
is_verified | tinyint(1) unsigned | YES |  | NULL | 
is_image_included | tinyint(1) unsigned | YES |  | NULL | 
is_video_included | tinyint(1) unsigned | YES |  | NULL | 
last_updated_time | timestamp | NO |  | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP

### (6) amazon_product_review_image

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-: 
id | bigint(20) unsigned | NO | PRI | NULL | auto_increment
region | enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') | NO | MUL | com | 
review_id | varchar(16) | NO | MUL | NULL | 
url | varchar(128) | NO | MUL | NULL | 
width | smallint(5) unsigned | YES |  | NULL | 
height | smallint(5) unsigned | YES |  | NULL | 
position | tinyint(3) unsigned | NO |  | 0 | 

### (7) amazon_product_review_video

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-: 
id | bigint(20) unsigned | NO | PRI | NULL | auto_increment
region | enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') | NO | MUL | com | 
review_id | varchar(16) | NO | MUL | NULL | 
url | varchar(128) | NO | MUL | NULL | 
image_url | varchar(128) | YES |  | NULL | 

### (8) amazon_seller

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-: 
id | int(10) unsigned | NO | PRI | NULL | auto_increment
region | enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') | NO | MUL | com | 
seller_id | varchar(32) | NO | MUL | NULL | 
name | varchar(128) | YES |  | NULL | 
logo_url | varchar(128) | YES |  | NULL | 
rating | tinyint(3) unsigned | YES |  | NULL | 
last_30_days_positive_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
last_90_days_positive_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
last_12_months_positive_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
lifetime_positive_feedback_ratio | tinyint(3) unsigned | YES |  | NULL  | 
last_30_days_neutral_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
last_90_days_neutral_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
last_12_months_neutral_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
lifetime_neutral_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
last_30_days_negative_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
last_90_days_negative_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
last_12_months_negative_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
lifetime_negative_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
last_30_days_feedback_count | int(10) unsigned | YES |  | NULL | 
last_90_days_feedback_count | int(10) unsigned | YES |  | NULL | 
last_12_months_feedback_count | int(10) unsigned | YES |  | NULL | 
lifetime_feedback_count | int(10) unsigned | YES |  | NULL	

### (9) amazon_seller_product

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-: 
id | int(10) unsigned | NO | PRI | NULL | auto_increment
region | enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') | NO | MUL | com | 
seller_id | varchar(32) | NO | MUL | NULL | 
asin | char(10) | NO | MUL | NULL | 
status | tinyint(3) unsigned | NO |  | 1 | 
rank | smallint(5) unsigned | YES |  | NULL | 
price | int(10) unsigned | YES |  | NULL | 
list_price | int(10) unsigned | YES |  | NULL | 
seller_name | varchar(128) | YES |  | NULL | 
seller_logo_url | varchar(128) | YES |  | NULL | 
seller_logo_width | smallint(5) unsigned | YES |  | NULL | 
seller_logo_height | smallint(5) unsigned | YES |  | NULL | 
seller_rating | tinyint(3) unsigned | YES |  | NULL | 
seller_last_12_months_positive_feedback_ratio | tinyint(3) unsigned | YES |  | NULL | 
seller_lifetime_feedback_count | int(10) unsigned | YES |  | NULL | 
search_index | varchar(32) | YES |  | NULL | 
bestseller_node_id | bigint(20) unsigned | YES |  | NULL | 

### (10) amazon_seller_product_offer

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-:
id | int(10) unsigned | NO | PRI | NULL | auto_increment
region | enum('com','com.br','ca','cn','fr','de','in','it','co.jp','com.mx','es','co.uk') | NO | MUL | com | 
seller_id | varchar(32) | NO | MUL | NULL | 
asin | char(10) | NO | MUL | NULL | 
item_id | varchar(32) | YES | MUL | NULL | 
status | tinyint(3) unsigned | NO |  | 1 | 
price | int(10) unsigned | YES |  | NULL | 
shipping | varchar(64) | YES |  | NULL | 
condition | enum('New','UsedLikeNew','UsedVeryGood','UsedGood','UsedAcceptable','CollectibleLikeNew','CollectibleVeryGood','CollectibleGood','CollectibleAcceptable','Refurbished','Club') | YES |  | NULL | 
fulfillment | enum('AFN','MFN') | YES |  | NULL | 
inventory | smallint(6) | YES |  | NULL | 	

### (11) download_queue

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-:
id | int(10) unsigned | NO | PRI | NULL | auto_increment
ac_download_queue_id | int(10) unsigned | NO |  | 0 | 
region | tinyint(3) unsigned | NO |  | 0 | 
type | tinyint(3) unsigned | NO |  | 0 | 
value | varchar(64) | NO | MUL | NULL | 
status | tinyint(3) unsigned | NO |  | 0 | 
priority | tinyint(3) unsigned | NO |  | 0 | 
scrape_count | tinyint(3) unsigned | NO |  | 0 | 
upload_status | tinyint(3) unsigned | NO |  | 0 | 
upload_count | tinyint(3) unsigned | NO |  | 0 | 
last_updated_time | datetime | YES |  | NULL | 
time | timestamp | NO |  | CURRENT_TIMESTAMP | 

## 6.2 博客网站数据库相关设计(以新浪微博为例)

### (1) sina_download_queue

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-:
id | int(11) | NO | PRI | NULL | auto_increment
url_id | varchar(64) | NO |  | NULL | 
title | varchar(255) | NO |  | NULL | 
url | varchar(255) | NO |  | NULL | 
type | varchar(64) | NO |  | NULL | 
status | tinyint(4) | NO |  | 0 | 
last_updated_time | timestamp | NO |  | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP

### (2) sina_pages

Field | Type | Null | Key | Default | Extra
:-: | :-: | :-: | :-: | :-: | :-:
id | int(11) | NO | PRI | NULL | auto_increment
url_id | varchar(64) | NO | UNI | NULL | 
title | varchar(255) | NO |  | NULL | 
url | varchar(255) | NO |  | NULL | 
summary | varchar(500) | YES |  | NULL | 
keywords | varchar(255) | YES |  | NULL | 
published_time | timestamp | NO |  | CURRENT_TIMESTAMP | on update CURRENT_TIMESTAMP
last_updated_time | timestamp | NO |  | CURRENT_TIMESTAMP | 



# 7. 接口设计
**接口信息** 

接口名称|描述|实现技术
:-: | :-: | :-:
http://47.88.2.41/captcha.php|验证码识别接口|图像识别、模式识别技术
http://104.156.229.82/upload/queue|前后端数据接口 | Python+Django+Apache

# 8. 爬虫逻辑架构图

![图 单线程爬虫结构](http://i1.buimg.com/1949/ec78deb89ddb7cc3.png)

实际的爬虫逻辑架构如上图所示。其中：
- URL Frontier包含爬虫当前待抓取的URL(对于持续更新抓取的爬虫，以前已经抓取过的URL可能会回到Frontier重抓)。
- DNS解析模块根据给定的URL决定从哪个Web服务器获取网页。
- 获取模块使用HTTP协议获取URL代表的页面。
- 解析模块提取文本(数据)和网页的链接集合。
- 重复消除模块决定一个解析出来的链接是否已经在URL Frontier或者最近下载过。

![图 多线程爬虫结构](http://i1.buimg.com/1949/604ac7fe47548da8.png)

对并行爬虫架构而言，处理空队列要比序列爬虫更加复杂。空的队列并不意味着爬虫已经完成了工作，因为此刻其他的进程或者线程可能依然在解析网页，并且马上会加入新的URL。进程或者线程管理员需要给报告队列为空的进程/线程发送临时的休眠信号来解决这类问题。线程管理员需要不断跟踪休眠线程的数目，只有当所有线程都休眠的时候，爬虫才可以终止。

# 9. 爬虫物理分布简化架构图

![图 爬虫物理分布简化架构图](http://i1.buimg.com/1949/e09b14ecb2de5ca6.png)

这里最主要的关注对象是爬虫和存储库。其中的爬虫部分阶段性地抓取互联网上的内容。存储库存储爬虫下载下来的网页，是分布式的和可扩展的存储系统。在往存储库中加载新的内容时仍然可以读取存储库。
 
## 参考资料
编号| 文档名称 | 备注
:-: | :-: | :-:
1   |	《Python网络数据采集》	| ISBN: 978-7-115-41629-2
2 | 《用Python写网络爬虫》 | ISBN: 978-7-115-43179-0
3 |	大数据环境下基于python的网络爬虫技术[J]	| 电子制作,2017,(09):44-45
4 | 基于Java平台的分布式网络爬虫系统研究[J]	| 科技创新与应用,2017,(01):112
5 | 《自己动手写网络爬虫(修订版)》 | 清华大学出版社，罗刚，2016
6 | 《精通python网络爬虫——框架与项目实战》 | 机械工业出版社，韦玮，2017

# 优势与特色：

## 1. 抓取数量大，范围广
我们抓取了多个平台的数据，电商类包括亚马逊、淘宝、京东，新闻博客类包括新浪新闻和腾讯新闻，其中亚马逊又涵盖了美国、加拿大、日本、英国、法国、德国、意大利、西班牙八个国家，新浪新闻和腾讯新闻各自也包括了新闻、财经、科技、体育、娱乐、汽车、博客、时尚等十几个大类。能够针对目前海量且分散的互联网数据进行高效、准确的采集。

![用户搜索展示效果图1](http://i4.piimg.com/1949/1050f104529a0de0.png)
![用户搜索展示效果图2](http://i4.piimg.com/1949/086a1f78451c4bc0.png)

## 2. 分布式调度策略

我们的分布式系统采用多进程技术，各个进程之间互不影响，保证了爬虫爬取数据的高效性，可以在同一时间内运行多个平台的抓取。同时我们将抓取进程分成两类，一类是批量抓取，将系统部署到服务器上，通过服务器的数据上传接口将任务分发到不同的服务器，服务器通过cronjob定时队列会批量运行；另一类是用户搜索抓取，用户搜索某信息时，若数据库中没有查询结果，本系统会自动将任务添加到抓取队列中，在后续进行抓取。在服务器操作中，我们主要使用linux系统的crontab定时任务，爬虫被部署到服务器上，同时开启服务器的定时任务，只需要将需要抓取的任务通过数据接口发布到服务器上的任务队列中，爬虫程序会自动进行任务抓取，时间间隔为1分钟。下图所示为服务器上定时任务文件内容。

![图 服务器定时任务文件](http://i4.piimg.com/1949/3d15778730046171.png)

## 3. 高效反爬虫策略

高效应对网站反爬虫机制。对于电商类网站，有几种反爬虫策略，主要包括：

- 图片验证码

针对亚马逊等电商网站反爬虫时出现的图片验证码，我们主要使用的是第三方的验证码识别接口进行破解，通过selenium获取页面中验证码图片的链接，将其与接口地址拼接后发送get请求，将返回的破解后的验证码填入输入框，点击确定后可以进行后续的操作。如下图所示，分别是亚马逊和淘宝的图片验证码，通过上述方法，即可进行破解。
![图 亚马逊图片验证码](http://i1.buimg.com/1949/960721a2dbd51435.png)
![图 淘宝的图片验证码](http://i1.buimg.com/1949/d638abf24fac2f4e.png)

- 滑块验证码

在爬取淘宝相关内容时，短时间内频繁访问多个页面，此时若未处于登录情况下，淘宝反爬虫机制就会推送登录界面，而其中大多数情况下会出现滑块验证码，一般的登录即失效。而我们使用了selenium模拟浏览器操作，可以模拟用户操作，点击滑块并将滑块移动到指定位置，然后就可以进行下一步的抓取。如图2所示，是淘宝的滑块验证码。
![图 淘宝登录滑块验证码](http://i1.buimg.com/1949/6dc5a3bea6a46554.png)

- 弹窗

在爬取京东相关内容时，和淘宝类似，主要短时间内大量访问时就会弹出验证码窗口，相对于淘宝和亚马逊的验证码，京东的应对操作比较简单，我们使用selenium+firefox抓取时，若遇到验证码，只要使用refresh(刷新)操作，便可以很好的越过弹窗验证码，然后就可以进行下一步的抓取。如图所示，即京东的弹窗验证码。
![图 京东弹窗验证码](http://i1.buimg.com/1949/26bcb6f0d3f2247c.png)

- 页面使用js渲染

很多电商网站为了反爬虫，将相关页面做成了动态网页，python中一般的request请求的方式远远达不到我们获取相关数据的要求，response回来的内容只是一些静态内容，比较有价值的例如商品价格等信息无法获取。而对此，我们团队使用selenium+phantomjs的方式对页面内容进行提取。在网络较好的情况下，速度和效果都是较好的。如下图所示，京东的产品页面就是用JavaScript动态渲染的，若是用一般的抓取方式是无法获取到有价值信息的。
![图 禁用JavaScript后的产品页面](http://i1.buimg.com/1949/76f60a43de0ed020.png)
![图 禁用JavaScript后的产品页面](http://i1.buimg.com/1949/79be995b46fd511e.png)

总的来说，我们从各个网站抓取结果分析得出，大多数网站注重对于爬虫的限制，主要是根据爬虫在一段时间内session(使用浏览器打开某个页面，保持这样的会话称为一个session)的数量，当关闭浏览器后session也就关闭了，反爬虫机器人就根据session会话来判断当前用户是真实用户还是爬虫机器人，便于进行相应操作。我们的分布式爬虫系统很好的规避了这一点，大大提高了抓取效率，同时节省了大量代理IP的费用。从效率和成本上来说具有较大优势。

## 4. 网页结构自动化

对于电商类网页，能够对同一个网站的数据进行自动结构化，以亚马逊为例，针对产品页、关键词页、卖家页、评论页、offer页等设计不同的数据库表，同时将比如图片等信息另外用数据库表存储，达到结构化的目的。如图6是亚马逊数据库表中各个字段，详细内容会在数据库设计中介绍。
![亚马逊产品表字段](http://i1.buimg.com/1949/5481fb6bce2ada83.png)

## 5. URL去重

在爬虫启动过程中，我们不希望同一个网页被多次下载，因为重复下载会浪费CPU，还会为搜索引擎系统增加负荷。想要控制这种重复下载问题，就要考虑下载所依据的超链接，只要能够控制待下载的URL不重复，基本可以解决同一个网页重复下载的问题。我们在URL去重过程中，选用下载队列这一数据结构，为每一条URL添加相应的下载状态，假设未下载前的状态为0，该URL执行下载操作后，相应数据库表中得到数据后，即将其状态修改为1，表示该URL已经被下载过，系统下次从任务队列中取任务时，判断URL的状态，若为1，表示已经被抓取，便不再进行重复下载。这种方式解决了URL重复下载的问题。如下图所示。
![图 URL去重](http://i1.buimg.com/1949/5f7c6484f137ac85.png)
