"""add comment

Revision ID: 281127ea308a
Revises: 5061538be59e
Create Date: 2020-12-18 04:19:39.844867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '281127ea308a'
down_revision = '5061538be59e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('book', sa.String(length=500), nullable=True))
    op.add_column('comments', sa.Column('doc', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'doc')
    op.drop_column('comments', 'book')
    # ### end Alembic commands ###
