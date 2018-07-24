# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:20:32 2018

@author: LF仔仔
"""
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json
data=json.loads(data)

def fee():
    for a in range(0,36):
        if float(data['mods']['itemlist']['data']['auctions'][a]['view_fee'])==0.0:
            print('商品'+str(a+1)+'包邮')
fee()
