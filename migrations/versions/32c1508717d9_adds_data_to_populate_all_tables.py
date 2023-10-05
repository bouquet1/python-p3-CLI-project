"""adds data to populate all tables

Revision ID: 32c1508717d9
Revises: ad6fc8cb4a27
Create Date: 2023-10-04 21:36:45.639810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32c1508717d9'
down_revision: Union[str, None] = 'ad6fc8cb4a27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales', sa.Column('only_mattress_sold', sa.Integer(), nullable=True))
    op.drop_column('sales', 'mattress_sold')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sales', sa.Column('mattress_sold', sa.INTEGER(), nullable=True))
    op.drop_column('sales', 'only_mattress_sold')
    # ### end Alembic commands ###
