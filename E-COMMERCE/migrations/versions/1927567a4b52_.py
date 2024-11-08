"""empty message

Revision ID: 1927567a4b52
Revises: 6f11100af506
Create Date: 2024-09-14 14:39:33.099277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1927567a4b52'
down_revision = '6f11100af506'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_favorites',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'product_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_favorites')
    # ### end Alembic commands ###
