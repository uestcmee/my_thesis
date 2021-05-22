from get_list import get_list
company_df=get_list()

for one in company_df.iloc[:,0]:
    print(one)