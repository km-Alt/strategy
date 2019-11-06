import tushare as ts

ts.set_token('e5ee15f8154fe7e19debeefb0f59ca37602a707381a819134a6297de')

pro = ts.pro_api()
fields = 'ts_code,symbol,name,area,industry,market,exchange,list_status,list_date,delist_date,is_hs'
data = pro.stock_basic(list_status='L', fields=fields)
print(data)
