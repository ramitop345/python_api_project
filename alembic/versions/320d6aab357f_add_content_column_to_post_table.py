"""add content column to post table

Revision ID: 320d6aab357f
Revises: d764c81384a5
Create Date: 2023-10-11 17:10:33.975830

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '320d6aab357f'
down_revision: Union[str, None] = 'd764c81384a5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts',sa.Column('content',sa.String(3000), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
