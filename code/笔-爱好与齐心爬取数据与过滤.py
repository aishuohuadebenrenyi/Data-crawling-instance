# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 11:41:08 2018

@author: Administrator
"""

f1=open('各品牌销量汇总.txt',encoding='utf-8').readlines()
f2=open('各品牌销量汇总（已排序).txt','a',encoding='utf-8')
for n in range(1):
    sa=[]
    loc=[] 

    for line in f1:
        
        if line.startswith('sales'):
           
            sa.append(line.split('sales')[1])
            
        if line.startswith('location'):
            loc=line
            
    print('='*40)
    print(sa)
    print('='*40)
    print(loc)
    
           
        
    mydict=dict(zip(loc,sa))
    e=sorted(mydict.items(),key=lambda item:item[1])
   

    for i in e:
        print(i)
        f2.write(str(i)+'\n')

                  
f2.close()

