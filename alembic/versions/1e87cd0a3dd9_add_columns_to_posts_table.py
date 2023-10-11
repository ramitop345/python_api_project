"""add columns to posts table

Revision ID: 1e87cd0a3dd9
Revises: 9c7eee0856c4
Create Date: 2023-10-11 17:35:18.215312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1e87cd0a3dd9'
down_revision: Union[str, None] = '9c7eee0856c4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(), nullable = False, server_default='1'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable= False, server_default= sa.text('now()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
