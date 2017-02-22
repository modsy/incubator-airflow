"""add_colum_params_to_dag_run

Revision ID: 91d15ffd0648
Revises: 2e82aab8ef20
Create Date: 2017-02-21 16:35:48.193198

"""

# revision identifiers, used by Alembic.
revision = '91d15ffd0648'
down_revision = '2e82aab8ef20'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('dag_run', sa.Column('params', sa.PickleType))


def downgrade():
    op.drop_column('dag_run', 'params')
