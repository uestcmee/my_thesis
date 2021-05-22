#

import os
from bs4 import BeautifulSoup
import traceback
import pandas as pd

def process_line(line):
    try:
        title_s=line.find_all('font')[0]
        title=title_s.text
        title_url=title_s.find_all('a')[0].attrs['href']
        date=line.find_all('span')[0].text
        infos=[date,title,title_url]
        return infos
    except:
        # print(traceback.print_exc())
        return [None,None,None]
def get_list(text):
    soup = BeautifulSoup(text, 'lxml')
    table = soup.find_all('div',id='r_con')[0]
    lines=list(map(lambda x:process_line(x),table.find_all('tr')))
    return lines

tot_df=pd.DataFrame(columns=['date','title','title_url'])
for file in os.listdir('./htmls'):
    print(file)
    with open('./htmls/'+file,'r',encoding='utf-8') as f:
        text=f.read()
        f.close()
    res=get_list(text)
    res_df=pd.DataFrame(res,columns=['date','title','title_url'])
    res_df.dropna(inplace=True)
    tot_df=pd.concat([tot_df,res_df])

tot_df.to_excel('新闻链接.xlsx')