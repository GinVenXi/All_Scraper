#项目名称：分布式爬虫系统

##项目构成：
####后端
* Cronjob
* Service
* Downloader
* Models
####前端
* learn (前端展示项目，前后端分离，Django实现)

##技术文档
http://42.123.127.93:10080/javen_Mushishi/document项目下README.md

##数据库
(1)文件  
all_scraper/Models/Data/All_Scraper.sql
(2)数据库查看url  
http://104.156.229.82/phpmyadmin

##演示视频(下面两任选其一)
(1)
http://42.123.127.93:10080/javen_Mushishi/document项目下:
随心所欲团队_分布式爬虫系统[WisMencoder Encoded].avi
(2)
网址：http://v.youku.com/v_show/id_XMjg1OTQ0OTc1Ng==.html?spm=a2h3j.8428770.3416059.1
密码：WWWcnsoftbeiCom666Javen

##服务器前端演示url
http://104.156.229.82:8000/home
建议搜索关键词：
(1)亚马逊:iphone
(2)淘宝:自行车
(3)京东:自行车
(4)Sina:fashion
(5)Tencent:fashion
若其他关键词搜索不出结果，本系统会自动将用户搜索信息添加到后端任务队列中，便于下次抓取

##服务器后端抓取演示
服务器ip:104.156.229.82  

终端命令:  
(1)登录服务器  
ssh -l root 104.156.229.82  
密码:python@2017  

(2)进入项目目录  
cd /home/javen/PycharmProjects/all_scraper/Cronjob/  

(3)运行相应抓取  
1)亚马逊抓取  
python ProcessPendingDownloadQueue.py  
2)淘宝抓取  
python ProcessPendingTaobaoDownloadQueue.py  
3)京东抓取   
python ProcessPendingJingdongDownloadQueue.py  
4)新浪抓取  
python ProcessPendingSinaDownloadQueue.py  
5)腾讯抓取  
python ProcessPendingTencentDownloadQueue.py  

**提示**:为了便于演示在抓取过程中将一些字段的抓取情况展现出来，显示"no xxx"，不是我们抓取器效果不好，只是页面中不存在该信息。

##docker后端抓取演示
团队已经上传docker镜像至harbor的镜像仓库。
(1)将docker镜像pull至本地
docker pull hub.scybsx.com/javen_mushishi/all_scraper:latest
(2)进入项目目录
cd /home/all_scraper/Cronjob/
(3)终端运行命令
sudo export C.UTF-8
(4)运行相应抓取
1)亚马逊抓取  
python ProcessPendingDownloadQueue.py  
2)淘宝抓取  
python ProcessPendingTaobaoDownloadQueue.py  
3)京东抓取   
python ProcessPendingJingdongDownloadQueue.py  
4)新浪抓取  
python ProcessPendingSinaDownloadQueue.py  
5)腾讯抓取  
python ProcessPendingTencentDownloadQueue.py  
**提示**:由于docker中启动无头浏览器等需要时长相比服务器与本地主机较长，所以如遇到运行相应抓取命令后一段时间后执行，属于正常情况。因而推荐首选服务器进行后端抓取演示。
相关dockerfile的内容如下：（由于在大赛官网中多次点击保存未能成功，故将其放在此处说明）
FROM ubuntu
MAINTAINER <nuist bwxhhjy@gmail.com>
RUN apt-get update
RUN export C.UTF-8
RUN apt-get install python-pip
RUN pip install --upgrade pip
RUN apt-get install mysql-server
RUN apt-get install vim
RUN pip install selenium
RUN apt-get install apache2
RUN apt-get install firefox
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb
RUN apt-get -f install
RUN cd /usr/local/lib/python2.7/dist-packages/
RUN vi sudo vi mypkpath.pth
RUN /home/all_scraper
RUN :wq
RUN chmod -R 777mypkpath.pth
RUN service apache2 restart
RUN pip install pyvirtualdisplay
RUN pip install pytz
RUN pip install pymysql
RUN pip install lxml
RUN apt-get install xvfb
RUN pip install requests
RUN pip install bs4
(注意：以上命令均是在sudo用户下执行)
如出现运行问题等，请及时联系我们，十分感谢！

