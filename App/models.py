from App.ext import db


# 用户类
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(20))
    password = db.Column(db.String(200))
    token = db.Column(db.String(200))



