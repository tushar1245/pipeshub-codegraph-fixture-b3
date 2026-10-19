"""Seeds a local database with demo data."""
from app.main import create_app
from app.testing.fixtures_loader import load_demo_catalogue


def main() -> None:
    create_app()
    print(f"loaded {load_demo_catalogue()} products")


if __name__ == "__main__":
    main()
