import re
from robobrowser import RoboBrowser

url = 'http://www.qq.com/'
b = RoboBrowser(history=True)
b.open(url)

today_top = b.find(id='todaytop').a
print today_top['href']

b.follow_link(today_top)

title = b.select('.hd h1')[0]
print '*****************************'
print title.text
print '*****************************'

print b.find(id='articleContent').text