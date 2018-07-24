# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:27:37 2018

@author: LF仔仔
"""
lc=open("XML高考派城市.txt",encoding="gbk").readlines()
for line in lc[1:-1]:
    nu=line.split(",")[1].split(")")[0]
    cn=line.split("\">")[1].split("<")[0]
    print(str(cn)+'  '+str(nu))