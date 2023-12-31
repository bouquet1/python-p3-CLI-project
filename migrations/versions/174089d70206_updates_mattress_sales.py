"""updates mattress sales

Revision ID: 174089d70206
Revises: 32c1508717d9
Create Date: 2023-10-12 17:03:05.122437

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '174089d70206'
down_revision: Union[str, None] = '32c1508717d9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales', sa.Column('queen_sold', sa.Integer(), nullable=True))
    op.add_column('sales', sa.Column('queen_price', sa.Integer(), nullable=True))
    op.add_column('sales', sa.Column('queen_amount', sa.Integer(), nullable=True))
    op.add_column('sales', sa.Column('king_sold', sa.Integer(), nullable=True))
    op.add_column('sales', sa.Column('king_price', sa.Integer(), nullable=True))
    op.add_column('sales', sa.Column('king_amount', sa.Integer(), nullable=True))
    op.add_column('sales', sa.Column('full_sold', sa.Integer(), nullable=True))
    op.add_column('sales', sa.Column('full_price', sa.Integer(), nullable=True))
    op.add_column('sales', sa.Column('full_amount', sa.Integer(), nullable=True))
    op.add_column('sales', sa.Column('twin_sold', sa.Integer(), nullable=True))
    op.add_column('sales', sa.Column('twin_price', sa.Integer(), nullable=True))
    op.add_column('sales', sa.Column('twin_amount', sa.Integer(), nullable=True))
    op.drop_column('sales', 'only_mattress_sold')
    op.drop_column('sales', 'mattress_price')
    op.drop_column('sales', 'set_sold')
    op.drop_column('sales', 'set_price')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales', sa.Column('set_price', sa.INTEGER(), nullable=True))
    op.add_column('sales', sa.Column('set_sold', sa.INTEGER(), nullable=True))
    op.add_column('sales', sa.Column('mattress_price', sa.INTEGER(), nullable=True))
    op.add_column('sales', sa.Column('only_mattress_sold', sa.INTEGER(), nullable=True))
    op.drop_column('sales', 'twin_amount')
    op.drop_column('sales', 'twin_price')
    op.drop_column('sales', 'twin_sold')
    op.drop_column('sales', 'full_amount')
    op.drop_column('sales', 'full_price')
    op.drop_column('sales', 'full_sold')
    op.drop_column('sales', 'king_amount')
    op.drop_column('sales', 'king_price')
    op.drop_column('sales', 'king_sold')
    op.drop_column('sales', 'queen_amount')
    op.drop_column('sales', 'queen_price')
    op.drop_column('sales', 'queen_sold')
    # ### end Alembic commands ###
