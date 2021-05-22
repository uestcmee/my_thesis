import pandas as pd
def get_list():
    df=pd.read_excel('风投退出.xlsx',sheet_name='所需PE')
    return df