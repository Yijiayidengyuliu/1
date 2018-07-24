# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:29:45 2018

@author: LF仔仔
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
##打印每天18点的天气
b=[1]
def weather(i,day,c):
    b.remove(c)
    b.append(i)
    print('Day',day)
    print('temp:',data['list'][b[0]]['main']['temp'],'°C')
    print('Situation:',data['list'][b[0]]['weather'][0]['main'])
    print('pressure:',data['list'][b[0]]['main']['pressure'])
    print('temp_max:',data['list'][b[0]]['main']['temp_max'],'°C')
    print('temp_min:',data['list'][b[0]]['main']['temp_min'],'°C')
    print(' ')
weather(2,1,1)
weather(10,2,2)
weather(18,3,10)
weather(26,4,18)
weather(34,5,26)

def chart(a):
    num=str('-')*int(data['list'][a]['main']['temp'])
    return num
print('The temperature line chart is:')
print('Day 1',chart(2))
print('Day 2',chart(10))
print('Day 3',chart(18))
print('Day 4',chart(26))
print('Day 5',chart(34))
