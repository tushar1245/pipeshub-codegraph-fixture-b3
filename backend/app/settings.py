import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://acme:acme@localhost:5432/acme")
PAYMENTS_API_KEY = os.getenv("PAYMENTS_API_KEY", "CANARYSECRET-7f3a9c1e5b2d4086")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "AKIAIOSFODNN7EXAMPLE")
CACHE_TTL = float(os.getenv("CACHE_TTL", "300"))
