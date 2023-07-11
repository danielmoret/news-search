"""empty message

Revision ID: 311a68dddbd4
Revises: 64bf7583e6cd
Create Date: 2023-07-11 16:24:29.194623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '311a68dddbd4'
down_revision = '64bf7583e6cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('news', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
