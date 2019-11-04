from config import db


class Stock(db.Model):
    __tablename__ = 'stocks'
    id = db.Column(db.Integer, primary_key=True)
    # TS代码
    ts_code = db.Column(db.String(64), unique=True)
    # 股票代码
    symbol = db.Column(db.String(64))
    # 股票名称
    name = db.Column(db.String(64))
    # 所在地域
    area = db.Column(db.String(64))
    # 所属行业
    industry = db.Column(db.String(64))
    # 市场类型
    market = db.Column(db.String(64))
    # 交易所代码
    exchange = db.Column(db.String(64))
    # 上市状态
    list_status = db.Column(db.String(64))
    # 上市日期
    list_date = db.Column(db.String(64))
    # 退市日期
    delist_date = db.Column(db.String(64))
    # 是否沪深港通标的
    is_hs = db.Column(db.String(64))
