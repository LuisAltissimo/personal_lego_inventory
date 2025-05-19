"""create todos table

Revision ID: 5ee0bb61bd88
Revises: e2e2e24040fb
Create Date: 2025-05-19 16:20:59.180264

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5ee0bb61bd88'
down_revision: Union[str, None] = 'e2e2e24040fb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:  

        batch_op.add_column(   
            sa.Column(
                'updated_at',
                sa.DateTime(),
                server_default=sa.text('(CURRENT_TIMESTAMP)'),
                nullable=False,
            )
        )


def downgrade():
    with op.batch_alter_table('users', schema=None) as batch_op:  
        batch_op.drop_column('updated_at')