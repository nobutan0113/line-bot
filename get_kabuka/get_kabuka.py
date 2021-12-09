import numpy
from numpy import mod
from requests.api import request
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import pandas as pd
import sys
import requests as re

# 取得コード
code = ['9984', '7817', '9946']
comp_name = ['ソフトバンクグループ（株）', 'パラマウントベッドホールディングス（株）', 'ミニストップ（株）']

s_year = 1 # 取得年数
s_month = 1
s_day = 1 # 取得単位

def get_kabuka():
    for i in range(1):
        company_code = str(code[i]) + '.T'
        my_share = share.Share(company_code)
        # symbol_data = None
        # symbol_data = {}

        try:
            symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY, 1, share.FREQUENCY_TYPE_DAY, 1)
            
            # if i == 1:
            #     symbol_data['softbank'] = my_share.get_historical(share.PERIOD_TYPE_DAY, 1, share.FREQUENCY_TYPE_DAY, 1)
            # elif i == 2:
            #     symbol_data['paramount'] = my_share.get_historical(share.PERIOD_TYPE_DAY, 1, share.FREQUENCY_TYPE_DAY, 1)
            # else:
            #     symbol_data['ministop'] = my_share.get_historical(share.PERIOD_TYPE_DAY, 1, share.FREQUENCY_TYPE_DAY, 1)
                
            # symbol_data = my_share.get_historical(share.PERIOD_TYPE_YEAR, s_year, share.FREQUENCY_TYPE_DAY, s_day)
            # symbol_data.append(my_share.get_historical(share.PERIOD_TYPE_DAY, 1, share.FREQUENCY_TYPE_DAY, 1))

        except YahooFinanceError as e:
            print(e.message)
            sys.exit(1)

        # result = []
        # result.append(symbol_data)
        # df_base = pd.DataFrame(symbol_data)
        # df_base = pd.DataFrame(symbol_data.values(), index=symbol_data.keys()).T
        # df_base.timestamp = pd.to_datetime(df_base.timestamp, unit='ms')
        # df_base.index = pd.DataFrameIndex(df_base.timestamp, name='timestamp').tz_localize('UTC').tz_convert('Asia/Tokyo')

        
        # df_base = df_base.reset_index(drop=True)
        
        
    return symbol_data





def main():
    result = get_kabuka()
    df = pd.DataFrame(result)
    df["datetime"] = pd.to_datetime(df.timestamp, unit="ms") #timestamp変換
    df.head()

    TESTTOKEN = 'BQedVjJhi5yGcg4Cdq6uUgnCQGcRhufYfAhlf0IRSjN'
    PRODTOKEN = 'FvgP8wTGdNVpEbMJjPnIXM9NcNJEePtFCFgmEV9FnlL'
        
    headers = {
        'Authorization' : 'Bearer ' + PRODTOKEN
        # 'Authorization' : 'Bearer ' + TESTTOKEN
        
    }


    text = ''
    s_close = df['close'].values
    s_open = df['open'].values
    s_time = df['datetime'].values
    
    # ss_time = s_time.split(' ')

    end_text = '\n株価自動取得だよー by 信彦'
    text = '\nソフトバンクグループ\n 終値(前日終値.本日終値)：' + str(s_close) + '\n始値(前日始値.本日始値):' + str(s_open) + '\n日付：' + str(s_time) + '\n' + end_text
    
    print(text)

    files = {
        'message' : (None, text)
    }

    re.post('https://notify-api.line.me/api/notify', headers=headers, files=files)
    
main()