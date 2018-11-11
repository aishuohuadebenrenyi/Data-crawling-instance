# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 23:51:38 2018

@author: Robbin
"""

1、真彩，及海外品牌笔数据爬取


# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:58:39 2018

@author: xlb
"""



f=open('C:/Users/xlb/Desktop/作业XLB/江苏.txt','w',encoding='utf-8')
for i in range(0,100):
    print('print the'+str(i)+'page')
    s=i*44
    url='https://s.taobao.com/search?ie=utf8&initiative_id=staobaoz_20180725&stats_click=search_radio_all%3A1&style=grid&js=1&imgfile=&q=%E7%AC%94&suggest=history_1&_input_charset=utf-8&wq=bi&suggest_query=bi&source=suggest&cps=yes&ppath=20000%3A11525364&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&loc=%E5%B9%BF%E8%A5%BF&ajax=true&s={}'.format(s)
    import urllib.request as r#导入联网工具包，名为为r
    data=r.urlopen(url).read().decode('utf-8','ignore')
    f.write(data+'\n')
    

f.close() 



ls=['陕西','台湾',
    '江西','云南','内蒙古','吉林','四川','黑龙江','海南','辽宁','西藏','河北','宁夏','新疆']
k=0
ls1=[range(5),range(5),
     range(1),range(2),range(1),range(1),range(11),range(1),range(1),range(12),range(1),range(8),range(1),range(1)]
for i in ls:
    w=open('C:/Users/xlb/Desktop/作业XLB/{}.txt'.format(i),'w',encoding='utf-8')
       # w=open('齐心(){}.txt'.format(i),'w',encoding='utf-8')
    b=i.encode()  
    j=0
    print(i)
    for aa in ls1[k]:
        a=j*44
        url='https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.2&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E7%AC%94&suggest=history_1&_input_charset=utf-8&wq=bi&suggest_query=bi&source=suggest&cps=yes&ppath=20000%3A105625&loc={}&s={}&ajax=true'.format(b,a)
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                    'X-Requested-With': 'XMLHttpRequest'}
        
        req=r.Request(url,headers=headers) 
        data=r.urlopen(req).read().decode('utf-8','ignore')
        #data=json.loads(data)
        print('成功爬取第'+str(j)+'页')
        w.write(data+'\n')
        #print(i)
        j=j+1
    w.close()
    k=k+1
         
       

"""   
for i in range(51,100):
    print('print the'+str(i)+'page')
    s=s+i*44
    url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180719&ie=utf8&loc=%E6%B1%9F%E8%A5%BF&ajax=true&s={}'.format(s)
    import urllib.request as r#导入联网工具包，名为为r
    data=r.urlopen(url).read().decode('utf-8','ignore')
    f.write(data)
    f.write('\n')
    """




2、数据的分析
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
        
        url='https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A11525364&loc={}&s={}&ajax=true'.format(b,a)
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

"""
for(int j=0;j<8;j++)
	for(int i=0;i<8-j;i++)
	{
		if(a[i]>a[i+1])
		 swap(a[i],a[i+1]);
	}
"""

3、数据的排序
ls1=[926481, 2485, 0, 1661386, 5381, 3093038, 10368, 0, 0, 438, 262, 0, 693627, 1619759, 2211, 0, 203, 14, 37, 0, 4, 0, 76647, 9, 0, 12651, 0, 6952, 0, 1, 21006, 22, 1993, 5948926]
ls2=['安徽', '河南', '青海', '浙江', '福建', '湖北', '山东', '澳门', '甘肃', '湖南', '山西', '香港', '广东', '江苏', '陕西', '台湾', '广西', '江西', '云南', '内蒙古', '贵州', '吉林', '四川', '黑龙江', '海南', '辽宁', '西藏', '河北', '宁夏', '新疆', '北京', '天津', '重庆', '上海']
for i in range(0,len(ls1)):
    for j in range(0,len(ls1)-i):
        if  ls1[j]>ls1[j+1]:
            temp=ls1[j]
            ls1[j]=ls1[j+1]
            ls1[j]=temp
            ls1[j+1]=ls1[j]
            temp2=ls2[j]
            ls2[j]=ls2[j+1]
            ls2[j]=temp2
            ls2[j+1]=ls2[j]
print(ls1)
print(ls2)



