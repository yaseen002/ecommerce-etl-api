from src.database.session import SessionLocal, engine
from src.database.models import Base, Product
from datetime import datetime


def extract():
    return [
        {
            "name": "Laptop",
            "price": 1200.0,
            "availability": "In Stock",
            "description": "Powerful laptop",
            "rating": 5,
            "scraped_at": datetime.utcnow(),
        },
        {
            "name": "Smartphone",
            "price": 800.0,
            "availability": "In Stock",
            "description": "Latest smartphone",
            "rating": 4,
            "scraped_at": datetime.utcnow(),
        },
        {
            "name": "Headphones",
            "price": 150.0,
            "availability": "Limited Stock",
            "description": "Noise-cancelling",
            "rating": 4,
            "scraped_at": datetime.utcnow(),
        },
    ]


def load(data):
    db = SessionLocal()

    for item in data:
        product = Product(**item)
        db.add(product)

    db.commit()
    db.close()


def run_pipeline():
    print("Starting ETL pipeline...")

    # 🔥 ensure tables exist
    Base.metadata.create_all(bind=engine)

    data = extract()
    load(data)

    print(f"Loaded {len(data)} products into the database.")
    print("ETL pipeline completed.")


if __name__ == "__main__":
    run_pipeline()