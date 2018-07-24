# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:37:47 2018

@author: LF仔仔
"""
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json
data=json.loads(data)
def message(a):
    print('商品',a+1)
    print('标题：',data['mods']['itemlist']['data']['auctions'][a]['title'])
    print('价格：',data['mods']['itemlist']['data']['auctions'][a]['view_price'])
    print('销量：',data['mods']['itemlist']['data']['auctions'][a]['view_sales'])
    print('发货地',data['mods']['itemlist']['data']['auctions'][a]['item_loc'])
    print(' ')
    if ((a+1)%4==0):
        print('='*30)
        
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
