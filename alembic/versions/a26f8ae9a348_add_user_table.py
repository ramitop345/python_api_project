"""add user table

Revision ID: a26f8ae9a348
Revises: 320d6aab357f
Create Date: 2023-10-11 17:16:15.068037

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a26f8ae9a348'
down_revision: Union[str, None] = '320d6aab357f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',
                     sa.Column('id', sa.Integer(), nullable = False, primary_key = True), 
                     sa.Column('email', sa.String(250), nullable = False),
                     sa.Column('password', sa.String(400), nullable = False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
