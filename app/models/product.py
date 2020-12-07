from .db import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)
    description = db.Column(db.Text)
    amount_in_stock = db.Column(
        db.Float(precision=2), nullable=False, default=0)
    price = db.Column(db.Float(precision=2), nullable=False)
    main_image = db.Column(db.String, nullable=False)
    image2 = db.Column(db.String)
    image3 = db.Column(db.String)
    image4 = db.Column(db.String)
    image5 = db.Column(db.String)
    reviews = db.relationship('Review', backref='products', lazy=True)
    categories = db.relationship(
        'Category', secondary='category_join', back_populates='products', lazy=True)
