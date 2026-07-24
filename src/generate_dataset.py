from pathlib import Path
import random

import pandas as pd
from faker import Faker


fake = Faker()
Faker.seed(42)
random.seed(42)


OUTPUT_PATH = Path("data/raw/ecommerce_sales_raw.csv")

CITIES = [
    "Lahore",
    "Karachi",
    "Islamabad",
    "Rawalpindi",
    "Faisalabad",
    "Multan",
    "Sahiwal",
    "Peshawar",
    "Quetta",
    "Gujranwala",
]

PRODUCTS = {
    "Electronics": {
        "Laptop": (120000, 250000),
        "Smartphone": (40000, 180000),
        "Headphones": (2000, 25000),
        "Smart Watch": (5000, 45000),
    },
    "Clothing": {
        "T-Shirt": (1200, 3500),
        "Jeans": (2500, 7000),
        "Jacket": (4000, 15000),
        "Shoes": (3000, 18000),
    },
    "Home and Kitchen": {
        "Blender": (5000, 18000),
        "Cookware Set": (8000, 30000),
        "Table Lamp": (2000, 9000),
        "Coffee Maker": (7000, 25000),
    },
    "Books": {
        "Python Programming": (1500, 5000),
        "Data Science Book": (2000, 6500),
        "Machine Learning Book": (2500, 8000),
        "Business Analytics Book": (1800, 6000),
    },
}

PAYMENT_METHODS = [
    "Cash on Delivery",
    "Credit Card",
    "Debit Card",
    "Bank Transfer",
    "Digital Wallet",
]

ORDER_STATUSES = [
    "Delivered",
    "Delivered",
    "Delivered",
    "Processing",
    "Shipped",
    "Cancelled",
    "Returned",
]


def generate_order(order_number: int) -> dict:
    category = random.choice(list(PRODUCTS.keys()))
    product = random.choice(list(PRODUCTS[category].keys()))

    minimum_price, maximum_price = PRODUCTS[category][product]

    quantity = random.randint(1, 5)
    unit_price = random.randint(minimum_price, maximum_price)
    discount_percentage = random.choice([0, 0, 5, 10, 15, 20])

    return {
        "OrderID": f"ORD-{order_number:05d}",
        "OrderDate": fake.date_between(
            start_date="-1y",
            end_date="today",
        ),
        "CustomerID": f"CUST-{random.randint(1000, 9999)}",
        "CustomerName": fake.name(),
        "City": random.choice(CITIES),
        "Category": category,
        "Product": product,
        "Quantity": quantity,
        "UnitPrice": unit_price,
        "DiscountPercentage": discount_percentage,
        "PaymentMethod": random.choice(PAYMENT_METHODS),
        "OrderStatus": random.choice(ORDER_STATUSES),
    }


def generate_dataset(number_of_orders: int = 1500) -> pd.DataFrame:
    orders = [
        generate_order(order_number)
        for order_number in range(1, number_of_orders + 1)
    ]

    dataframe = pd.DataFrame(orders)

    # Introduce a few realistic data-quality issues.
    missing_city_indices = dataframe.sample(
        frac=0.02,
        random_state=42,
    ).index

    dataframe.loc[missing_city_indices, "City"] = None

    duplicated_rows = dataframe.sample(
        n=15,
        random_state=42,
    )

    dataframe = pd.concat(
        [dataframe, duplicated_rows],
        ignore_index=True,
    )

    return dataframe


def save_dataset(dataframe: pd.DataFrame) -> None:
    OUTPUT_PATH.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    dataframe.to_csv(
        OUTPUT_PATH,
        index=False,
    )

    print("Dataset generated successfully.")
    print(f"Rows: {len(dataframe)}")
    print(f"Columns: {len(dataframe.columns)}")
    print(f"Saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    ecommerce_data = generate_dataset(number_of_orders=1500)
    save_dataset(ecommerce_data)