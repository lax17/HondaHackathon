"""CompanyDetails table

Revision ID: 590561830064
Revises: 
Create Date: 2020-12-21 17:21:21.441765

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '590561830064'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('CompanyDetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('CompanyName', sa.String(length=255), nullable=False),
    sa.Column('Lat', sa.Float(), nullable=False),
    sa.Column('Long', sa.Float(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('ProductDetails',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('CompanyName', sa.String(length=255), nullable=False),
    sa.Column('Lat', sa.Float(), nullable=False),
    sa.Column('Long', sa.Float(), nullable=False),
    sa.Column('productname', sa.String(length=255), nullable=False),
    sa.Column('productprice', sa.Float(), nullable=False),
    sa.Column('productdescription', sa.Text(), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ProductDetails')
    op.drop_table('CompanyDetails')
    # ### end Alembic commands ###