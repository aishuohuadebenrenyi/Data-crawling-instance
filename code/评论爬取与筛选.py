# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 17:19:05 2018

@author: Robbin
"""
import json
import re
import urllib.request as r

data=r.urlopen('https://s.taobao.com/search?q=%E7%AC%94&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&cps=yes&ppath=20000%3A105795&fs=1&globalbuy=1').read().decode('utf-8','ignore')
ls=re.findall('"nid":"([0-9]*?)",',data,re.S)


f = open("百乐评论.txt",'w',encoding='utf-8')
for i in ls:
    url="https://rate.tmall.com/list_detail_rate.htm?itemId={}&spuId=715860793&sellerId=3248670612&order=3&currentPage=1&append=0&content=1&tagId=1157&posi=-1&picture=0&ua=098%23E1hv%2FpvPvogvUvCkvvvvvjiPPsqZgjrWRFLy0jnEPmPOQj1EnLMp0jiUPszvgj38RphvCvvvvvmrvpvXpv9qvkOevEmVAfvTExVH5ashj8Y1pnLwkOhCvvswN8nJbJMwznQGxDujvpvhvvpvvvyCvhQpl5UvCzMCIExreTt%2Bm7zpa4p7%2B3%2B%2BaNLXSfpAOHmQD7zpdit67Exr0j7J%2B3%2BKafmxfXuKNx%2F3FOkQrEgDNrBlMWoOVzXPTnsO1Cy7Kphv8vvvvvCvpvvvvvv2vhCvmUIvvvWvphvW9pvvvQCvpvs9vvv2vhCv2RmivpvUvvmvWiBT%2BkREvpvVmvvC9jXPvphvC9vhvvCvpvGCvvpvvPMMRphvCvvvvvm5vpvhvvmv9FyCvvpvvvvvdphvmpvZHUbsGQv65OhCvmLJjbiJmYMwznAv3DSSOaQ2zvX4wVSk4I3umWVBOX5jv98myfQ%3D&isg=BPj4GaEt1wI9FDuQD7lIFck0yaaA4Vyh7tXbdzJp3jP9TZw32nOBe0JPAQ3YHRTD&itemPropertyId=&itemPropertyIndex=&userPropertyId=&userPropertyIndex=&rateQuery=&location=&needFold=0&_ksTS=1532580778609_1052&callback=jsonp1053".format(i)
    req=r.Request(url)
    data1=r.urlopen(req).read().decode('gbk','ignore')
    try:
        data2 = data1.split("rateDetail\":")[1]
        data3 = json.loads(data2)
        for j in range(len(data3["rateList"])):
            m = data3["rateList"][j]["rateContent"]
            f.write(m+"\n")
    except:
        continue

f.close()   
    





