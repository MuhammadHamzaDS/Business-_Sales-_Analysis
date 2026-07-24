from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

RAW_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "ecommerce_sales_raw.csv"
)

PROCESSED_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "ecommerce_sales_cleaned.csv"
)


def load_data(file_path: Path) -> pd.DataFrame:
    """Load ecommerce sales data from a CSV file."""

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    dataframe = pd.read_csv(file_path)

    print("Raw dataset loaded successfully.")
    print(f"Original rows: {len(dataframe)}")

    return dataframe


def remove_duplicates(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Remove duplicate records from the dataset."""

    duplicate_count = dataframe.duplicated().sum()

    dataframe = dataframe.drop_duplicates().copy()

    print(f"Duplicate rows removed: {duplicate_count}")

    return dataframe


def handle_missing_values(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Handle missing values in important columns."""

    missing_city_count = dataframe["City"].isna().sum()

    dataframe["City"] = (
        dataframe["City"]
        .fillna("Unknown")
        .str.strip()
    )

    print(
        f"Missing city values replaced: "
        f"{missing_city_count}"
    )

    return dataframe


def convert_data_types(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Convert columns to appropriate data types."""

    dataframe["OrderDate"] = pd.to_datetime(
        dataframe["OrderDate"],
        errors="coerce",
    )

    numeric_columns = [
        "Quantity",
        "UnitPrice",
        "DiscountPercentage",
    ]

    for column in numeric_columns:
        dataframe[column] = pd.to_numeric(
            dataframe[column],
            errors="coerce",
        )

    invalid_date_count = dataframe["OrderDate"].isna().sum()

    if invalid_date_count > 0:
        dataframe = dataframe.dropna(
            subset=["OrderDate"]
        ).copy()

    print(
        f"Rows with invalid dates removed: "
        f"{invalid_date_count}"
    )

    return dataframe


def remove_invalid_records(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Remove records containing invalid numeric values."""

    rows_before = len(dataframe)

    dataframe = dataframe.dropna(
        subset=[
            "Quantity",
            "UnitPrice",
            "DiscountPercentage",
        ]
    ).copy()

    dataframe = dataframe[
        (dataframe["Quantity"] > 0)
        & (dataframe["UnitPrice"] > 0)
        & (
            dataframe["DiscountPercentage"]
            .between(0, 100)
        )
    ].copy()

    invalid_rows_removed = rows_before - len(dataframe)

    print(
        f"Invalid numeric records removed: "
        f"{invalid_rows_removed}"
    )

    return dataframe


def standardize_text_columns(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Clean and standardize text columns."""

    text_columns = [
        "CustomerName",
        "City",
        "Category",
        "Product",
        "PaymentMethod",
        "OrderStatus",
    ]

    for column in text_columns:
        dataframe[column] = (
            dataframe[column]
            .astype(str)
            .str.strip()
        )

    return dataframe


def calculate_sales_columns(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate gross sales, discount, and net sales."""

    dataframe["GrossSales"] = (
        dataframe["Quantity"]
        * dataframe["UnitPrice"]
    )

    dataframe["DiscountAmount"] = (
        dataframe["GrossSales"]
        * dataframe["DiscountPercentage"]
        / 100
    )

    dataframe["NetSales"] = (
        dataframe["GrossSales"]
        - dataframe["DiscountAmount"]
    )

    money_columns = [
        "UnitPrice",
        "GrossSales",
        "DiscountAmount",
        "NetSales",
    ]

    dataframe[money_columns] = (
        dataframe[money_columns].round(2)
    )

    return dataframe


def create_date_features(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Create additional date-related columns."""

    dataframe["Year"] = (
        dataframe["OrderDate"].dt.year
    )

    dataframe["MonthNumber"] = (
        dataframe["OrderDate"].dt.month
    )

    dataframe["MonthName"] = (
        dataframe["OrderDate"].dt.month_name()
    )

    dataframe["YearMonth"] = (
        dataframe["OrderDate"]
        .dt.to_period("M")
        .astype(str)
    )

    dataframe["DayName"] = (
        dataframe["OrderDate"].dt.day_name()
    )

    return dataframe


def sort_dataset(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Sort records by order date."""

    return (
        dataframe
        .sort_values(
            by="OrderDate",
            ascending=True,
        )
        .reset_index(drop=True)
    )


def save_cleaned_data(
    dataframe: pd.DataFrame,
    file_path: Path,
) -> None:
    """Save the cleaned dataset as a CSV file."""

    file_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    dataframe.to_csv(
        file_path,
        index=False,
    )

    print("\nCleaned dataset saved successfully.")
    print(f"Final rows: {len(dataframe)}")
    print(f"Final columns: {len(dataframe.columns)}")
    print(f"Saved to: {file_path}")


def clean_ecommerce_data() -> pd.DataFrame:
    """Execute the complete data-cleaning pipeline."""

    dataframe = load_data(RAW_DATA_PATH)

    dataframe = remove_duplicates(dataframe)
    dataframe = handle_missing_values(dataframe)
    dataframe = convert_data_types(dataframe)
    dataframe = remove_invalid_records(dataframe)
    dataframe = standardize_text_columns(dataframe)
    dataframe = calculate_sales_columns(dataframe)
    dataframe = create_date_features(dataframe)
    dataframe = sort_dataset(dataframe)

    save_cleaned_data(
        dataframe,
        PROCESSED_DATA_PATH,
    )

    return dataframe


if __name__ == "__main__":
    cleaned_data = clean_ecommerce_data()

    print("\nCleaned Dataset Preview:")
    print(cleaned_data.head())