import re
import requests
from bs4 import BeautifulSoup

sessions = requests.session()
i = 1  # 对应第1页信息
page = '_' + str(i)
if i == 1:
    newsMainUrl = 'https://cmcs.fzu.edu.cn/html/rcpy/jwgs'
elif i != 1:
    newsMainUrl = 'https://cmcs.fzu.edu.cn/html/rcpy/jwgs/' + page + '.html'

newsMainHeader = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Host': 'cmcs.fzu.edu.cn',
    'Referer': 'https://cmcs.fzu.edu.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'

}
# get 请求
rsp = sessions.get(newsMainUrl, headers=newsMainHeader)
# 获取网页
content = rsp.content.decode('utf-8')
# soup用来解析网页的
soup = BeautifulSoup(content, 'html.parser')
gstz_linklist = []
#str1 = ""
# 获取所有dvi 并且calss为con-right fr"的标签
dvs = soup.find_all('a', href=re.compile('/html/rcpy/jwgs/'))
for dv in soup.find_all('a', href=re.compile('/html/rcpy/jwgs/')):
    # 获取div中所有的a标签
    title = dv.find_all('span')
    link = dv.get('href')
    if link:
        gstz_linklist.append('https://cmcs.fzu.edu.cn' + link + ' ' + str(title))
#print(type(gstz_linklist))
for i in gstz_linklist:
    if "调剂" in i:
        str1 = ''.join(i)
        str1=str1.replace('<span>', '')
        str1 = str1.replace('</span>', '')
        str1 = str1.replace('...', '')
        #print(type(str1))
        print(str1)