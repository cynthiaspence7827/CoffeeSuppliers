from flask import Blueprint, jsonify
from app.models import Product, db
import json

product_routes = Blueprint('products', __name__)


@product_routes.route('/', strict_slashes=False)
def get_all_products():
    products = Product.query.all()
    return {
        'dict': {product.id: product.to_dict() for product in products},
        'ids': [product.id for product in products]
    }


@product_routes.route('/<int:id>', strict_slashes=False)
def get_product(id):
    product = Product.query.filter(Product.id == id).first()
    return product.to_dict()
