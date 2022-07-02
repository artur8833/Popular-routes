"""empty message

Revision ID: 54738fdcb5e9
Revises: 988c73d08cad
Create Date: 2022-07-02 18:22:29.067527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54738fdcb5e9'
down_revision = '988c73d08cad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('way',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('route_id', sa.Integer(), nullable=False),
    sa.Column('fancy_name', webapp.admin.JsonEncodedDict(), nullable=True),
    sa.ForeignKeyConstraint(['route_id'], ['route.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('way')
    # ### end Alembic commands ###
