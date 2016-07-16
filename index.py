import requests
from bs4 import BeautifulSoup
def getPage(titleId, weekDay, max_pages):
    pages = 1
    while pages <= max_pages:
        # &no=1&week=sat&listPage=1
        url = 'http://m.comic.naver.com/webtoon/detail.nhn?titleId=' + str(titleId) +'&no=' + str(pages) + '&week=' + str(weekDay) + '&listPage=' + str(pages)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'lxml')
        for link in soup.select('li > p > img'):
            imgLink = str(link.get('src')) + str(link.get('data-lazy-src'))# data-lazy-src
            print(imgLink)
        pages += 1
# example : 노네임드 1화까지 파싱
# getPage(460688, 'sat', 1)
getPage(titleId, weekDay, max_pages)
