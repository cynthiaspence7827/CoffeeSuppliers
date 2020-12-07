from .db import db


class Purchase(db.Model):
    __tablename__ = 'purchases'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fulfilled = db.Column(db.Boolean, nullable=False, default=False)
    delivery_address = db.Column(db.Text, nullable=False)
    delivery_time = db.Column(db.DateTime, nullable=False)
