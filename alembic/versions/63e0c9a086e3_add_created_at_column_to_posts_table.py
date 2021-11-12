"""add created_at column to posts table

Revision ID: 63e0c9a086e3
Revises: 1f4ffad63990
Create Date: 2021-11-12 12:44:35.829765

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import false, null


# revision identifiers, used by Alembic.
revision = "63e0c9a086e3"
down_revision = "1f4ffad63990"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )


def downgrade():
    op.drop_column('posts', 'created_at')
