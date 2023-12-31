"""add authentication

Revision ID: 730ab4143c14
Revises: 21c5c58fbd87
Create Date: 2023-11-02 07:19:48.523938

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '730ab4143c14'
down_revision: Union[str, None] = '21c5c58fbd87'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('hashed_password', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'hashed_password')
    # ### end Alembic commands ###
