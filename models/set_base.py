from config import db
from models.users import User
from models.roles import Role
from models.indexes import Index
from models.stocks import Stock
# 上下文
from start import create_app


def init_db():
    db.create_all()


def drop_db():
    db.drop_all()


def init_user():
    users = User.query.all()
    roles = Role.query.all()
    for user in users:
        db.session.delete(user)
    for role in roles:
        db.session.delete(role)
    Role.insert_roles()

    km = User(username='kangming', password='123456', email='451221245@qq.com')
    km.confirmed = True
    km.location = 'Beijing'
    km.about_me = 'The longest day has an end.'
    db.session.add(km)

    db.session.commit()


if __name__ == '__main__':
    with create_app('default').app_context():
        init_db()
        # drop_db()
        # init_user()
