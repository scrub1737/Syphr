"""create tables

Revision ID: 7ad651ddee5c
Revises: 0bb12b2d6568
Create Date: 2021-06-03 10:21:17.871950

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = '7ad651ddee5c'
down_revision = '0bb12b2d6568'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('selfDestructDate', sa.DateTime(), nullable=True),
    sa.Column('senderId', sa.Integer(), nullable=True),
    sa.Column('recieverId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recieverId'], ['users.id'], ),
    sa.ForeignKeyConstraint(['senderId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('messages')
    # ### end Alembic commands ###
