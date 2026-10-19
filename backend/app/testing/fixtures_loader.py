"""Loads the demo catalogue shown to new tenants during onboarding."""
from app.catalog.importers import import_csv

DEMO = "sku,title\nSKU-1001,Mug\nSKU-1002,Poster\n"


def load_demo_catalogue() -> int:
    return import_csv(DEMO)
