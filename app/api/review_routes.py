from flask import Blueprint, jsonify
from flask_login import login_required
from app.models import Review, db
import json

review_routes = Blueprint('reviews', __name__)


@review_routes.route('/', strict_slashes=False)
@login_required
def get_reviews(product_id):
    """ get all product reviews for a product with id product_id """
    product_reviews = Review.query.filter(
        Review.product_id == product_id).all()
    reviews = {review.id: review.to_dict() for review in product_reviews}
    ids = [review.id for review in product_reviews]
    return {'dict': reviews, 'ids': ids}


@review_routes.route('/<int:id>', methods=['DELETE'], strict_slashes=False)
@login_required
def delete_review(product_id, id):
    review = Review.query.filter(Review.id == id).first()
    db.session.delete(review)
    db.session.commit()
    return {'id': id}
