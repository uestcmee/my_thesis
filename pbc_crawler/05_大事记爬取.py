import requests
import re

urls='''http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/4068122/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/4021017/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/3974311/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/3776718/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/3491684/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/3265736/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/3020425/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/2810732/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/3776718/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/2865840/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/2858372/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/2850147/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/2875897/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/2846143/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/2817024/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/2817011/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/2892706/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/2816992/index.html
http://www.pbc.gov.cn/zhengcehuobisi/125207/125227/125963/2816989/index.html'''


from selenium import webdriver
driver=webdriver.Edge()

for index,url in enumerate(urls.split('\n')):

    driver.get(url)
    with open('./大事记htmls/{}.html'.format(driver.title),'wb') as f:

        f.write(driver.page_source.encode('utf-8'))
        f.close()

driver.close()

