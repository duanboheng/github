from bs4 import BeautifulSoup          # For processing HTML
soup=BeautifulSoup('https://finance.sina.com.cn/')
print (soup.findAll('https://finance.sina.com.cn/'))
