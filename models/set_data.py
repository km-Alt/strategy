# -*- coding: utf-8 -*-

from datetime import datetime
from config import db
import sqlite3
from models.indexes import Index
from models.stocks import Stock
# 上下文
from start import create_app
# tushare
import tushare as ts

ts.set_token('e5ee15f8154fe7e19debeefb0f59ca37602a707381a819134a6297de')
pro = ts.pro_api()
today = datetime.now().strftime("%Y-%m-%d")


def set_indexes(root_path):
    # 删除旧数据
    indexes = Index.query.all()
    for i in indexes:
        db.session.delete(i)
    db.session.commit()
    # 获取数据
    fields = 'ts_code,name,market,publisher,index_type,category,base_date,base_point,list_date,weight_rule,exp_date'
    df_csi = pro.index_basic(market='CSI', fields=fields)
    df_sse = pro.index_basic(market='SSE', fields=fields)
    df_szse = pro.index_basic(market='SZSE', fields=fields)
    # 写入新数据
    print('start')
    con = sqlite3.connect(root_path + '\data.s3db')
    df_csi.to_sql('indexes', con, if_exists='append', index_label='id')
    print('done')


if __name__ == '__main__':
    current_app = create_app('default')
    with current_app.app_context():
        set_indexes(create_app('default').root_path)
        # pass
