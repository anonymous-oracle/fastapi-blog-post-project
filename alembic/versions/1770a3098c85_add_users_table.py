"""add users table

Revision ID: 1770a3098c85
Revises: 63e0c9a086e3
Create Date: 2021-11-12 13:01:46.967637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1770a3098c85"
down_revision = "63e0c9a086e3"
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True, nullable=False),
        sa.Column("email", sa.Integer, nullable=False, unique=True),
        sa.Column("password", sa.String, nullable=False),
        sa.Column("salt", sa.String, nullable=False),
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=False,
            server_default=sa.text("NOW()"),
        ),
    )
    


def downgrade():
    op.drop_table("users")
