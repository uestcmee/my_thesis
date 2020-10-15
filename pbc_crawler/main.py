import requests
import re


url='http://www.pbc.gov.cn/goutongjiaoliu/113456/113469/11040/index{}.html'

# headers={
# "Host": "www.pbc.gov.cn",
# "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"
# }
#
# res=requests.get(full_url,headers=headers)
# with open('./htmls/1.html','wb') as f:
#
#     f.write(res.text.encode('utf-8'))
#     f.close()

from selenium import webdriver
driver=webdriver.Edge()

for page in range(1,3):
    print(page)
    full_url=url.format(page)

    driver.get(full_url)
    with open('./htmls/{}.html'.format(page),'wb') as f:

        f.write(driver.page_source.encode('utf-8'))
        f.close()

driver.close()

