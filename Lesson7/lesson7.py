# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 13:22:21 2020

@author: WEN
"""

import requests as req
import chardet
from bs4 import BeautifulSoup

url = "https://baike.baidu.com/item/%E5%8C%97%E6%96%97%E4%B8%89%E5%8F%B7%E5%8D%AB%E6%98%9F"
response = req.get(url)

#检查编码
#raw_data = urllib.urlopen(url).read()
#charset = chardet.detect(raw_data)
#encoding = charset['encoding']
#print(encoding)

#更改编码方式
response.encoding = "utf-8"

#content_type = response.['charset']
page_html = response.text



'''
Beautiful Soup 可解析你提供的任何内容，并为你遍历树材料。
可以命令其'查找所有的链接'
或’查找 classexternalLink 的所有链接'
或'查找 url 与 "foo.com" 匹配的所有链接
或'查找粗体文本的表格标题，
然后将该文本发送给我。
'''
soup = BeautifulSoup(page_html, "html.parser")
title = soup.title
print(title)

first_link = soup.select("[class~=lemma-summary]")
first_links = soup.find("div", class_="para")
print(first_link)