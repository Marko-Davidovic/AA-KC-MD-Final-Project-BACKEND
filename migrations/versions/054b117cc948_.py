"""empty message

Revision ID: 054b117cc948
Revises: 
Create Date: 2020-03-04 21:01:14.193292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '054b117cc948'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_temp_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('prod_name', sa.String(length=250), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('ship_cost', sa.Integer(), nullable=False),
    sa.Column('order_total', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('order_temp_id')
    )
    op.create_table('customer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('lastname', sa.String(length=25), nullable=False),
    sa.Column('email', sa.String(length=80), nullable=False),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('address', sa.String(length=80), nullable=False),
    sa.Column('city', sa.String(length=25), nullable=False),
    sa.Column('country', sa.String(length=25), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('cod_lib', sa.String(length=15), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('queries',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('session_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('amz_asin', sa.String(length=25), nullable=False),
    sa.Column('upc', sa.String(length=25), nullable=False),
    sa.Column('product', sa.String(length=250), nullable=False),
    sa.Column('description', sa.String(length=250), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('keywords', sa.String(length=250), nullable=False),
    sa.Column('categories', sa.String(length=250), nullable=False),
    sa.Column('fba', sa.Boolean(), nullable=True),
    sa.Column('prohibited', sa.Boolean(), nullable=True),
    sa.Column('ship_weight', sa.Integer(), nullable=False),
    sa.Column('ocean_dimension', sa.Integer(), nullable=False),
    sa.Column('air_dimension', sa.Integer(), nullable=False),
    sa.Column('added_cart', sa.Boolean(), nullable=True),
    sa.Column('last_added_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('session_id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('session_id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('order_num', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.Column('subtotal', sa.Integer(), nullable=False),
    sa.Column('ship_amt', sa.Integer(), nullable=False),
    sa.Column('ship_method', sa.String(length=25), nullable=False),
    sa.Column('status', sa.String(length=15), nullable=True),
    sa.Column('receiver_code', sa.String(length=15), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.id'], ),
    sa.PrimaryKeyConstraint('order_num'),
    sa.UniqueConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    op.drop_table('queries')
    op.drop_table('customer')
    op.drop_table('cart')
    # ### end Alembic commands ###