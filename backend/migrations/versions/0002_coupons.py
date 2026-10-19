"""add coupons"""
revision = "0002"
down_revision = "0001"


def upgrade(op) -> None:
    op.create_table("coupons", ("code", "text"), ("percent", "integer"))


def downgrade(op) -> None:
    op.drop_table("coupons")
