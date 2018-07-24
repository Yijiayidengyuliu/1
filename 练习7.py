# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 10:31:10 2018

@author: LF仔仔
"""
import urllib.request as r
word = r.quote('裙子')
url = 'https://s.taobao.com/search?q='+word+'&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E4%BD%9B%E5%B1%B1&ajax=true'
itemList = []
def reqTimeOut(url):
    for i in range(0,100):
        urlPage = url + '&s=' + str(i*44)
        try:
            req = r.urlopen(urlPage)
            if req.getcode()==200:
                data = req.read().decode('utf-8','ignore')
        except Exception as err:
            print('网络请求错误,正在重试中。。。')
            i = i-1
            break
        try:
            fileURL = open('foshan.txt','a+',encoding='utf-8')
            fileURL.write(data+'\n')
            fileURL.close()
        except Exception as err:
            print('文件写入错误！重试中。。。')
            break
        print('正在爬取第'+str(i+1)+'页...')
reqTimeOut(url)
