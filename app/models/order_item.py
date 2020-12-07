from .db import db


class OrderItem(db.Model):
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'products.id'), nullable=False)
    purchase_id = db.Column(db.Integer, db.ForeignKey(
        'purchases.id'), nullable=False)
    db.relationship('Purchase', backref='order_items', lazy=True)
    db.relationship('Product', backref='order_items', lazy=True)
