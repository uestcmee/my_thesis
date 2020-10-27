import pandas as pd
import numpy as np
import os
from bs4 import BeautifulSoup


def detail_info(text):
    soup = BeautifulSoup(text,'lxml')
    title=soup.find_all('h2')[0].text #标题

    infos = soup.find_all('td',class_='hui12')[3:-1]# 信息栏
    infos=list(map(lambda x:x.text.strip(),infos))
    main_text = soup.find_all('td',class_='content')[0].text #正文
    result_list=[title]+infos+[main_text]
    return result_list


tot_list=[]
for one in os.listdir('./detail_htmls/'):
    print(one)
    with open('./detail_htmls/' + one, 'r',encoding='utf-8') as f:
        text = f.read()
        result=detail_info(text)
        tot_list.append(result)

result_df=pd.DataFrame(tot_list,columns=['title','source','time','text'])

result_df.to_excel('信息详细时间.xlsx')