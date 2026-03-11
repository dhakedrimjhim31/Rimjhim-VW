class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:password@localhost/order_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100))
    quantity = db.Column(db.Integer)
    price = db.Column(db.Integer)