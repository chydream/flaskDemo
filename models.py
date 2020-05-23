import uuid

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Tag(db.Model):
    __tablename__ = 'product_tag'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(128), nullable=False, default=uuid.uuid4, unique=True)
    name = db.Column(db.String(128), nullable=False)
    code = db.Column(db.String(32))
    desc = db.Column(db.String(256))
    is_valid = db.Column(db.Boolean, default=True)
    reorder = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


class Classify(db.Model):
    __tablename__ = 'product_classify'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(128), nullable=False, default=uuid.uuid4, unique=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('product_classify.id'))
    img = db.Column(db.String(256))
    name = db.Column(db.String(128), nullable=False)
    code = db.Column(db.String(32))
    desc = db.Column(db.String(256))
    is_valid = db.Column(db.Boolean, default=True)
    reorder = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(128), nullable=False, default=uuid.uuid4, unique=True)
    name = db.Column(db.String(128), nullable=False)
    content = db.Column(db.Text, nullable=False)
    desc = db.Column(db.String(256))
    types = db.Column(db.String(32))
    price = db.Column(db.Integer, nullable=False)
    origin_price = db.Column(db.Float, nullable=False)
    img = db.Column(db.String(256), nullable=False)
    channel = db.Column(db.String(32))
    buy_link = db.Column(db.String(256))
    status = db.Column(db.String(32))
    sku_count = db.Column(db.Integer, default=0)
    remain_count = db.Column(db.Integer, default=0)
    view_count = db.Column(db.Integer, default=0)
    score = db.Column(db.Integer, default=10)
    is_valid = db.Column(db.Boolean, default=True)
    reorder = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)


class ProductClasses(db.Model):
    __tablename__ = 'product_classify_rel'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    cls_id = db.Column(db.Integer, db.ForeignKey('product_classify.id'))


class ProductTags(db.Model):
    __tablename__ = 'product_tag_rel'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('product_tag.id'))


class User(db.Model):
    __tablename__ = 'accounts_user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    nickname = db.Column(db.String(64))
    password = db.Column(db.String(256), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    is_super = db.Column(db.Boolean, default=False)