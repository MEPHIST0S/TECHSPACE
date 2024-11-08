"""empty message

Revision ID: 680ab07749b5
Revises: af18f59754f7
Create Date: 2024-09-15 11:24:18.581339

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '680ab07749b5'
down_revision = 'af18f59754f7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email_verified', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('otp_code', sa.String(length=6), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('otp_code')
        batch_op.drop_column('email_verified')

    # ### end Alembic commands ###
