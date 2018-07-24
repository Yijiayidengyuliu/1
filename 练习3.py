# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 19:12:51 2018

@author: LF仔仔
"""
import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')

import json
data=json.loads(data)
print('Weather:'+data['weather'][0]['description']+'  '+'Temperature:'+str(data['main']['temp'])+'   '+'Pressure:'+str(data['main']['pressure']))
