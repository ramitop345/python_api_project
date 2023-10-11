"""create posts table

Revision ID: d764c81384a5
Revises: 
Create Date: 2023-10-11 16:58:44.096691

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd764c81384a5'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable = False, primary_key = True), sa.Column('title', sa.String(250), nullable = False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
