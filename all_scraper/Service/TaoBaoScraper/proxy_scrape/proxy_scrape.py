#-*-coding:utf-8*-
from bs4 import BeautifulSoup
import urllib2
import httplib
import threading
import sys
reload(sys)
#設定系統整體的編碼形式爲utf-8
sys.setdefaultencoding('utf-8')
lock = threading.Lock()
inFile = open('/home/buweixin/桌面/proxy.txt','r+w')
outFile = open('/home/buweixin/桌面/verified.txt', 'w+r')
#獲取到代理ip的列表
def getProxyList(targeturl):
    countNum = 0
    #打開代理文件列表
    proxyFile = open('/home/buweixin/桌面/proxy.txt', 'r+w')
    #設定列表頭部user-agent
    requestHeader = {
        'User-Agent': " Chrome/46.0.2490.80 "}
    #獲取到免費代理網站前10頁的url和網頁源代碼
    for page in range(1, 10):
        url = targeturl + str(page)
        # 獲取頁面整體的html源代碼
        request = urllib2.Request(url, headers=requestHeader)
        html_doc = urllib2.urlopen(request).read()
        soup=BeautifulSoup(html_doc,"html.parser")
        # 利用BeautifulSoup獲取到網頁源代碼裏買的ip
        trs = soup.find('table', id='ip_list').find_all('tr')
        for tr in trs[1:]:
            tds = tr.find_all('td')
            # 国家
            if tds[0].find('img') is None:
                nation = '未知'
                locate = '未知'
            else:
                nation = tds[0].find('img')['alt'].strip()
                locate = tds[3].text.strip()
                ip = tds[1].text.strip()
                port = tds[2].text.strip()
                anony = tds[4].text.strip()
                protocol = tds[5].text.strip()
                speed = tds[6].find('div')['title'].strip()
                time = tds[8].text.strip()
                proxyFile.write('%s|%s|%s|%s|%s|%s|%s|%s\n' % (nation, ip, port, locate, anony, protocol, speed, time))
                print '%s://%s:%s' % (protocol, ip, port)
                countNum += 1
                #proxyFile.close()
    return countNum
#檢驗代理ip的有效性
def verifyProxyList():
    '''
    #验证代理的有效性
    '''
    #設定頭部信息
    requestHeader = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36"}
    #測試網址
    myurl = 'http://www.baidu.com/'
    while True:
        #將infile裏面的信息讀取出來
        lock.acquire()
        ll= inFile.readline().strip()
        #直到讀取完成才釋放
        lock.release()
        if len(ll) == 0: break
        line = ll.strip().split('|')
        protocol = line[5]
        ip = line[1]
        port = line[2]
        #利用獲取的ip地址和端口進行打開百度測試
        try:
            conn = httplib.HTTPConnection(ip, port, timeout=5.0)
            conn.request(method='GET', url=myurl, headers=requestHeader)
            res = conn.getresponse()
            lock.acquire()
            print "+++Success:" + ip + ":" + port
            outFile.write(ll + "\n")
            lock.release()
        except:
            print "---Failure:" + ip + ":" + port


if __name__ == '__main__':
    proxynum = getProxyList("http://www.xicidaili.com/nn/")
    print u"国内高匿：" + str(proxynum)

    print u"\n验证代理的有效性："

    all_thread = []
    for i in range(30):
        t = threading.Thread(target=verifyProxyList)
        all_thread.append(t)
        t.start()
    for t in all_thread:
        t.join()
    inFile.close()
    outFile.close()
    print "All Done."



