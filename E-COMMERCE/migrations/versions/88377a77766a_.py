"""empty message

Revision ID: 88377a77766a
Revises: 707a8a8b9c5a
Create Date: 2024-09-15 13:21:37.891341

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88377a77766a'
down_revision = '707a8a8b9c5a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_admin')

    # ### end Alembic commands ###
