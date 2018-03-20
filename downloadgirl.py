# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 17:11:53 2017

@author: hnw
"""

import urllib2
import os  #当前目录创建文件夹

def url_open(url):
    req = urllib2.Request(url) #打开浏览器
    #添加header信息
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36')#生成request对象，看起来像浏览器访问
    response = urllib2.urlopen(req) #访问
    html = response.read()
    
    return html
#用于从煎蛋网的网页中获得页面的地址的函数
def get_page(url):
    #将网页解码为python能够处理的Unicode编码
    html = url_open(url).decode('utf-8')
  
    a = html.find('current-comment-page')+23  #查找并平移
    b = html.find(']',a) #从a开始找到索引坐标
   
    return html[a:b]


#用于从煎蛋网的页面找到图片地址的函数
def find_imgs(url):
    html = url_open(url).decode('utf-8')
    img_addrs = []
    #find函数若找不到要找的字符串则会返回-1
    a = html.find('img src=')
    
    while a != -1:
        b = html.find('.jpg', a, a+255) #给定.JPG的寻找范围，注意不要太大
        
        if b != -1: #如果顺利找到.JPG,说明找到完整的图片的地址，则进行保存                                                          
            if 'http'not in html [a +9:b+4]:
                img_addrs.append('http:'+html[a+9:b+4])
            else:
                img_addrs.append(html[a+9:b+4])
        else:
            b = a + 9
            
        a = html.find('img src=',b)

    return img_addrs
    
def save_imgs(folder,img_addrs):
    for each in img_addrs: #保存图片
        filename = each.split('/')[-1] #图片的地址
        with open(filename, 'wb') as f: #在ooxx中写入filename文件
           
            img = url_open(each)
        
            f.write(img)


def download_mm(folder = 'OOXX',pages = 10):#创建新的文件夹ooxx，下载的前10页
    if not os.path.exists('./OOXX'):
        os.mkdir(folder)# 创建文件夹
    os.chdir(folder)# 把当前的工作目录切换进去

    url = "http://jandan.net/ooxx/"
   
    page_num = int(get_page(url))# 获得页面的地址

    for i in range(pages):
        page_num -=i
        page_url = url + 'page-' + str(page_num) +'#comments' #
        img_addrs = find_imgs(page_url)#获得图片的地址并返回列表
    
        save_imgs(folder,img_addrs)#保存到指定的文件夹folder


if __name__ == '__main__':
    download_mm()
