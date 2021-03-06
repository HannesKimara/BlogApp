"""Add title to blog model

Revision ID: 8766db1f2c50
Revises: 76e94216c804
Create Date: 2020-02-19 01:02:07.542732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8766db1f2c50'
down_revision = '76e94216c804'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('title', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('blogs', 'title')
    # ### end Alembic commands ###
