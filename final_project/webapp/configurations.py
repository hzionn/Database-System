from cs50 import SQL
import pandas as pd
from pyparsing import col

# connect to database
#db = SQL('sqlite:///project.db')
#db = SQL('sqlite:///project_cascade.db')
db = SQL('sqlite:///project_noforeign.db')

# places where that polices work
PLACES = [
    'tainan',
    'taipei',
    'kaohsiung',
    'taoyuan'
]

PLACEOFOCCUR = [place.upper() for place in PLACES]

# to store and update globle variables from request
tmp_data = {}

def pd_df(sql_result: list):
    '''create pandas dataframe using query result, return pd.DataFrame'''

    col_names = [] # to store columns name
    for dic_data in sql_result[:1]:
        for col_name in dic_data.keys():
            col_names.append(col_name)
    if col_names[-1] == None:
        col_names = col_names[:-1]

    df = pd.DataFrame(columns=col_names) # create a new dataframe

    all_data = []
    for dic_data in sql_result:
        all_data.append([])
        for data in dic_data.values():
            all_data[-1].append(data)
        df.loc[len(df)] = all_data[-1] # insert data to new row

    return df
