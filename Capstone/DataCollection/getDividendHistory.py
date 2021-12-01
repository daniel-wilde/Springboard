import os, ssl
import urllib.request as req
import base64
import requests
import pandas as pd
from sqlalchemy import create_engine
# from bs4 import BeautifulSoup as bs

# CREATE ENGINE FOR MYSQL INVESTING DATABASE
investing_db_engine = create_engine(
        "mysql+pymysql://{user}:{pw}@{host}/{db}".format(
            host='127.0.0.1'
            ,db='investing'
            ,user='root'
            ,pw='<pw_here>'
            # ,pw='<pw_here>'
        )
    )

# CREATE A NEW CONNECTION TO THE DB
investing_db_conn = investing_db_engine.raw_connection()

# GET FULL DIVIDEND HISTORY FOR A TICKER
request = req.Request('https://seekingalpha.com/login')
base64string = base64.b64encode(bytes('%s:%s' % ('daniel.r.wilde@gmail.com', 'SDInv924$'),'ascii'))
request.add_header("Authorization", "Basic %s" % base64string.decode('utf-8'))
result = req.urlopen(request)
resulttext = result.read()
print(resulttext)

# headers = {
#         'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
#     }
# login_data = {
#         'Email':'daniel.r.wilde@gmail.com', 'Password':'SDInv924$'
#     }

# with requests.Session() as s:
#     url = 'https://seekingalpha.com/login'
#     r = s.get(url, headers=headers)
#     r = s.post(url, auth=('daniel.r.wilde@gmail.com','SDInv924$'), headers=headers) 
#     r2 = s.get('https://seekingalpha.com/symbol/PG/dividends/history', headers=headers)
#     # print(r.content)

# # login_data = dict(Email='daniel.r.wilde@gmail.com', Password='SDInv924$')
# url = 'https://seekingalpha.com/symbol/PG/dividends/history'
# context = ssl._create_unverified_context()
# response = req.urlopen(url, data=login_data)
# html = response.read()

# DivHist=pd.read_html(r2)  
# div_hist_0 = DivHist[0]
# div_hist_1 = DivHist[1]
# div_hist_2 = DivHist[2]
# div_hist_3 = DivHist[3]

# print(DivHist)

# # # IMPORT CURRENT AND HISTORICAL S&P LISTS TO STAGING TABLES
# div_hist_0.to_sql(con=investing_db_engine, name='_stg_div_hist_0', if_exists='replace')
# div_hist_1.to_sql(con=investing_db_engine, name='_stg_div_hist_1', if_exists='replace')
# div_hist_2.to_sql(con=investing_db_engine, name='_stg_div_hist_2', if_exists='replace')
# div_hist_3.to_sql(con=investing_db_engine, name='_stg_div_hist_3', if_exists='replace')

# # FIND ALL STOCKS THAT NEED DATA REFRESHED
# sql = '''SELECT 'PG' AS Ticker;'''

# # ITERATE THROUGH STOCKS AND GET FINANCIALS
# try:
#     cursor = investing_db_conn.cursor()
#     cursor.execute(sql)
#     df_results = pd.DataFrame(cursor.fetchall(), columns=['Ticker'])
#     cursor.close()
#     investing_db_conn.commit()     
#     for _, row in df_results.iterrows():
#         ticker = str(row['Ticker'])
#         print('Get Financial Info for: ' + ticker)
#         try:
#             ticker_info = YahooFinancials(ticker)
#             # summary_df = pd.DataFrame.from_dict(ticker_info.get_summary_data())
#             # print(summary_df)
#             stock_earnings_df = pd.DataFrame.from_dict(ticker_info.get_stock_earnings_data())
#             print(stock_earnings_df)
#             # financial_stmts_df = ticker_info.get_financial_stmts('quarterly','income')
#             # summary_df.to_sql(con=investing_db_engine, name='_stg_summary', if_exists='replace')            
#             stock_earnings_df.to_sql(con=investing_db_engine, name='_stg_stock_earnings', if_exists='replace')            
#             # financial_stmts_df.to_sql(con=investing_db_engine, name='_stg_financial_stmts', if_exists='replace')            
#             # cursor_pr = investing_db_conn.cursor()
#             # cursor_pr.callproc('sp_refresh_prices', args=[ticker,])
#             # results = list(cursor_pr.fetchall())
#             # cursor_pr.close()
#             investing_db_conn.commit()
#         except Exception as error:
#             print(error)
# except Exception as error:
#     print(error)
# finally:
#     investing_db_conn.close()

