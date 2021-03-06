"""empty message

Revision ID: 771caf5fbd7e
Revises: 077ff321e442
Create Date: 2018-11-18 21:48:29.947361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '771caf5fbd7e'
down_revision = '077ff321e442'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('active', sa.Boolean(), nullable=True))
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_column('users', 'active')
    # ### end Alembic commands ###
