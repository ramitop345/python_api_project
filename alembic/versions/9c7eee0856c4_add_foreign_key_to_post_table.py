"""add foreign key to post table

Revision ID: 9c7eee0856c4
Revises: a26f8ae9a348
Create Date: 2023-10-11 17:26:41.464059

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c7eee0856c4'
down_revision: Union[str, None] = 'a26f8ae9a348'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table= 'posts',
                           referent_table="users", local_cols=['user_id'], 
                           remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'user_id')
    pass
