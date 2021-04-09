"""empty message

Revision ID: d987cfc84166
Revises: 7b476eb2ed5b
Create Date: 2021-04-09 20:37:54.303800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd987cfc84166'
down_revision = '7b476eb2ed5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reservas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idRecinto', sa.Integer(), nullable=False),
    sa.Column('horaReserva', sa.String(length=30), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reservas')
    # ### end Alembic commands ###