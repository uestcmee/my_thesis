#

import os
from bs4 import BeautifulSoup
import traceback
import pandas as pd



# for file in os.listdir('./大事记htmls/'):
#     print(file)
#     with open('./大事记htmls/'+file,'r',encoding='utf-8') as f:
#         text=f.read()
#         f.close()
#     res=get_list(text)
#     res_df=pd.DataFrame(res,columns=['date','title','title_url'])
#     res_df.dropna(inplace=True)
#     tot_df=pd.concat([tot_df,res_df])
#
# tot_df.to_excel('新闻链接.xlsx')