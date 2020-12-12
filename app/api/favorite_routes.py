from flask import Blueprint, jsonify, session, request
from sqlalchemy import and_
from app.models import Favorite, db
# from flask_login import current_user
import json

favorite_routes = Blueprint('favorites', __name__)

# TODO: Get all current user's favorite products
# TODO: Favorite a product
# TODO: Unfavorite a product


@favorite_routes.route('/', strict_slashes=False)
def get_user_favorites(user_id):
    user_favorites = Favorite.query.filter(Favorite.user_id == user_id).all()
    return {"ids": [favorite.to_dict() for favorite in user_favorites], "dict": {favorite.id: favorite.to_dict() for favorite in user_favorites}}


@favorite_routes.route('/', methods=['POST'], strict_slashes=False)
def favorite_product(user_id):
    req_data = json.loads(request.data)
    favorite = Favorite(
        user_id=user_id, product_id=req_data['productId'])
    db.session.add(favorite)
    db.session.commit()
    return favorite.to_dict()


@favorite_routes.route('/', methods=['DELETE'], strict_slashes=False)
def unfavorite_product(user_id):
    req_data = json.loads(request.data)
    favorite = Favorite.query.filter(
        and_(Favorite.user_id == user_id, Favorite.product_id == req_data['productId'])).first()
    id = favorite.id
    db.session.delete(favorite)
    db.session.commit()
    return {'id': id}
