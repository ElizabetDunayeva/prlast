"""empty message

Revision ID: db9e1c5dbdfc
Revises: 4dd3baaf3071
Create Date: 2022-05-14 11:47:03.672289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db9e1c5dbdfc'
down_revision = '4dd3baaf3071'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('abtest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.String(length=1000), nullable=True),
    sa.Column('scen_id', sa.Integer(), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('percent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scen_id', sa.Integer(), nullable=True),
    sa.Column('probability', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('percent')
    op.drop_table('abtest')
    # ### end Alembic commands ###
