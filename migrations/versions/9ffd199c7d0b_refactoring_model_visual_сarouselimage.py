"""Refactoring model Visual --- СarouselImage

Revision ID: 9ffd199c7d0b
Revises: 69f40dea0053
Create Date: 2022-09-16 10:39:47.843869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9ffd199c7d0b'
down_revision = '69f40dea0053'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Сarousel_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image', sa.Unicode(length=128), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=False),
    sa.Column('body', sa.Text(), nullable=False),
    sa.Column('route_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['route_id'], ['route.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('visual')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('visual',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('image', sa.VARCHAR(length=128), nullable=False),
    sa.Column('title', sa.VARCHAR(length=80), nullable=False),
    sa.Column('body', sa.TEXT(), nullable=False),
    sa.Column('route_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['route_id'], ['route.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('Сarousel_image')
    # ### end Alembic commands ###
