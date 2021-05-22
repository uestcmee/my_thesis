import re,requests,traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

df=pd.read_excel('新闻链接.xlsx',index_col=0)

def get_detail(url,index):
    driver.get(url)
    text=driver.page_source
    with open('./detail_htmls/{}.html'.format(index),'wb') as f:
        f.write(text.encode('utf-8'))


# driver=webdriver.Chrome()
options = webdriver.ChromeOptions()
#1允许所有图片；2阻止所有图片；3阻止第三方服务器图片
prefs = {
    'profile.default_content_setting_values': {
        'images': 2
    }
}
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)


url='http://www.pbc.gov.cn/'

try:
    for index,url_s in enumerate(df['title_url']):

        if index!=2255:
            continue
        print('hello')
        full_url=url+url_s
        print(index,full_url)
        get_detail(full_url,index)

finally:
    traceback.print_exc()
    driver.quit()