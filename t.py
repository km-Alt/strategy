import tushare as ts

ts.set_token('e5ee15f8154fe7e19debeefb0f59ca37602a707381a819134a6297de')

pro = ts.pro_api()
data = pro.index_basic(market='SW', fields='ts_code,name,index_type,category')
# data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,market,exchange')
print(type(data))
