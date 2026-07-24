from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
from matplotlib.ticker import FuncFormatter


PROJECT_ROOT = Path(__file__).resolve().parent.parent

CLEANED_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "ecommerce_sales_cleaned.csv"
)

STATIC_CHARTS_DIRECTORY = (
    PROJECT_ROOT
    / "reports"
    / "charts"
    / "static"
)

INTERACTIVE_CHARTS_DIRECTORY = (
    PROJECT_ROOT
    / "reports"
    / "charts"
    / "interactive"
)


def load_data() -> pd.DataFrame:
    """Load the cleaned ecommerce dataset."""

    if not CLEANED_DATA_PATH.exists():
        raise FileNotFoundError(
            f"Cleaned dataset not found: {CLEANED_DATA_PATH}"
        )

    dataframe = pd.read_csv(
        CLEANED_DATA_PATH,
        parse_dates=["OrderDate"],
    )

    return dataframe


def get_delivered_orders(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Return successfully delivered orders only."""

    return dataframe[
        dataframe["OrderStatus"] == "Delivered"
    ].copy()


def format_currency(value: float, position: int) -> str:
    """Format large PKR values for chart axes."""

    if value >= 1_000_000:
        return f"PKR {value / 1_000_000:.1f}M"

    if value >= 1_000:
        return f"PKR {value / 1_000:.0f}K"

    return f"PKR {value:.0f}"


def prepare_directories() -> None:
    """Create output directories for chart files."""

    STATIC_CHARTS_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    INTERACTIVE_CHARTS_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )


def save_matplotlib_chart(
    file_name: str,
) -> None:
    """Save and close the current Matplotlib chart."""

    output_path = (
        STATIC_CHARTS_DIRECTORY
        / file_name
    )

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight",
    )

    plt.close()

    print(f"Saved static chart: {output_path}")


def create_monthly_sales_chart(
    delivered_orders: pd.DataFrame,
) -> None:
    """Create monthly revenue charts."""

    monthly_sales = (
        delivered_orders
        .groupby(
            "YearMonth",
            as_index=False,
        )
        .agg(
            NetSales=("NetSales", "sum"),
            Orders=("OrderID", "nunique"),
        )
        .sort_values("YearMonth")
    )

    plt.figure(figsize=(14, 7))

    plt.plot(
        monthly_sales["YearMonth"],
        monthly_sales["NetSales"],
        marker="o",
        linewidth=2.5,
    )

    plt.title(
        "Monthly E-commerce Revenue Trend",
        fontsize=18,
        fontweight="bold",
        pad=20,
    )

    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Net Revenue", fontsize=12)

    plt.xticks(
        rotation=45,
        ha="right",
    )

    plt.grid(
        axis="y",
        alpha=0.3,
    )

    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(format_currency)
    )

    save_matplotlib_chart(
        "monthly_sales_trend.png"
    )

    interactive_figure = px.line(
        monthly_sales,
        x="YearMonth",
        y="NetSales",
        markers=True,
        title="Monthly E-commerce Revenue Trend",
        labels={
            "YearMonth": "Month",
            "NetSales": "Net Revenue",
        },
    )

    interactive_figure.update_layout(
        template="plotly_white",
        hovermode="x unified",
    )

    interactive_figure.update_traces(
        line_width=3,
        marker_size=8,
    )

    interactive_figure.write_html(
        INTERACTIVE_CHARTS_DIRECTORY
        / "monthly_sales_trend.html"
    )


def create_category_sales_chart(
    delivered_orders: pd.DataFrame,
) -> None:
    """Create category revenue charts."""

    category_sales = (
        delivered_orders
        .groupby(
            "Category",
            as_index=False,
        )
        .agg(
            NetSales=("NetSales", "sum"),
            QuantitySold=("Quantity", "sum"),
        )
        .sort_values(
            "NetSales",
            ascending=False,
        )
    )

    plt.figure(figsize=(12, 7))

    bars = plt.bar(
        category_sales["Category"],
        category_sales["NetSales"],
    )

    plt.title(
        "Revenue by Product Category",
        fontsize=18,
        fontweight="bold",
        pad=20,
    )

    plt.xlabel("Category", fontsize=12)
    plt.ylabel("Net Revenue", fontsize=12)

    plt.xticks(
        rotation=25,
        ha="right",
    )

    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(format_currency)
    )

    for bar in bars:
        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width() / 2,
            height,
            f"{height / 1_000_000:.1f}M",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    save_matplotlib_chart(
        "category_sales.png"
    )

    interactive_figure = px.bar(
        category_sales,
        x="Category",
        y="NetSales",
        text_auto=".3s",
        title="Revenue by Product Category",
        labels={
            "Category": "Product Category",
            "NetSales": "Net Revenue",
        },
    )

    interactive_figure.update_layout(
        template="plotly_white"
    )

    interactive_figure.write_html(
        INTERACTIVE_CHARTS_DIRECTORY
        / "category_sales.html"
    )


def create_top_products_chart(
    delivered_orders: pd.DataFrame,
) -> None:
    """Create a chart of the top products by revenue."""

    top_products = (
        delivered_orders
        .groupby(
            "Product",
            as_index=False,
        )
        .agg(
            NetSales=("NetSales", "sum"),
            QuantitySold=("Quantity", "sum"),
        )
        .sort_values(
            "NetSales",
            ascending=False,
        )
        .head(10)
        .sort_values("NetSales")
    )

    plt.figure(figsize=(12, 8))

    plt.barh(
        top_products["Product"],
        top_products["NetSales"],
    )

    plt.title(
        "Top 10 Products by Revenue",
        fontsize=18,
        fontweight="bold",
        pad=20,
    )

    plt.xlabel("Net Revenue", fontsize=12)
    plt.ylabel("Product", fontsize=12)

    plt.gca().xaxis.set_major_formatter(
        FuncFormatter(format_currency)
    )

    plt.grid(
        axis="x",
        alpha=0.3,
    )

    save_matplotlib_chart(
        "top_products.png"
    )

    interactive_figure = px.bar(
        top_products,
        x="NetSales",
        y="Product",
        orientation="h",
        text_auto=".3s",
        title="Top 10 Products by Revenue",
        labels={
            "NetSales": "Net Revenue",
            "Product": "Product",
        },
    )

    interactive_figure.update_layout(
        template="plotly_white"
    )

    interactive_figure.write_html(
        INTERACTIVE_CHARTS_DIRECTORY
        / "top_products.html"
    )


def create_city_sales_chart(
    delivered_orders: pd.DataFrame,
) -> None:
    """Create city-level revenue charts."""

    city_sales = (
        delivered_orders
        .groupby(
            "City",
            as_index=False,
        )
        .agg(
            NetSales=("NetSales", "sum"),
            Orders=("OrderID", "nunique"),
        )
        .sort_values(
            "NetSales",
            ascending=False,
        )
        .head(10)
    )

    plt.figure(figsize=(13, 7))

    plt.bar(
        city_sales["City"],
        city_sales["NetSales"],
    )

    plt.title(
        "Top Cities by Revenue",
        fontsize=18,
        fontweight="bold",
        pad=20,
    )

    plt.xlabel("City", fontsize=12)
    plt.ylabel("Net Revenue", fontsize=12)

    plt.xticks(
        rotation=35,
        ha="right",
    )

    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(format_currency)
    )

    save_matplotlib_chart(
        "city_sales.png"
    )

    interactive_figure = px.bar(
        city_sales,
        x="City",
        y="NetSales",
        hover_data=["Orders"],
        title="Top Cities by Revenue",
        labels={
            "City": "City",
            "NetSales": "Net Revenue",
            "Orders": "Delivered Orders",
        },
    )

    interactive_figure.update_layout(
        template="plotly_white"
    )

    interactive_figure.write_html(
        INTERACTIVE_CHARTS_DIRECTORY
        / "city_sales.html"
    )


def create_order_status_chart(
    dataframe: pd.DataFrame,
) -> None:
    """Create order status distribution charts."""

    status_summary = (
        dataframe
        .groupby(
            "OrderStatus",
            as_index=False,
        )
        .agg(
            Orders=("OrderID", "nunique")
        )
        .sort_values(
            "Orders",
            ascending=False,
        )
    )

    plt.figure(figsize=(11, 7))

    plt.bar(
        status_summary["OrderStatus"],
        status_summary["Orders"],
    )

    plt.title(
        "Order Status Distribution",
        fontsize=18,
        fontweight="bold",
        pad=20,
    )

    plt.xlabel("Order Status", fontsize=12)
    plt.ylabel("Number of Orders", fontsize=12)

    plt.xticks(
        rotation=30,
        ha="right",
    )

    save_matplotlib_chart(
        "order_status_distribution.png"
    )

    interactive_figure = px.pie(
        status_summary,
        names="OrderStatus",
        values="Orders",
        hole=0.55,
        title="Order Status Distribution",
    )

    interactive_figure.update_layout(
        template="plotly_white"
    )

    interactive_figure.update_traces(
        textposition="inside",
        textinfo="percent+label",
    )

    interactive_figure.write_html(
        INTERACTIVE_CHARTS_DIRECTORY
        / "order_status_distribution.html"
    )


def create_payment_method_chart(
    delivered_orders: pd.DataFrame,
) -> None:
    """Create payment method usage charts."""

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
            "Orders",
            ascending=False,
        )
    )

    plt.figure(figsize=(13, 7))

    plt.bar(
        payment_summary["PaymentMethod"],
        payment_summary["Orders"],
    )

    plt.title(
        "Delivered Orders by Payment Method",
        fontsize=18,
        fontweight="bold",
        pad=20,
    )

    plt.xlabel("Payment Method", fontsize=12)
    plt.ylabel("Delivered Orders", fontsize=12)

    plt.xticks(
        rotation=30,
        ha="right",
    )

    save_matplotlib_chart(
        "payment_methods.png"
    )

    interactive_figure = px.bar(
        payment_summary,
        x="PaymentMethod",
        y="Orders",
        hover_data=["NetSales"],
        title="Delivered Orders by Payment Method",
        labels={
            "PaymentMethod": "Payment Method",
            "Orders": "Delivered Orders",
            "NetSales": "Net Revenue",
        },
    )

    interactive_figure.update_layout(
        template="plotly_white"
    )

    interactive_figure.write_html(
        INTERACTIVE_CHARTS_DIRECTORY
        / "payment_methods.html"
    )


def create_weekday_sales_chart(
    delivered_orders: pd.DataFrame,
) -> None:
    """Create weekday revenue charts."""

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

    plt.figure(figsize=(12, 7))

    plt.plot(
        weekday_sales["DayName"],
        weekday_sales["NetSales"],
        marker="o",
        linewidth=2.5,
    )

    plt.title(
        "Revenue by Day of the Week",
        fontsize=18,
        fontweight="bold",
        pad=20,
    )

    plt.xlabel("Day", fontsize=12)
    plt.ylabel("Net Revenue", fontsize=12)

    plt.xticks(rotation=20)

    plt.grid(
        axis="y",
        alpha=0.3,
    )

    plt.gca().yaxis.set_major_formatter(
        FuncFormatter(format_currency)
    )

    save_matplotlib_chart(
        "weekday_sales.png"
    )

    interactive_figure = px.line(
        weekday_sales,
        x="DayName",
        y="NetSales",
        markers=True,
        hover_data=["Orders"],
        title="Revenue by Day of the Week",
        labels={
            "DayName": "Day",
            "NetSales": "Net Revenue",
            "Orders": "Delivered Orders",
        },
    )

    interactive_figure.update_layout(
        template="plotly_white"
    )

    interactive_figure.write_html(
        INTERACTIVE_CHARTS_DIRECTORY
        / "weekday_sales.html"
    )


def generate_all_visualizations() -> None:
    """Generate all static and interactive visualizations."""

    prepare_directories()

    dataframe = load_data()

    delivered_orders = get_delivered_orders(
        dataframe
    )

    create_monthly_sales_chart(
        delivered_orders
    )

    create_category_sales_chart(
        delivered_orders
    )

    create_top_products_chart(
        delivered_orders
    )

    create_city_sales_chart(
        delivered_orders
    )

    create_order_status_chart(
        dataframe
    )

    create_payment_method_chart(
        delivered_orders
    )

    create_weekday_sales_chart(
        delivered_orders
    )

    print("\nAll visualizations generated successfully.")


if __name__ == "__main__":
    generate_all_visualizations()