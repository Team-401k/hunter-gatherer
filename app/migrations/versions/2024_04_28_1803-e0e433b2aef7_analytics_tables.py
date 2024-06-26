"""analytics tables

Revision ID: e0e433b2aef7
Revises: 997a6f28ea27
Create Date: 2024-04-28 18:03:53.230413

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e0e433b2aef7"
down_revision: Union[str, None] = "997a6f28ea27"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "analytics",
        sa.Column("month", sa.String(), nullable=False),
        sa.Column("year", sa.String(), nullable=False),
        sa.Column("month_sales", sa.Float(), nullable=True),
        sa.Column("month_fees", sa.Float(), nullable=True),
        sa.Column("month_profit", sa.Float(), nullable=True),
        sa.Column("ytd_sales", sa.Float(), nullable=True),
        sa.Column("ytd_fees", sa.Float(), nullable=True),
        sa.Column("ytd_profit", sa.Float(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("month", "year", name="pk_analytics"),
    )
    op.create_index(op.f("ix_analytics_month"), "analytics", ["month"], unique=False)
    op.create_index(op.f("ix_analytics_year"), "analytics", ["year"], unique=False)
    op.create_table(
        "product_analytics",
        sa.Column("sku", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
        sa.Column("month_sales", sa.Float(), nullable=True),
        sa.Column("month_fees", sa.Float(), nullable=True),
        sa.Column("month_profit", sa.Float(), nullable=True),
        sa.Column("ytd_sales", sa.Float(), nullable=True),
        sa.Column("ytd_fees", sa.Float(), nullable=True),
        sa.Column("ytd_profit", sa.Float(), nullable=True),
        sa.Column("month", sa.String(), nullable=False),
        sa.Column("year", sa.String(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["sku"],
            ["products.sku"],
            name=op.f("fk_product_analytics_sku_products"),
        ),
        sa.PrimaryKeyConstraint("sku", "month", "year", name="pk_product_analytics"),
    )
    op.create_index(
        op.f("ix_product_analytics_month"),
        "product_analytics",
        ["month"],
        unique=False,
    )
    op.create_index(
        op.f("ix_product_analytics_year"),
        "product_analytics",
        ["year"],
        unique=False,
    )
    op.add_column("users", sa.Column("profile_pic", sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "profile_pic")
    op.drop_index(op.f("ix_product_analytics_year"), table_name="product_analytics")
    op.drop_index(op.f("ix_product_analytics_month"), table_name="product_analytics")
    op.drop_table("product_analytics")
    op.drop_index(op.f("ix_analytics_year"), table_name="analytics")
    op.drop_index(op.f("ix_analytics_month"), table_name="analytics")
    op.drop_table("analytics")
    # ### end Alembic commands ###
