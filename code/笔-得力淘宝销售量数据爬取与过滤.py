# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 09:21:19 2018

@author: JinF
"""

import urllib.request as r
import json

ls=['安徽','河南','青海','浙江','福建','湖北','山东','澳门','甘肃','湖南','山西','香港','广东','江苏','陕西','台湾','广西','江西',
    '云南','内蒙古','贵州','吉林','四川','黑龙江','海南','辽宁','西藏','河北','宁夏','新疆','北京','天津','重庆','上海']
LS=[] 
f=open('笔—得力淘宝销售量.txt','w',encoding='utf-8')

for i in ls:
    lss=[]      
    b=r.quote(i)  
    sum=0
    summ=0
    for j in range(0,100):
        a=j*44
        url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105625&loc={}&s={}&ajax=true'.format(b,a)
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                 'X-Requested-With': 'XMLHttpRequest'}
            
        req=r.Request(url,headers=headers)
        data=r.urlopen(req).read().decode('utf-8','ignore')
        data=json.loads(data)
       
        p=data['mods']['itemlist']['status']
        if p=='hide':
            print('打印结束')
            break
        
        l=len(data['mods']['itemlist']['data']['auctions'])
                  
        for k in range(0,l):
            sales=data['mods']['itemlist']['data']['auctions'][k]['view_sales']
            s=int(sales[0:-3])
            lss.append(s)
                
        for m in lss:
            sum=sum+int(m)
        print(sum)
              
    
        print('第'+str(j+1)+'页')
    summ=summ+sum 
    LS.append(summ)
    
f.write(str(LS)+'\n')                  
f.write(str(ls))         
f.close()
