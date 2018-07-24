# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:12:08 2018

@author: LF仔仔
"""






import re
ls=open("all_school.txt",encoding="utf-8").readlines()
school_ls=[]

for line in ls:
    r=re.findall('.*[大学|学院]',line)
    num=line.split("-jianjie-")[1].split(".")[0]
    print(''.join(r)+'  '+str(num))