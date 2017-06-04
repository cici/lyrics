"""empty message

Revision ID: cb7aa42d36f1
Revises: 8b7040170da9
Create Date: 2017-04-02 13:52:57.252551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb7aa42d36f1'
down_revision = '8b7040170da9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('performer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id', 'name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('performer')
    # ### end Alembic commands ###