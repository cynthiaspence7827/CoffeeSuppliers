from flask import Blueprint, jsonify, session, request
from app.models import OrderItem, Product, Purchase, db
from sqlalchemy import and_
import json

order_item_routes = Blueprint('order_items', __name__)


@order_item_routes.route('/', strict_slashes=False)
def get_order_items():
    req_data = json.loads(request.data)
    purchase_id = req_data['purchaseId']
    purchase = Purchase.query.filter(Purchase.id == purchase_id).first()
    return purchase.to_dict()['orderItems']


@order_item_routes.route('/', methods=['POST'], strict_slashes=False)
def add_order_item():
    req_data = json.loads(request.data)
    order_item = OrderItem(user_id=req_data['userId'], product_id=req_data['productId'],
                           quantity=req_data['qty'], purchase_id=req_data['purchaseId'])
    db.session.add(order_item)
    db.session.commit()
    return order_item


@order_item_routes.route('/<int:item_id>', methods=['PUT'], strict_slashes=False)
def change_item_qty(item_id):
    req_data = json.loads(request.data)
    order_item = OrderItem.query.filter(
        OrderItem.id == item_id).first()
    prev_qty = order_item.quantity
    order_item.quantity = req_data['qty']
    product = Product.query.filter(Product.id == req_data['productId']).first()
    product.quantity -= (order_item.quantity + prev_qty)
    db.session.commit()
    return order_item.to_dict()


@order_item_routes.route('/<int:item_id>', methods=['DELETE'], strict_slashes=False)
def remove_order_item(item_id):
    req_data = json.loads(request.data)
    order_item = OrderItem.query.filter(OrderItem.id == item_id).first()
    qty = order_item.quantity
    product = Product.query.filter(Product.id == order_item.product_id).first()
    product.quantity += qty
    db.session.delete(order_item)
    db.session.commit()
    return {"id": item_id}
