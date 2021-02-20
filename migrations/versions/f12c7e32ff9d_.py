"""empty message

Revision ID: f12c7e32ff9d
Revises: 
Create Date: 2021-02-17 12:02:55.908092

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f12c7e32ff9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=15), nullable=False),
    sa.Column('password', sa.String(length=64), nullable=False),
    sa.Column('phone', sa.String(length=11), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.Column('rdatetime', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('user_info',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('realname', sa.String(length=15), nullable=False),
    sa.Column('sex', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_info')
    op.drop_table('user')
    # ### end Alembic commands ###