"""create posts table

Revision ID: d03d1687c415
Revises: 
Create Date: 2023-11-26 04:57:00.580030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd03d1687c415'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('title', sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_table('posts')
