# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 15:43:07 2018

@author: LF仔仔
"""
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')

import json
data=json.loads(data)

price_list=[]
def price():
    for a in range(0,36):
        b=float(data['mods']['itemlist']['data']['auctions'][a]['view_price'])
        price_list.append(b)
    return price_list
price()
c=sorted(price_list)
print('价格由高到低排序：')
d=list(reversed(c))
print(d)

sales_list=[]
def sales():
    for i in range(0,36):
        sales=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
        e=int(sales[0:-3])
        sales_list.append(e)
    return sales_list
sales()
f=sorted(sales_list)
print('销量由高到低排序：')
g=list(reversed(f))
print(g)
