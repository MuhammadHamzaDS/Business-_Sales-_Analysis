from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st
from textwrap import dedent


# ---------------------------------------------------------
# Application Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="E-commerce Sales Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "ecommerce_sales_cleaned.csv"
)


# ---------------------------------------------------------
# Custom Styling
# ---------------------------------------------------------

 # ---------------------------------------------------------
# Animated Custom Styling
# ---------------------------------------------------------

st.markdown(
    dedent(
        """
        <style>
            :root {
                --primary-green: #22c55e;
                --dark-green: #071f12;
                --medium-green: #0d3b21;
                --soft-green: rgba(34, 197, 94, 0.12);
                --card-border: rgba(34, 197, 94, 0.22);
            }

            /* ---------------------------------------------
               Global Page Animation
            --------------------------------------------- */

            .stApp {
                background:
                    radial-gradient(
                        circle at 8% 15%,
                        rgba(34, 197, 94, 0.06),
                        transparent 28%
                    ),
                    radial-gradient(
                        circle at 92% 85%,
                        rgba(16, 185, 129, 0.05),
                        transparent 30%
                    );
                animation: appFadeIn 0.7s ease-out both;
            }

            .block-container {
                padding-top: 1.5rem;
                padding-bottom: 2rem;
                animation: pageSlideUp 0.75s
                    cubic-bezier(0.22, 1, 0.36, 1) both;
            }

            @keyframes appFadeIn {
                from {
                    opacity: 0;
                }

                to {
                    opacity: 1;
                }
            }

            @keyframes pageSlideUp {
                from {
                    opacity: 0;
                    transform: translateY(22px);
                }

                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            /* ---------------------------------------------
               Animated Dashboard Header
            --------------------------------------------- */

            .dashboard-header {
                position: relative;
                overflow: hidden;
                isolation: isolate;

                padding: 2rem 2.2rem;
                margin-bottom: 1.6rem;

                border-radius: 20px;
                border: 1px solid rgba(34, 197, 94, 0.35);

                background:
                    linear-gradient(
                        125deg,
                        #03160c,
                        #092d19,
                        #0d4727,
                        #071f12
                    );

                background-size: 300% 300%;

                box-shadow:
                    0 20px 50px rgba(0, 0, 0, 0.18),
                    inset 0 1px 0 rgba(255, 255, 255, 0.05);

                animation:
                    headerEntrance 0.85s
                        cubic-bezier(0.16, 1, 0.3, 1) both,
                    gradientMovement 10s ease infinite;
            }

            .dashboard-header::before {
                content: "";
                position: absolute;
                inset: 0;
                z-index: -1;

                background-image:
                    linear-gradient(
                        rgba(255, 255, 255, 0.025) 1px,
                        transparent 1px
                    ),
                    linear-gradient(
                        90deg,
                        rgba(255, 255, 255, 0.025) 1px,
                        transparent 1px
                    );

                background-size: 35px 35px;
                mask-image:
                    linear-gradient(
                        to right,
                        black,
                        transparent
                    );
            }

            .dashboard-header::after {
                content: "";
                position: absolute;
                top: -30%;
                left: -35%;

                width: 28%;
                height: 170%;

                background:
                    linear-gradient(
                        90deg,
                        transparent,
                        rgba(255, 255, 255, 0.09),
                        transparent
                    );

                transform: rotate(18deg);
                animation: headerShine 7s ease-in-out infinite;
            }

            @keyframes headerEntrance {
                from {
                    opacity: 0;
                    transform:
                        translateY(-20px)
                        scale(0.98);
                }

                to {
                    opacity: 1;
                    transform:
                        translateY(0)
                        scale(1);
                }
            }

            @keyframes gradientMovement {
                0% {
                    background-position: 0% 50%;
                }

                50% {
                    background-position: 100% 50%;
                }

                100% {
                    background-position: 0% 50%;
                }
            }

            @keyframes headerShine {
                0%,
                25% {
                    left: -40%;
                }

                60%,
                100% {
                    left: 125%;
                }
            }

            /* ---------------------------------------------
               Header Content
            --------------------------------------------- */

            .header-content {
                position: relative;
                z-index: 3;
                max-width: 780px;
            }

            .dashboard-eyebrow {
                display: inline-flex;
                align-items: center;
                gap: 0.5rem;

                margin-bottom: 0.75rem;
                padding: 0.35rem 0.8rem;

                color: #86efac;
                background: rgba(34, 197, 94, 0.12);
                border: 1px solid rgba(34, 197, 94, 0.25);
                border-radius: 999px;

                font-size: 0.76rem;
                font-weight: 700;
                letter-spacing: 0.09rem;
                text-transform: uppercase;

                animation: contentSlide 0.7s 0.15s both;
            }

            .live-indicator {
                width: 8px;
                height: 8px;

                border-radius: 50%;
                background: #22c55e;

                box-shadow:
                    0 0 0 0 rgba(34, 197, 94, 0.65);

                animation: livePulse 1.8s infinite;
            }

            @keyframes livePulse {
                0% {
                    box-shadow:
                        0 0 0 0 rgba(34, 197, 94, 0.65);
                }

                70% {
                    box-shadow:
                        0 0 0 10px rgba(34, 197, 94, 0);
                }

                100% {
                    box-shadow:
                        0 0 0 0 rgba(34, 197, 94, 0);
                }
            }

            .dashboard-title {
                margin: 0 0 0.4rem 0;

                color: #ffffff;
                font-size: clamp(2rem, 4vw, 3rem);
                font-weight: 850;
                line-height: 1.1;
                letter-spacing: -0.05rem;

                animation: contentSlide 0.75s 0.25s both;
            }

            .dashboard-title span {
                color: #4ade80;
                text-shadow:
                    0 0 30px rgba(74, 222, 128, 0.22);
            }

            .dashboard-subtitle {
                max-width: 680px;
                margin: 0;

                color: #c8d8cd;
                font-size: 1rem;
                line-height: 1.7;

                animation: contentSlide 0.75s 0.38s both;
            }

            @keyframes contentSlide {
                from {
                    opacity: 0;
                    transform: translateX(-22px);
                }

                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            /* ---------------------------------------------
               Floating Motion Graphics
            --------------------------------------------- */

            .motion-layer {
                position: absolute;
                inset: 0;
                z-index: 1;
                pointer-events: none;
            }

            .motion-orb {
                position: absolute;
                display: block;

                border-radius: 50%;
                filter: blur(1px);

                background:
                    radial-gradient(
                        circle at 30% 30%,
                        rgba(134, 239, 172, 0.85),
                        rgba(34, 197, 94, 0.18) 45%,
                        transparent 72%
                    );
            }

            .orb-one {
                width: 150px;
                height: 150px;
                right: 5%;
                top: -32px;

                animation: floatOrbOne 6s
                    ease-in-out infinite;
            }

            .orb-two {
                width: 90px;
                height: 90px;
                right: 18%;
                bottom: -30px;

                opacity: 0.65;

                animation: floatOrbTwo 7s
                    ease-in-out infinite;
            }

            .orb-three {
                width: 34px;
                height: 34px;
                right: 31%;
                top: 28%;

                opacity: 0.8;

                animation: smallOrbFloat 4s
                    ease-in-out infinite;
            }

            @keyframes floatOrbOne {
                0%,
                100% {
                    transform:
                        translate(0, 0)
                        rotate(0deg)
                        scale(1);
                }

                50% {
                    transform:
                        translate(-18px, 22px)
                        rotate(10deg)
                        scale(1.08);
                }
            }

            @keyframes floatOrbTwo {
                0%,
                100% {
                    transform:
                        translateY(0)
                        scale(1);
                }

                50% {
                    transform:
                        translateY(-24px)
                        scale(1.12);
                }
            }

            @keyframes smallOrbFloat {
                0%,
                100% {
                    transform:
                        translate(0, 0);
                }

                50% {
                    transform:
                        translate(12px, -15px);
                }
            }

            .analytics-line {
                position: absolute;
                right: 7%;
                bottom: 24%;

                width: 210px;
                height: 80px;

                opacity: 0.45;
                transform: skewY(-8deg);

                border-bottom: 2px solid
                    rgba(74, 222, 128, 0.55);

                animation: graphFloat 5s
                    ease-in-out infinite;
            }

            .analytics-line::before,
            .analytics-line::after {
                content: "";
                position: absolute;

                width: 9px;
                height: 9px;

                border-radius: 50%;
                background: #4ade80;

                box-shadow:
                    0 0 14px rgba(74, 222, 128, 0.8);
            }

            .analytics-line::before {
                left: 15%;
                bottom: -5px;
            }

            .analytics-line::after {
                right: 12%;
                bottom: 28px;
            }

            @keyframes graphFloat {
                0%,
                100% {
                    transform:
                        translateY(0)
                        skewY(-8deg);
                }

                50% {
                    transform:
                        translateY(-9px)
                        skewY(-8deg);
                }
            }

            /* ---------------------------------------------
               Section Headings
            --------------------------------------------- */

            .section-title {
                position: relative;
                display: inline-block;

                margin-top: 1.1rem;
                margin-bottom: 1rem;

                font-size: 1.4rem;
                font-weight: 750;

                animation: sectionReveal 0.6s ease both;
            }

            .section-title::after {
                content: "";
                position: absolute;
                left: 0;
                bottom: -7px;

                width: 45%;
                height: 3px;

                border-radius: 20px;

                background:
                    linear-gradient(
                        90deg,
                        #22c55e,
                        transparent
                    );

                animation: underlineExpand 0.9s ease both;
            }

            @keyframes sectionReveal {
                from {
                    opacity: 0;
                    transform: translateX(-15px);
                }

                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            @keyframes underlineExpand {
                from {
                    width: 0;
                }

                to {
                    width: 45%;
                }
            }

            /* ---------------------------------------------
               Animated KPI Cards
            --------------------------------------------- */

            div[data-testid="stMetric"] {
                position: relative;
                overflow: hidden;

                min-height: 125px;
                padding: 1.15rem;

                border: 1px solid var(--card-border);
                border-radius: 16px;

                background:
                    linear-gradient(
                        145deg,
                        rgba(255, 255, 255, 0.96),
                        rgba(240, 253, 244, 0.92)
                    );

                box-shadow:
                    0 8px 26px rgba(15, 23, 42, 0.06);

                animation: metricEntrance 0.65s
                    cubic-bezier(0.22, 1, 0.36, 1) both;

                transition:
                    transform 0.3s ease,
                    box-shadow 0.3s ease,
                    border-color 0.3s ease;
            }

            div[data-testid="stMetric"]::before {
                content: "";
                position: absolute;
                left: 0;
                top: 0;

                width: 4px;
                height: 100%;

                background:
                    linear-gradient(
                        #4ade80,
                        #16a34a
                    );

                transform: scaleY(0);
                transform-origin: bottom;

                transition: transform 0.35s ease;
            }

            div[data-testid="stMetric"]::after {
                content: "";
                position: absolute;
                top: -45px;
                right: -45px;

                width: 100px;
                height: 100px;

                border-radius: 50%;
                background: rgba(34, 197, 94, 0.08);

                transition:
                    transform 0.4s ease,
                    background 0.4s ease;
            }

            div[data-testid="stMetric"]:hover {
                transform: translateY(-7px);
                border-color: rgba(34, 197, 94, 0.55);

                box-shadow:
                    0 18px 40px rgba(22, 163, 74, 0.14);
            }

            div[data-testid="stMetric"]:hover::before {
                transform: scaleY(1);
            }

            div[data-testid="stMetric"]:hover::after {
                transform: scale(1.35);
                background: rgba(34, 197, 94, 0.13);
            }

            div[data-testid="stMetricValue"] {
                position: relative;
                z-index: 2;

                font-weight: 800;

                animation: valueGlow 2.8s
                    ease-in-out infinite;
            }

            @keyframes metricEntrance {
                from {
                    opacity: 0;
                    transform:
                        translateY(22px)
                        scale(0.96);
                }

                to {
                    opacity: 1;
                    transform:
                        translateY(0)
                        scale(1);
                }
            }

            @keyframes valueGlow {
                0%,
                100% {
                    filter: brightness(1);
                }

                50% {
                    filter: brightness(1.12);
                }
            }

            /* ---------------------------------------------
               Plotly Chart Animation
            --------------------------------------------- */

            div[data-testid="stPlotlyChart"] {
                overflow: hidden;

                border: 1px solid rgba(34, 197, 94, 0.12);
                border-radius: 17px;

                background: #ffffff;

                box-shadow:
                    0 8px 28px rgba(15, 23, 42, 0.05);

                animation: chartReveal 0.8s
                    cubic-bezier(0.22, 1, 0.36, 1) both;

                transition:
                    transform 0.3s ease,
                    box-shadow 0.3s ease,
                    border-color 0.3s ease;
            }

            div[data-testid="stPlotlyChart"]:hover {
                transform: translateY(-4px);
                border-color: rgba(34, 197, 94, 0.3);

                box-shadow:
                    0 16px 38px rgba(15, 23, 42, 0.1);
            }

            @keyframes chartReveal {
                from {
                    opacity: 0;
                    transform:
                        translateY(28px)
                        scale(0.98);
                }

                to {
                    opacity: 1;
                    transform:
                        translateY(0)
                        scale(1);
                }
            }

            /* ---------------------------------------------
               Tabs Animation
            --------------------------------------------- */

            button[data-baseweb="tab"] {
                border-radius: 10px 10px 0 0;

                transition:
                    color 0.25s ease,
                    background 0.25s ease,
                    transform 0.25s ease;
            }

            button[data-baseweb="tab"]:hover {
                color: #16a34a;
                background: rgba(34, 197, 94, 0.07);

                transform: translateY(-2px);
            }

            button[data-baseweb="tab"][aria-selected="true"] {
                color: #15803d;
                font-weight: 700;

                background: rgba(34, 197, 94, 0.1);
            }

            /* ---------------------------------------------
               Insight Cards
            --------------------------------------------- */

            .insight-card {
                position: relative;
                overflow: hidden;

                padding: 1rem 1.1rem;
                margin-bottom: 0.8rem;

                border: 1px solid rgba(34, 197, 94, 0.18);
                border-radius: 14px;

                background:
                    linear-gradient(
                        135deg,
                        rgba(240, 253, 244, 0.9),
                        rgba(255, 255, 255, 0.98)
                    );

                animation: insightEntrance 0.65s ease both;

                transition:
                    transform 0.25s ease,
                    border-color 0.25s ease;
            }

            .insight-card:hover {
                transform:
                    translateX(7px)
                    scale(1.01);

                border-color: rgba(34, 197, 94, 0.48);
            }

            .insight-card::after {
                content: "";
                position: absolute;
                right: -35px;
                bottom: -35px;

                width: 75px;
                height: 75px;

                border-radius: 50%;
                background: rgba(34, 197, 94, 0.09);
            }

            .insight-label {
                color: #64748b;

                font-size: 0.76rem;
                font-weight: 700;
                letter-spacing: 0.05rem;
                text-transform: uppercase;
            }

            .insight-value {
                position: relative;
                z-index: 2;

                margin-top: 0.3rem;

                color: #14281d;
                font-size: 1.15rem;
                font-weight: 800;
            }

            @keyframes insightEntrance {
                from {
                    opacity: 0;
                    transform: translateX(18px);
                }

                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            /* ---------------------------------------------
               Sidebar Transition
            --------------------------------------------- */

            section[data-testid="stSidebar"] {
                animation: sidebarEntrance 0.75s
                    cubic-bezier(0.22, 1, 0.36, 1) both;
            }

            @keyframes sidebarEntrance {
                from {
                    opacity: 0;
                    transform: translateX(-24px);
                }

                to {
                    opacity: 1;
                    transform: translateX(0);
                }
            }

            /* ---------------------------------------------
               Buttons
            --------------------------------------------- */

            div.stDownloadButton > button,
            div.stButton > button {
                position: relative;
                overflow: hidden;

                border-radius: 10px;

                transition:
                    transform 0.25s ease,
                    box-shadow 0.25s ease;
            }

            div.stDownloadButton > button:hover,
            div.stButton > button:hover {
                transform: translateY(-3px);

                box-shadow:
                    0 10px 25px rgba(22, 163, 74, 0.18);
            }

            /* ---------------------------------------------
               Dataframe Transition
            --------------------------------------------- */

            div[data-testid="stDataFrame"] {
                animation: tableReveal 0.75s ease both;
            }

            @keyframes tableReveal {
                from {
                    opacity: 0;
                    transform: translateY(18px);
                }

                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }

            /* ---------------------------------------------
               Accessibility
            --------------------------------------------- */

            @media (
                prefers-reduced-motion: reduce
            ) {
                *,
                *::before,
                *::after {
                    animation-duration: 0.01ms !important;
                    animation-iteration-count: 1 !important;
                    transition-duration: 0.01ms !important;
                    scroll-behavior: auto !important;
                }
            }

            footer {
                visibility: hidden;
            }
        </style>
        """
    ),
    unsafe_allow_html=True,
)


# ---------------------------------------------------------
# Data Loading
# ---------------------------------------------------------

@st.cache_data
def load_data(file_path: Path) -> pd.DataFrame:
    """Load and prepare the cleaned ecommerce dataset."""

    if not file_path.exists():
        raise FileNotFoundError(
            f"Cleaned dataset was not found: {file_path}"
        )

    dataframe = pd.read_csv(
        file_path,
        parse_dates=["OrderDate"],
    )

    dataframe["YearMonth"] = (
        dataframe["OrderDate"]
        .dt.to_period("M")
        .astype(str)
    )

    return dataframe


def format_currency(value: float) -> str:
    """Format numeric values as Pakistani rupees."""

    return f"PKR {value:,.0f}"


def get_delivered_orders(
    dataframe: pd.DataFrame,
) -> pd.DataFrame:
    """Return successfully delivered orders."""

    return dataframe[
        dataframe["OrderStatus"] == "Delivered"
    ].copy()


def calculate_top_performer(
    dataframe: pd.DataFrame,
    column: str,
) -> str:
    """Return the highest-performing value by revenue."""

    if dataframe.empty:
        return "No data"

    result = (
        dataframe
        .groupby(
            column,
            as_index=False,
        )
        .agg(
            NetSales=("NetSales", "sum")
        )
        .sort_values(
            "NetSales",
            ascending=False,
        )
    )

    return str(result.iloc[0][column])


def dataframe_to_csv(
    dataframe: pd.DataFrame,
) -> bytes:
    """Convert a DataFrame into downloadable CSV data."""

    return dataframe.to_csv(
        index=False,
    ).encode("utf-8")


try:
    sales_data = load_data(DATA_PATH)

except FileNotFoundError as error:
    st.error(str(error))

    st.info(
        "Run `python src/data_cleaning.py` before "
        "starting the dashboard."
    )

    st.stop()


# ---------------------------------------------------------
# Sidebar Filters
# ---------------------------------------------------------

st.sidebar.title("Dashboard Filters")

st.sidebar.caption(
    "Use the filters below to explore the sales dataset."
)


minimum_date = sales_data["OrderDate"].min().date()
maximum_date = sales_data["OrderDate"].max().date()


selected_date_range = st.sidebar.date_input(
    "Order date range",
    value=(minimum_date, maximum_date),
    min_value=minimum_date,
    max_value=maximum_date,
)


available_categories = sorted(
    sales_data["Category"]
    .dropna()
    .unique()
    .tolist()
)

selected_categories = st.sidebar.multiselect(
    "Product categories",
    options=available_categories,
    default=available_categories,
)


available_cities = sorted(
    sales_data["City"]
    .dropna()
    .unique()
    .tolist()
)

selected_cities = st.sidebar.multiselect(
    "Cities",
    options=available_cities,
    default=available_cities,
)


available_payment_methods = sorted(
    sales_data["PaymentMethod"]
    .dropna()
    .unique()
    .tolist()
)

selected_payment_methods = st.sidebar.multiselect(
    "Payment methods",
    options=available_payment_methods,
    default=available_payment_methods,
)


available_order_statuses = sorted(
    sales_data["OrderStatus"]
    .dropna()
    .unique()
    .tolist()
)

selected_order_statuses = st.sidebar.multiselect(
    "Order statuses",
    options=available_order_statuses,
    default=available_order_statuses,
)


# ---------------------------------------------------------
# Apply Filters
# ---------------------------------------------------------

filtered_data = sales_data.copy()


if isinstance(selected_date_range, tuple):
    start_date, end_date = selected_date_range
else:
    start_date = selected_date_range
    end_date = selected_date_range


filtered_data = filtered_data[
    (
        filtered_data["OrderDate"].dt.date
        >= start_date
    )
    & (
        filtered_data["OrderDate"].dt.date
        <= end_date
    )
]


filtered_data = filtered_data[
    filtered_data["Category"].isin(
        selected_categories
    )
]


filtered_data = filtered_data[
    filtered_data["City"].isin(
        selected_cities
    )
]


filtered_data = filtered_data[
    filtered_data["PaymentMethod"].isin(
        selected_payment_methods
    )
]


filtered_data = filtered_data[
    filtered_data["OrderStatus"].isin(
        selected_order_statuses
    )
]


if filtered_data.empty:
    st.warning(
        "No records match the selected filters. "
        "Change one or more sidebar filters."
    )

    st.stop()


delivered_data = get_delivered_orders(
    filtered_data
)


# ---------------------------------------------------------
# Dashboard Header
# ---------------------------------------------------------

 # ---------------------------------------------------------
# Animated Dashboard Header
# ---------------------------------------------------------

 # ---------------------------------------------------------
# Animated Dashboard Header
# ---------------------------------------------------------

st.html(
    dedent(
        """
        <div class="dashboard-header">
            <div class="motion-layer">
                <span class="motion-orb orb-one"></span>
                <span class="motion-orb orb-two"></span>
                <span class="motion-orb orb-three"></span>
                <span class="analytics-line"></span>
            </div>
            <div class="header-content">
                <div class="dashboard-eyebrow">
                    <span class="live-indicator"></span>
                    Live Business Intelligence
                </div>
                <div class="dashboard-title">
                    E-commerce <span>Sales Analytics</span>
                </div>
                <div class="dashboard-subtitle">
                    Monitor revenue, customer activity, product performance
                    and order trends through an interactive analytics workspace.
                </div>
            </div>
        </div>
        """
    )
)

# ---------------------------------------------------------
# KPI Calculations
# ---------------------------------------------------------

total_orders = filtered_data[
    "OrderID"
].nunique()

delivered_orders = delivered_data[
    "OrderID"
].nunique()

total_customers = filtered_data[
    "CustomerID"
].nunique()

total_revenue = delivered_data[
    "NetSales"
].sum()

total_discount = delivered_data[
    "DiscountAmount"
].sum()

average_order_value = (
    total_revenue / delivered_orders
    if delivered_orders > 0
    else 0
)

delivery_rate = (
    delivered_orders / total_orders * 100
    if total_orders > 0
    else 0
)


# ---------------------------------------------------------
# KPI Cards
# ---------------------------------------------------------

st.markdown(
    '<div class="section-title">Business Overview</div>',
    unsafe_allow_html=True,
)


kpi_column_1, kpi_column_2, kpi_column_3 = (
    st.columns(3)
)

kpi_column_4, kpi_column_5, kpi_column_6 = (
    st.columns(3)
)


with kpi_column_1:
    st.metric(
        label="Total Revenue",
        value=format_currency(total_revenue),
        border=True,
    )


with kpi_column_2:
    st.metric(
        label="Total Orders",
        value=f"{total_orders:,}",
        border=True,
    )


with kpi_column_3:
    st.metric(
        label="Delivered Orders",
        value=f"{delivered_orders:,}",
        border=True,
    )


with kpi_column_4:
    st.metric(
        label="Total Customers",
        value=f"{total_customers:,}",
        border=True,
    )


with kpi_column_5:
    st.metric(
        label="Average Order Value",
        value=format_currency(
            average_order_value
        ),
        border=True,
    )


with kpi_column_6:
    st.metric(
        label="Delivery Rate",
        value=f"{delivery_rate:.1f}%",
        border=True,
    )


# ---------------------------------------------------------
# Prepare Analysis Tables
# ---------------------------------------------------------

monthly_sales = (
    delivered_data
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


category_sales = (
    delivered_data
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
        "NetSales",
        ascending=False,
    )
)


product_sales = (
    delivered_data
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
        "NetSales",
        ascending=False,
    )
)


city_sales = (
    delivered_data
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
        "NetSales",
        ascending=False,
    )
)


order_status_summary = (
    filtered_data
    .groupby(
        "OrderStatus",
        as_index=False,
    )
    .agg(
        Orders=("OrderID", "nunique"),
        OrderValue=("NetSales", "sum"),
    )
    .sort_values(
        "Orders",
        ascending=False,
    )
)


payment_summary = (
    delivered_data
    .groupby(
        "PaymentMethod",
        as_index=False,
    )
    .agg(
        Orders=("OrderID", "nunique"),
        NetSales=("NetSales", "sum"),
    )
    .sort_values(
        "NetSales",
        ascending=False,
    )
)


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
    delivered_data
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


# ---------------------------------------------------------
# Overview Tab
# ---------------------------------------------------------

overview_tab, products_tab, customers_tab, data_tab = (
    st.tabs(
        [
            "Sales Overview",
            "Product Analysis",
            "Customers and Orders",
            "Dataset",
        ]
    )
)


with overview_tab:
    chart_column_1, chart_column_2 = st.columns(
        [1.7, 1]
    )

    with chart_column_1:
        monthly_figure = px.line(
            monthly_sales,
            x="YearMonth",
            y="NetSales",
            markers=True,
            title="Monthly Revenue Trend",
            labels={
                "YearMonth": "Month",
                "NetSales": "Net Revenue",
            },
            color_discrete_sequence=[
                "#22c55e"
            ],
        )

        monthly_figure.update_traces(
            line_width=3,
            marker_size=8,
        )

        monthly_figure.update_layout(
            template="plotly_white",
            hovermode="x unified",
            height=430,
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20,
            ),
            yaxis_tickprefix="PKR ",
        )

        st.plotly_chart(
            monthly_figure,
            width="stretch",
            config={
                "displaylogo": False
            },
        )

    with chart_column_2:
        status_figure = px.pie(
            order_status_summary,
            names="OrderStatus",
            values="Orders",
            hole=0.58,
            title="Order Status Distribution",
            color_discrete_sequence=(
                px.colors.qualitative.Safe
            ),
        )

        status_figure.update_traces(
            textposition="inside",
            textinfo="percent+label",
        )

        status_figure.update_layout(
            template="plotly_white",
            height=430,
            margin=dict(
                l=20,
                r=20,
                t=60,
                b=20,
            ),
            showlegend=False,
        )

        st.plotly_chart(
            status_figure,
            width="stretch",
            config={
                "displaylogo": False
            },
        )

    lower_column_1, lower_column_2 = st.columns(2)

    with lower_column_1:
        category_figure = px.bar(
            category_sales,
            x="Category",
            y="NetSales",
            title="Revenue by Product Category",
            labels={
                "Category": "Category",
                "NetSales": "Net Revenue",
            },
            text_auto=".3s",
            color="NetSales",
            color_continuous_scale="Greens",
        )

        category_figure.update_layout(
            template="plotly_white",
            height=430,
            showlegend=False,
            coloraxis_showscale=False,
            yaxis_tickprefix="PKR ",
        )

        st.plotly_chart(
            category_figure,
            width="stretch",
            config={
                "displaylogo": False
            },
        )

    with lower_column_2:
        payment_figure = px.bar(
            payment_summary,
            x="PaymentMethod",
            y="NetSales",
            title="Revenue by Payment Method",
            labels={
                "PaymentMethod": "Payment Method",
                "NetSales": "Net Revenue",
            },
            hover_data=["Orders"],
            color_discrete_sequence=[
                "#16a34a"
            ],
        )

        payment_figure.update_layout(
            template="plotly_white",
            height=430,
            yaxis_tickprefix="PKR ",
        )

        st.plotly_chart(
            payment_figure,
            width="stretch",
            config={
                "displaylogo": False
            },
        )

    weekday_figure = px.line(
        weekday_sales,
        x="DayName",
        y="NetSales",
        markers=True,
        title="Revenue by Day of the Week",
        labels={
            "DayName": "Day",
            "NetSales": "Net Revenue",
        },
        hover_data=["Orders"],
        color_discrete_sequence=[
            "#22c55e"
        ],
    )

    weekday_figure.update_traces(
        line_width=3,
        marker_size=9,
    )

    weekday_figure.update_layout(
        template="plotly_white",
        height=420,
        yaxis_tickprefix="PKR ",
    )

    st.plotly_chart(
        weekday_figure,
        width="stretch",
        config={
            "displaylogo": False
        },
    )


# ---------------------------------------------------------
# Product Analysis Tab
# ---------------------------------------------------------

with products_tab:
    product_column_1, product_column_2 = (
        st.columns([1.6, 1])
    )

    with product_column_1:
        top_products = (
            product_sales
            .head(10)
            .sort_values("NetSales")
        )

        product_figure = px.bar(
            top_products,
            x="NetSales",
            y="Product",
            orientation="h",
            title="Top 10 Products by Revenue",
            labels={
                "NetSales": "Net Revenue",
                "Product": "Product",
            },
            hover_data=[
                "Category",
                "QuantitySold",
                "Orders",
            ],
            color="NetSales",
            color_continuous_scale="Greens",
        )

        product_figure.update_layout(
            template="plotly_white",
            height=550,
            coloraxis_showscale=False,
            xaxis_tickprefix="PKR ",
        )

        st.plotly_chart(
            product_figure,
            width="stretch",
            config={
                "displaylogo": False
            },
        )

    with product_column_2:
        top_product = calculate_top_performer(
            delivered_data,
            "Product",
        )

        top_category = calculate_top_performer(
            delivered_data,
            "Category",
        )

        st.markdown(
            """
            <div class="section-title">
                Product Insights
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-label">
                    Top Product
                </div>
                <div class="insight-value">
                    {top_product}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-label">
                    Top Category
                </div>
                <div class="insight-value">
                    {top_category}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div class="insight-card">
                <div class="insight-label">
                    Delivered-order Discount
                </div>
                <div class="insight-value">
                    {format_currency(total_discount)}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.dataframe(
            product_sales.head(10),
            use_container_width=True,
            hide_index=True,
        )


# ---------------------------------------------------------
# Customer and Order Analysis Tab
# ---------------------------------------------------------

with customers_tab:
    city_column, status_column = st.columns(2)

    with city_column:
        top_cities = city_sales.head(10)

        city_figure = px.bar(
            top_cities,
            x="City",
            y="NetSales",
            title="Top Cities by Revenue",
            labels={
                "City": "City",
                "NetSales": "Net Revenue",
            },
            hover_data=[
                "Orders",
                "Customers",
            ],
            color="NetSales",
            color_continuous_scale="Greens",
        )

        city_figure.update_layout(
            template="plotly_white",
            height=450,
            coloraxis_showscale=False,
            yaxis_tickprefix="PKR ",
        )

        st.plotly_chart(
            city_figure,
            width="stretch",
            config={
                "displaylogo": False
            },
        )

    with status_column:
        status_value_figure = px.bar(
            order_status_summary,
            x="OrderStatus",
            y="OrderValue",
            title="Order Value by Status",
            labels={
                "OrderStatus": "Order Status",
                "OrderValue": "Order Value",
            },
            color="OrderValue",
            color_continuous_scale="Greens",
        )

        status_value_figure.update_layout(
            template="plotly_white",
            height=450,
            coloraxis_showscale=False,
            yaxis_tickprefix="PKR ",
        )

        st.plotly_chart(
            status_value_figure,
            width="stretch",
            config={
                "displaylogo": False
            },
        )

    top_city = calculate_top_performer(
        delivered_data,
        "City",
    )

    st.success(
        f"The highest-revenue city for the selected "
        f"filters is **{top_city}**."
    )

    st.dataframe(
        city_sales,
        use_container_width=True,
        hide_index=True,
    )


# ---------------------------------------------------------
# Dataset Tab
# ---------------------------------------------------------

with data_tab:
    st.subheader("Filtered Dataset")

    st.caption(
        f"Showing {len(filtered_data):,} records "
        f"after applying the selected filters."
    )

    display_columns = [
        "OrderID",
        "OrderDate",
        "CustomerID",
        "CustomerName",
        "City",
        "Category",
        "Product",
        "Quantity",
        "UnitPrice",
        "DiscountPercentage",
        "NetSales",
        "PaymentMethod",
        "OrderStatus",
    ]

    st.dataframe(
        filtered_data[display_columns],
        use_container_width=True,
        hide_index=True,
        height=520,
    )

    st.download_button(
        label="Download Filtered Data",
        data=dataframe_to_csv(filtered_data),
        file_name="filtered_ecommerce_sales.csv",
        mime="text/csv",
        width="stretch",
    )


# ---------------------------------------------------------
# Sidebar Information
# ---------------------------------------------------------

st.sidebar.divider()

st.sidebar.subheader("Current Selection")

st.sidebar.write(
    f"**Records:** {len(filtered_data):,}"
)

st.sidebar.write(
    f"**Orders:** {total_orders:,}"
)

st.sidebar.write(
    f"**Delivered:** {delivered_orders:,}"
)

st.sidebar.write(
    f"**Revenue:** {format_currency(total_revenue)}"
)

st.sidebar.divider()

st.sidebar.caption(
    "Developed with Python, Pandas, "
    "Plotly and Streamlit."
)