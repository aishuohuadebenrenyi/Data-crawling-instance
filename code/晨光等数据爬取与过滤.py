# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:19:24 2018

@author: Robbin
"""

import urllib.request as r
s=0
f=open('海外LAMY笔.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A4534273&fs=1&globalbuy=1&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('海外英雄笔.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105804&fs=1&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('海外无印良品笔.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A3346593&fs=1&globalbuy=1&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('安徽晨光.txt','a',encoding='utf-8')
for i in range(82):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E5%AE%89%E5%BE%BD&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('福建晨光.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E7%A6%8F%E5%BB%BA&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('甘肃晨光.txt','a',encoding='utf-8')
for i in range(4):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E7%94%98%E8%82%83&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('广东晨光.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E5%B9%BF%E4%B8%9C&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('广西晨光.txt','a',encoding='utf-8')
for i in range(5):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E5%B9%BF%E8%A5%BF&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('贵州晨光.txt','a',encoding='utf-8')
for i in range(3):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E8%B4%B5%E5%B7%9E&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('海南晨光.txt','a',encoding='utf-8')
for i in range(1):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E6%B5%B7%E5%8D%97&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('河北晨光.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E6%B2%B3%E5%8C%97&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('河南晨光.txt','a',encoding='utf-8')
for i in range(38):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E6%B2%B3%E5%8D%97&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('湖北晨光.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E6%B9%96%E5%8C%97&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('湖南晨光.txt','a',encoding='utf-8')
for i in range(51):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E6%B9%96%E5%8D%97&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('江苏晨光.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E6%B1%9F%E8%8B%8F&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('江西晨光.txt','a',encoding='utf-8')
for i in range(8):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E6%B1%9F%E8%A5%BF&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('吉林晨光.txt','a',encoding='utf-8')
for i in range(4):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E5%90%89%E6%9E%97&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('辽宁晨光.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E8%BE%BD%E5%AE%81&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('宁夏晨光.txt','a',encoding='utf-8')
for i in range(1):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180725&ie=utf8&cps=yes&ppath=20000%3A105529784&fs=1&loc=%E5%AE%81%E5%A4%8F&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('山东晨光.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E5%B1%B1%E4%B8%9C&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('山西晨光.txt','a',encoding='utf-8')
for i in range(13):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E5%B1%B1%E8%A5%BF&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('陕西晨光.txt','a',encoding='utf-8')
for i in range(71):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E9%99%95%E8%A5%BF&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('云南晨光.txt','a',encoding='utf-8')
for i in range(9):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E4%BA%91%E5%8D%97&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('四川晨光.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E5%9B%9B%E5%B7%9D&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('新疆晨光.txt','a',encoding='utf-8')
for i in range(6):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E6%96%B0%E7%96%86&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('浙江晨光.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E6%B5%99%E6%B1%9F&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('内蒙古晨光.txt','a',encoding='utf-8')
for i in range(6):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E5%86%85%E8%92%99%E5%8F%A4&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('黑龙江晨光.txt','a',encoding='utf-8')
for i in range(23):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E9%BB%91%E9%BE%99%E6%B1%9F&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('北京晨光.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E5%8C%97%E4%BA%AC&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('上海晨光.txt','a',encoding='utf-8')
for i in range(100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E4%B8%8A%E6%B5%B7&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('重庆晨光.txt','a',encoding='utf-8')
for i in range(6):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E9%87%8D%E5%BA%86&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
s=0
f=open('天津晨光.txt','a',encoding='utf-8')
for i in range(44):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105529784&loc=%E5%A4%A9%E6%B4%A5&s={}&ajax=true'.format(s)
    data=r.urlopen(url).read().decode('utf-8')
    f.write(data+'\n')
f.close()

import urllib.request as r
import json

ls=['安徽','河南','青海','浙江','福建','湖北','山东','澳门','甘肃','湖南','山西','香港','广东','江苏','陕西','台湾','广西','江西',
    '云南','内蒙古','贵州','吉林','四川','黑龙江','海南','辽宁','西藏','河北','宁夏','新疆','北京','天津','重庆','上海']
LS=[] 
f=open('齐心各省情况.txt','w',encoding='utf-8')

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
            print('没页了')
            break
        
        l=len(data['mods']['itemlist']['data']['auctions'])
                  
        for k in range(0,l):
            sales=data['mods']['itemlist']['data']['auctions'][k]['view_sales']
            s=int(sales[0:-3])
            lss.append(s)
                
        for m in lss:
            sum=sum+int(m)
        print(sum)
              
    
        print('成功爬取第'+str(j+1)+'页')
    summ=summ+sum 
    LS.append(summ)
    
f.write(str(LS)+'\n')                  
f.write(str(ls))         
f.close()

