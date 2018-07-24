# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:39:02 2018

@author: LF仔仔
"""
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json
data=json.loads(data)
def message(a):
    print('商品'+str(a+1)+' '+data['mods']['itemlist']['data']['auctions'][a]['title'])
        
def info(i):
    message(i)
    message(i+1)
    message(i+2)
    message(i+3)
    message(i+4)
    message(i+5)
    
info(0)
info(6)
info(12)
info(18)
info(24)
info(30)
