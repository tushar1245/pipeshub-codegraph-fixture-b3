"""initial schema"""
revision = "0001"
down_revision = None


def upgrade(op) -> None:
    op.create_table("orders", ("id", "text"), ("status", "text"))


def downgrade(op) -> None:
    op.drop_table("orders")
