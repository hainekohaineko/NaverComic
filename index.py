# -*- coding: utf8 -*-
import requests
from bs4 import BeautifulSoup
import re

def getPage(titleId, weekDay, max_pages):
    pages = 1
    img_link = []
    while pages <= max_pages:
        # &no=1&week=sat&listPage=1
        url = 'http://m.comic.naver.com/webtoon/detail.nhn?titleId=' + str(titleId) +'&no=' + str(pages) + '&week=' + str(weekDay) + '&listPage=' + str(pages)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for link in soup.select('li > p > img'):
            img_src = str(link.get('src'))
            img_lazy = str(link.get('data-lazy-src'))
            if not isBgTransparency(img_src):
                img_link.append(img_src)
            if not img_lazy == 'None':
                img_link.append(img_lazy)
        pages += 1
    return img_link

def isBgTransparency(link):
    regex = re.compile('(http)?:\/\/[^ ]+\.(png)')
    is_bool = regex.match(link)
    return is_bool

# example : 노네임드 1화까지 파싱
print(getPage(460688, 'sat', 1))
