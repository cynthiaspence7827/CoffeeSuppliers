from .db import db


class Purchase(db.Model):
    __tablename__ = 'purchases'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fulfilled = db.Column(db.Boolean, nullable=False, default=False)
    delivery_address = db.Column(db.Text, nullable=False)
    delivery_time = db.Column(db.DateTime, nullable=False)
    order_items = db.relationship('OrderItem', backref='purchases', lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "fulfilled": self.fulfilled,
            "address": self.delivery_address,
            "scheduledAt": self.delivery_time,
            "orderItems": [item.to_dict() for item in self.order_items]
        }
