"""empty message

Revision ID: 54d0f8a1251b
Revises: 
Create Date: 2020-12-13 16:08:15.637255

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54d0f8a1251b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('products',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('amount_in_stock', sa.Float(precision=2), nullable=False),
    sa.Column('price', sa.Float(precision=2), nullable=False),
    sa.Column('main_image', sa.String(), nullable=False),
    sa.Column('image2', sa.String(), nullable=True),
    sa.Column('image3', sa.String(), nullable=True),
    sa.Column('image4', sa.String(), nullable=True),
    sa.Column('image5', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.Column('address', sa.Text(), nullable=False),
    sa.Column('phone_number', sa.String(length=10), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('category_join',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('category_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('product_and_category_associated_only_once', 'category_join', ['category_id', 'product_id'], unique=True)
    op.create_table('favorites',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('purchases',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('order_placed', sa.Boolean(), nullable=False),
    sa.Column('fulfilled', sa.Boolean(), nullable=False),
    sa.Column('delivery_address', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('review_body', sa.Text(), nullable=True),
    sa.CheckConstraint('NOT(rating IS NULL AND review_body IS NULL)'),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('one_item_review_per_customer', 'reviews', ['user_id', 'product_id'], unique=True)
    op.create_table('order_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('purchase_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['purchase_id'], ['purchases.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_items')
    op.drop_index('one_item_review_per_customer', table_name='reviews')
    op.drop_table('reviews')
    op.drop_table('purchases')
    op.drop_table('favorites')
    op.drop_index('product_and_category_associated_only_once', table_name='category_join')
    op.drop_table('category_join')
    op.drop_table('users')
    op.drop_table('products')
    op.drop_table('categories')
    # ### end Alembic commands ###
