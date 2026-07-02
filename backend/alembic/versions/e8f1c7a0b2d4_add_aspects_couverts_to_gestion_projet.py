"""add aspects couverts to gestion projet

Revision ID: e8f1c7a0b2d4
Revises: d3e29878871a
Create Date: 2026-07-01 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8f1c7a0b2d4'
down_revision: Union[str, None] = 'd3e29878871a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('gestion_projet', sa.Column('aspects_couverts', sa.JSON(), nullable=True))


def downgrade() -> None:
    op.drop_column('gestion_projet', 'aspects_couverts')