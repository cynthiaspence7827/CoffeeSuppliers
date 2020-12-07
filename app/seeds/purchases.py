from app.models import db, Purchase, OrderItem
from datetime import datetime
from werkzeug.security import generate_password_hash


def seed_purchases():
    purchase_seed = Purchase(
        user_id=2,
        fulfilled=True,
        delivery_address=generate_password_hash(
            '123 Happy Lane, Yuma, Arizona 85364'),
        delivery_time=datetime.now()
    )
    db.session.add(purchase_seed)
    db.session.commit()
    order_item_seed = OrderItem(user_id=2, product_id=1, purchase_id=1)
    db.session.add(order_item_seed)
    order_item_seed = OrderItem(user_id=2, product_id=1, purchase_id=1)
    db.session.add(order_item_seed)
    order_item_seed = OrderItem(user_id=2, product_id=1, purchase_id=1)
    db.session.add(order_item_seed)
    order_item_seed = OrderItem(user_id=2, product_id=1, purchase_id=1)
    db.session.add(order_item_seed)
    db.session.commit()

    purchase_seed = Purchase(
        user_id=2,
        fulfilled=True,
        delivery_address=generate_password_hash(
            '125 Some Beach Lane, Yuma, Arizona 85364'),
        delivery_time=datetime.now()
    )
    db.session.add(purchase_seed)
    db.session.commit()
    order_item_seed = OrderItem(user_id=2, product_id=5, purchase_id=2)
    db.session.add(order_item_seed)
    order_item_seed = OrderItem(user_id=2, product_id=7, purchase_id=2)
    db.session.add(order_item_seed)
    order_item_seed = OrderItem(user_id=2, product_id=2, purchase_id=2)
    db.session.add(order_item_seed)
    order_item_seed = OrderItem(user_id=2, product_id=1, purchase_id=2)
    db.session.add(order_item_seed)
    db.session.commit()

    purchase_seed = Purchase(
        user_id=2,
        fulfilled=True,
        delivery_address=generate_password_hash(
            '339 React Street, Yuma, Arizona 85367'),
        delivery_time=datetime.now()
    )
    db.session.add(purchase_seed)
    db.session.commit()
    order_item_seed = OrderItem(user_id=2, product_id=4, purchase_id=2)
    db.session.add(order_item_seed)
    order_item_seed = OrderItem(user_id=2, product_id=3, purchase_id=2)
    db.session.add(order_item_seed)
    order_item_seed = OrderItem(user_id=2, product_id=2, purchase_id=2)
    db.session.add(order_item_seed)
    order_item_seed = OrderItem(user_id=2, product_id=6, purchase_id=2)
    db.session.add(order_item_seed)
    db.session.commit()


def undo_purchases():
    db.session.execute('TRUNCATE purchases; TRUNCATE order_items;')
    db.session.commit()
