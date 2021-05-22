import requests
import re


url='http://dcfm.eastmoney.com/em_mutisvcexpandinterface/api/js/get?callback=jQuery112304878244235130902_1605667649123&st=DATADATE&sr=-1&ps=100&p={}&type=HYZS_All&js=(%7Bdata%3AdataDistinc((x)%2C%22DATADATE%22)%2Cpages%3A(tp)%7D)&filter=(ID%3D%27EMI00662535%27)&token=894050c76af8597a853f5b408b759f5d'

import requests

import json


for page in range(0,26):
    print(page)
    full_url=url.format(page)
    res=requests.get(url)

    print(res.json())
    break
