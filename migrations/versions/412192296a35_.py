"""empty message

Revision ID: 412192296a35
Revises: 30fb1b056366
Create Date: 2021-04-07 16:11:14.758849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '412192296a35'
down_revision = '30fb1b056366'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('lastname', sa.String(length=80), nullable=False))
    op.add_column('user', sa.Column('name', sa.String(length=80), nullable=False))
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.drop_column('user', 'name')
    op.drop_column('user', 'lastname')
    # ### end Alembic commands ###