from config import db


class Index(db.Model):
    __tablename__ = 'indexes'
    id = db.Column(db.Integer, primary_key=True)
    # TS代码
    ts_code = db.Column(db.String(64), unique=True)
    # 简称
    name = db.Column(db.String(64))
    # 市场
    market = db.Column(db.String(64))
    # 发布方
    publisher = db.Column(db.String(64))
    # 指数风格
    index_type = db.Column(db.String(64))
    # 指数类别
    category = db.Column(db.String(64))
    # 基期
    base_date = db.Column(db.String(64))
    # 基点
    base_point = db.Column(db.Float)
    # 发布日期
    list_date = db.Column(db.String(64))
    # 加权方式
    weight_rule = db.Column(db.String(64))
    # 终止日期
    exp_date = db.Column(db.String(64))
