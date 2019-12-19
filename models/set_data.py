from datetime import datetime
from config import db
import sqlite3
from models.indexes import Index
from models.stocks import Stock
# 上下文
from start import create_app
# tushare
import tushare as ts
import pandas as pd

ts.set_token('e5ee15f8154fe7e19debeefb0f59ca37602a707381a819134a6297de')
pro = ts.pro_api()
today = datetime.now().strftime("%Y-%m-%d")


# 基金基本信息
def set_indexes(root_path):
    # 删除旧数据
    indexes = Index.query.all()
    for i in indexes:
        db.session.delete(i)
    db.session.commit()
    # 获取数据
    fields = 'ts_code,name,market,publisher,index_type,category,base_date,base_point,list_date,weight_rule,exp_date'
    # MSCI指数
    df_msci = pro.index_basic(market='MSCI', fields=fields)
    print('MSCI指数 ' + str(len(df_msci)) + ' 只.')
    # 中证指数
    df_csi = pro.index_basic(market='CSI', fields=fields)
    print('中证指数 ' + str(len(df_csi)) + ' 只.')
    # 上交所指数
    df_sse = pro.index_basic(market='SSE', fields=fields)
    print('上交所指数 ' + str(len(df_sse)) + ' 只.')
    # 深交所指数
    df_szse = pro.index_basic(market='SZSE', fields=fields)
    print('深交所指数 ' + str(len(df_szse)) + ' 只.')
    # 申万指数
    df_sw = pro.index_basic(market='SW', fields=fields)
    print('申万指数 ' + str(len(df_sw)) + ' 只.')
    # 合并df
    df_all = pd.concat([df_msci, df_csi, df_sse, df_szse, df_sw], ignore_index=True)
    # 写入新数据
    con = sqlite3.connect(root_path + '\data.s3db')
    df_all.to_sql('indexes', con, if_exists='append', index_label='id')
    print('finished.')


# 股票基本信息
def set_stocks(root_path):
    # 删除旧数据
    stocks = Stock.query.all()
    for i in stocks:
        db.session.delete(i)
    db.session.commit()
    # 获取数据
    fields = 'ts_code,symbol,name,area,industry,market,exchange,list_status,list_date,delist_date,is_hs'
    # 全部沪深上市股票
    df_stock = pro.stock_basic(list_status='L', fields=fields)
    print('全部沪深上市股票共 ' + str(len(df_stock)) + ' 只.')
    # 写入新数据
    con = sqlite3.connect(root_path + '\data.s3db')
    df_stock.to_sql('stocks', con, if_exists='append', index_label='id')
    print('finished.')


if __name__ == '__main__':
    current_app = create_app('default')
    with current_app.app_context():
        set_indexes(current_app.root_path)
        set_stocks(current_app.root_path)
        # pass
