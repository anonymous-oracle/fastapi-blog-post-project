"""create posts table

Revision ID: 1f4ffad63990
Revises: 
Create Date: 2021-11-12 11:56:19.037506

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1f4ffad63990"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("content", sa.String, nullable=False),
        sa.Column("published", sa.Boolean, server_default="True", nullable=False),
    )


def downgrade():
    op.drop_table("posts")
