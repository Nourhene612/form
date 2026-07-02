"""add outil gestion to gestion projet

Revision ID: a1d4e7b8c9f0
Revises: e8f1c7a0b2d4
Create Date: 2026-07-01 00:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1d4e7b8c9f0'
down_revision: Union[str, None] = 'e8f1c7a0b2d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('gestion_projet', sa.Column('outil_gestion', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('gestion_projet', 'outil_gestion')