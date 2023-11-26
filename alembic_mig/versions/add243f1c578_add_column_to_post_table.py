"""add column to post table

Revision ID: add243f1c578
Revises: d03d1687c415
Create Date: 2023-11-26 05:06:38.745206

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'add243f1c578'
down_revision: Union[str, None] = 'd03d1687c415'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column('posts','content')
