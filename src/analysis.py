from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEANED_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "ecommerce_sales_cleaned.csv"
)

REPORTS_DIRECTORY = (
    PROJECT_ROOT
    / "reports"
    / "analysis"
)


def load_cleaned_data(file_path: Path) -> pd.DataFrame:
    """Load the cleaned ecommerce dataset."""

    if not file_path.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found: {file_path}"
        )

    dataframe = pd.read_csv(
        file_path,
        parse_dates=["OrderDate"],
    )

    print("Cleaned dataset loaded successfully.")
    print(f"Rows: {len(dataframe)}")

    return dataframe


def get_delivered_orders(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Return only successfully delivered orders."""

    delivered_orders = dataframe[
        dataframe["OrderStatus"] == "Delivered"
    ].copy()

    return delivered_orders


def get_top_value(
    dataframe: pd.DataFrame,
    group_column: str,
) -> str:
    """Return the highest-performing value by net sales."""

    if dataframe.empty:
        return "N/A"

    grouped_data = (
        dataframe
        .groupby(
            group_column,
            as_index=False,
        )
        .agg(
            NetSales=("NetSales", "sum")
        )
        .sort_values(
            by="NetSales",
            ascending=False,
        )
    )

    return str(
        grouped_data.iloc[0][group_column]
    )


def calculate_kpis(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate the main ecommerce business KPIs."""

    delivered_orders = get_delivered_orders(dataframe)

    total_orders = dataframe["OrderID"].nunique()

    delivered_order_count = (
        delivered_orders["OrderID"].nunique()
    )

    total_customers = dataframe[
        "CustomerID"
    ].nunique()

    total_revenue = delivered_orders[
        "NetSales"
    ].sum()

    total_discount = delivered_orders[
        "DiscountAmount"
    ].sum()

    average_order_value = (
        total_revenue / delivered_order_count
        if delivered_order_count > 0
        else 0
    )

    delivery_rate = (
        delivered_order_count / total_orders * 100
        if total_orders > 0
        else 0
    )

    top_product = get_top_value(
        delivered_orders,
        "Product",
    )

    top_category = get_top_value(
        delivered_orders,
        "Category",
    )

    top_city = get_top_value(
        delivered_orders,
        "City",
    )

    kpi_data = {
        "TotalOrders": total_orders,
        "DeliveredOrders": delivered_order_count,
        "TotalCustomers": total_customers,
        "TotalRevenue": round(total_revenue, 2),
        "AverageOrderValue": round(
            average_order_value,
            2,
        ),
        "TotalDiscount": round(
            total_discount,
            2,
        ),
        "DeliveryRatePercentage": round(
            delivery_rate,
            2,
        ),
        "TopProduct": top_product,
        "TopCategory": top_category,
        "TopCity": top_city,
    }

    return pd.DataFrame([kpi_data])


def analyze_monthly_sales(
    delivered_orders: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate monthly revenue and order volume."""

    monthly_sales = (
        delivered_orders
        .groupby(
            "YearMonth",
            as_index=False,
        )
        .agg(
            NetSales=("NetSales", "sum"),
            Orders=("OrderID", "nunique"),
            Customers=("CustomerID", "nunique"),
        )
        .sort_values("YearMonth")
    )

    monthly_sales["NetSales"] = (
        monthly_sales["NetSales"].round(2)
    )

    return monthly_sales


def analyze_category_sales(
    delivered_orders: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate sales performance by category."""

    category_sales = (
        delivered_orders
        .groupby(
            "Category",
            as_index=False,
        )
        .agg(
            NetSales=("NetSales", "sum"),
            QuantitySold=("Quantity", "sum"),
            Orders=("OrderID", "nunique"),
        )
        .sort_values(
            by="NetSales",
            ascending=False,
        )
    )

    category_sales["NetSales"] = (
        category_sales["NetSales"].round(2)
    )

    return category_sales


def analyze_product_sales(
    delivered_orders: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate sales performance by product."""

    product_sales = (
        delivered_orders
        .groupby(
            ["Category", "Product"],
            as_index=False,
        )
        .agg(
            NetSales=("NetSales", "sum"),
            QuantitySold=("Quantity", "sum"),
            Orders=("OrderID", "nunique"),
        )
        .sort_values(
            by="NetSales",
            ascending=False,
        )
        .head(10)
    )

    product_sales["NetSales"] = (
        product_sales["NetSales"].round(2)
    )

    return product_sales


def analyze_city_sales(
    delivered_orders: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate sales performance by city."""

    city_sales = (
        delivered_orders
        .groupby(
            "City",
            as_index=False,
        )
        .agg(
            NetSales=("NetSales", "sum"),
            Orders=("OrderID", "nunique"),
            Customers=("CustomerID", "nunique"),
        )
        .sort_values(
            by="NetSales",
            ascending=False,
        )
    )

    city_sales["NetSales"] = (
        city_sales["NetSales"].round(2)
    )

    return city_sales


def analyze_payment_methods(
    delivered_orders: pd.DataFrame,
) -> pd.DataFrame:
    """Analyze delivered orders by payment method."""

    payment_summary = (
        delivered_orders
        .groupby(
            "PaymentMethod",
            as_index=False,
        )
        .agg(
            Orders=("OrderID", "nunique"),
            NetSales=("NetSales", "sum"),
        )
        .sort_values(
            by="Orders",
            ascending=False,
        )
    )

    payment_summary["NetSales"] = (
        payment_summary["NetSales"].round(2)
    )

    return payment_summary


def analyze_order_status(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Analyze the complete order status distribution."""

    status_summary = (
        dataframe
        .groupby(
            "OrderStatus",
            as_index=False,
        )
        .agg(
            Orders=("OrderID", "nunique"),
            OrderValue=("NetSales", "sum"),
        )
        .sort_values(
            by="Orders",
            ascending=False,
        )
    )

    status_summary["OrderValue"] = (
        status_summary["OrderValue"].round(2)
    )

    return status_summary


def analyze_weekday_sales(
    delivered_orders: pd.DataFrame,
) -> pd.DataFrame:
    """Calculate sales performance by day of the week."""

    weekday_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]

    weekday_sales = (
        delivered_orders
        .groupby(
            "DayName",
            as_index=False,
        )
        .agg(
            NetSales=("NetSales", "sum"),
            Orders=("OrderID", "nunique"),
        )
    )

    weekday_sales["DayName"] = pd.Categorical(
        weekday_sales["DayName"],
        categories=weekday_order,
        ordered=True,
    )

    weekday_sales = weekday_sales.sort_values(
        "DayName"
    )

    weekday_sales["NetSales"] = (
        weekday_sales["NetSales"].round(2)
    )

    return weekday_sales


def create_analysis_reports(
    dataframe: pd.DataFrame,
) -> dict[str, pd.DataFrame]:
    """Create all KPI and analysis tables."""

    delivered_orders = get_delivered_orders(
        dataframe
    )

    reports = {
        "kpis": calculate_kpis(dataframe),
        "monthly_sales": analyze_monthly_sales(
            delivered_orders
        ),
        "category_sales": analyze_category_sales(
            delivered_orders
        ),
        "top_products": analyze_product_sales(
            delivered_orders
        ),
        "city_sales": analyze_city_sales(
            delivered_orders
        ),
        "payment_methods": analyze_payment_methods(
            delivered_orders
        ),
        "order_status": analyze_order_status(
            dataframe
        ),
        "weekday_sales": analyze_weekday_sales(
            delivered_orders
        ),
    }

    return reports


def save_analysis_reports(
    reports: dict[str, pd.DataFrame],
) -> None:
    """Save all analysis tables as CSV files."""

    REPORTS_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    for report_name, report_dataframe in reports.items():
        output_path = (
            REPORTS_DIRECTORY
            / f"{report_name}.csv"
        )

        report_dataframe.to_csv(
            output_path,
            index=False,
        )

        print(f"Saved: {output_path}")


def print_kpi_summary(
    kpi_dataframe: pd.DataFrame,
) -> None:
    """Display the main KPIs in the terminal."""

    kpis = kpi_dataframe.iloc[0]

    print("\nE-commerce KPI Summary")
    print("-" * 40)

    print(
        f"Total Orders: "
        f"{int(kpis['TotalOrders']):,}"
    )

    print(
        f"Delivered Orders: "
        f"{int(kpis['DeliveredOrders']):,}"
    )

    print(
        f"Total Customers: "
        f"{int(kpis['TotalCustomers']):,}"
    )

    print(
        f"Total Revenue: "
        f"PKR {kpis['TotalRevenue']:,.2f}"
    )

    print(
        f"Average Order Value: "
        f"PKR {kpis['AverageOrderValue']:,.2f}"
    )

    print(
        f"Total Discount: "
        f"PKR {kpis['TotalDiscount']:,.2f}"
    )

    print(
        f"Delivery Rate: "
        f"{kpis['DeliveryRatePercentage']:.2f}%"
    )

    print(
        f"Top Product: "
        f"{kpis['TopProduct']}"
    )

    print(
        f"Top Category: "
        f"{kpis['TopCategory']}"
    )

    print(
        f"Top City: "
        f"{kpis['TopCity']}"
    )


def run_analysis() -> dict[str, pd.DataFrame]:
    """Run the complete ecommerce analysis pipeline."""

    dataframe = load_cleaned_data(
        CLEANED_DATA_PATH
    )

    reports = create_analysis_reports(
        dataframe
    )

    save_analysis_reports(
        reports
    )

    print_kpi_summary(
        reports["kpis"]
    )

    return reports


if __name__ == "__main__":
    analysis_reports = run_analysis()