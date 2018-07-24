# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:23:59 2018

@author: LF仔仔
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
##打印每天18点的天气
def weather(a,b):
    print('Day'+str(a))
    print('Situation:'+str(data['list'][b]['weather'][0]['main']))
    print(' ')
weather(1,2)
weather(2,10)
weather(3,18)
weather(4,26)
weather(5,34)
print('第一天：')
print('温度:'+str(data['list'][2]['main']['temp'])+'°C')
print('气压：'+str(data['list'][2]['main']['pressure']))
print('天气：'+str(data['list'][2]['weather'][0]['description']))
print('最低温度：'+str(data['list'][2]['main']['temp_min'])+'°C')
print('最高温度：'+str(data['list'][2]['main']['temp_max'])+'°C')
print('第二天：')
print('温度：'+str(data['list'][2]['main']['temp'])+'°C')
print('气压：'+str(data['list'][10]['main']['pressure']))
print('天气：'+str(data['list'][10]['weather'][0]['description']))
print('最低温度：'+str(data['list'][10]['main']['temp_min'])+'°C')
print('最高温度：'+str(data['list'][10]['main']['temp_max'])+'°C')
print('第三天：')
print('温度：'+str(data['list'][2]['main']['temp'])+'°C')
print('气压：'+str(data['list'][18]['main']['pressure']))
print('天气：'+str(data['list'][18]['weather'][0]['description']))
print('最低温度：'+str(data['list'][18]['main']['temp_min'])+'°C')
print('最高温度：'+str(data['list'][18]['main']['temp_max'])+'°C')
print('第四天：')
print('温度：'+str(data['list'][2]['main']['temp'])+'°C')
print('气压：'+str(data['list'][26]['main']['pressure']))
print('天气：'+str(data['list'][26]['weather'][0]['description']))
print('最低温度：'+str(data['list'][26]['main']['temp_min'])+'°C')
print('最高温度：'+str(data['list'][26]['main']['temp_max'])+'°C')
print('第五天：')
print('温度：'+str(data['list'][2]['main']['temp'])+'°C')
print('气压：'+str(data['list'][34]['main']['pressure']))
print('天气：'+str(data['list'][34]['weather'][0]['description']))
print('最低温度：'+str(data['list'][34]['main']['temp_min'])+'°C')
print('最高温度：'+str(data['list'][34]['main']['temp_max'])+'°C')
a=data['list'][2]['main']['temp']
b=data['list'][10]['main']['temp']
c=data['list'][18]['main']['temp']
d=data['list'][26]['main']['temp']
e=data['list'][34]['main']['temp']
##打印折线图
print('折线图：')
print('第一天'+('-'*int(a)))
print('第二天'+('-'*int(b)))
print('第三天'+('-'*int(c)))
print('第四天'+('-'*int(d)))
print('第五天'+('-'*int(e)))
##排序
print('排序后的温度：')
print(sorted([a,b,c,d,e]))

