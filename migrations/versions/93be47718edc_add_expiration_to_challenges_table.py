"""Add expiration to Challenges table

Revision ID: 93be47718edc
Revises: 46a278193a94
Create Date: 2023-03-14 20:02:27.554190

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "93be47718edc"
down_revision = "46a278193a94"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("challenges", sa.Column("expiration", sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("challenges", "expiration")
    # ### end Alembic commands ###