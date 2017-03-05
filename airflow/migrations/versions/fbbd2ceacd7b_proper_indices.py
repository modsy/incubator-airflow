"""proper_indices

Revision ID: fbbd2ceacd7b
Revises: 331d5090c550
Create Date: 2017-02-22 10:45:29.026604

"""

# revision identifiers, used by Alembic.
revision = 'fbbd2ceacd7b'
down_revision = '331d5090c550'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


def upgrade():
    op.create_table('task_instance_timeout',
        sa.Column('id', sa.Integer(), nullable=False, autoincrement=True),
        sa.Column('dag_id', sa.String(length=250), nullable=True),
        sa.Column('task_id', sa.String(length=250), nullable=True),
        sa.Column('execution_date', type_=mysql.DATETIME(fsp=6), nullable=True),
        sa.Column('dagrun_run_id', sa.String(length=250), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('dag_id', 'task_id', 'execution_date'),
        sa.UniqueConstraint('dagrun_run_id'),
    )

def downgrade():
    op.drop_table('task_instance_timeout')
