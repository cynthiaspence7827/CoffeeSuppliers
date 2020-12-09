from flask import Blueprint, jsonify
from app.models import Category, db
import json

category_routes = Blueprint('categories', __name__)


@category_routes.route('/', strict_slashes=False)
def get_all_categories():
    categories = Category.query.all()
    category_dict = {category.id: category.to_dict()
                     for category in categories}
    category_ids = [category.id for category in categories]
    return {
        'dict': category_dict,
        'ids': category_ids
    }
