"""add_is_verified

Revision ID: fe73c912f416
Revises: fdf8821871d7
Create Date: 2026-03-12 17:17:11.122273

"""
from alembic import op
import sqlalchemy as sa


revision = 'fe73c912f416'
down_revision = 'fdf8821871d7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('users', sa.Column('is_verified', sa.Boolean(), server_default='false', nullable=False))

def downgrade():
    op.drop_column('users', 'is_verified')

