<div align="center">

<img
  src="https://capsule-render.vercel.app/api?type=waving&color=0:052e16,50:16a34a,100:4ade80&height=240&section=header&text=E-commerce%20Sales%20Analytics&fontSize=43&fontColor=ffffff&fontAlignY=38&desc=From%20Raw%20Data%20to%20Actionable%20Business%20Insights&descAlignY=58&animation=fadeIn"
  width="100%"
  alt="E-commerce Sales Analytics"
/>

<img
  src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=21&duration=2800&pause=800&color=22C55E&center=true&vCenter=true&width=850&lines=Clean+Data.+Clear+Insights.+Better+Decisions.;Interactive+Dashboard+Built+with+Python+and+Streamlit.;Data+Cleaning+%7C+EDA+%7C+Business+Intelligence"
  alt="Typing Animation"
/>

<br>

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/python/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-16A34A?style=for-the-badge)](LICENSE)

<br>

**An end-to-end e-commerce analytics project that transforms raw sales records into an interactive business intelligence dashboard.**

[Repository](https://github.com/MuhammadHamzaDS/Ecommerce-Sales-Analytics)
&nbsp;•&nbsp;
[Report an Issue](https://github.com/MuhammadHamzaDS/Ecommerce-Sales-Analytics/issues)
&nbsp;•&nbsp;
[GitHub Profile](https://github.com/MuhammadHamzaDS)

</div>

---

## Project Preview

<div align="center">

<img
  src="assets/dashboard-preview.png"
  width="95%"
  alt="E-commerce Sales Analytics Dashboard Preview"
/>

</div>

---

## About the Project

**E-commerce Sales Analytics** is a complete Python data analytics project designed to demonstrate how raw transactional data can be:

- Generated
- Validated
- Cleaned
- Transformed
- Analyzed
- Visualized
- Presented through an interactive dashboard

The dashboard provides meaningful insights into revenue, orders, customers, products, categories, payment methods and city-level performance.

---

## Analytics Workflow

```text
Raw E-commerce Data
        │
        ▼
Data Validation
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
KPI Calculation
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Interactive Visualizations
        │
        ▼
Streamlit Dashboard
```

---

## Core Features

<table>
<tr>
<td width="50%" valign="top">

### Data Cleaning

- Duplicate-record removal
- Missing-value handling
- Data-type conversion
- Invalid-value filtering
- Text standardization
- Date processing
- Clean dataset export

</td>

<td width="50%" valign="top">

### Business Analytics

- Total revenue
- Total orders
- Delivered orders
- Total customers
- Average order value
- Delivery rate
- Total discount
- Top product, category and city

</td>
</tr>

<tr>
<td width="50%" valign="top">

### Interactive Dashboard

- Date-range filter
- Product-category filter
- City filter
- Payment-method filter
- Order-status filter
- Interactive Plotly charts
- Filtered CSV download

</td>

<td width="50%" valign="top">

### Professional Interface

- Animated gradient header
- Smooth entrance transitions
- Motion graphics
- KPI card hover effects
- Responsive dashboard layout
- Tab-based navigation
- Custom Streamlit theme

</td>
</tr>
</table>

---

## Dashboard Modules

### Sales Overview

Provides a complete overview of business performance:

- Monthly revenue trend
- Revenue by category
- Revenue by payment method
- Order-status distribution
- Weekday sales performance
- Revenue and order KPIs

### Product Analysis

Identifies the strongest products and categories:

- Top 10 products by revenue
- Quantity sold
- Number of orders
- Top-performing product
- Top-performing category
- Delivered-order discounts

### Customers and Orders

Analyzes geographic and order performance:

- Revenue by city
- Orders by city
- Customers by city
- Order value by status
- Highest-performing city

### Dataset Explorer

Allows users to inspect and download filtered data:

- Interactive data table
- Filter-aware records
- Selected-column preview
- CSV download functionality

---

## Key Performance Indicators

| KPI | Description |
|---|---|
| **Total Revenue** | Net sales generated from delivered orders |
| **Total Orders** | Number of unique orders |
| **Delivered Orders** | Number of successfully delivered orders |
| **Total Customers** | Number of unique customers |
| **Average Order Value** | Average revenue per delivered order |
| **Delivery Rate** | Percentage of orders successfully delivered |
| **Total Discount** | Discount applied to delivered orders |
| **Top Product** | Product generating the highest revenue |
| **Top Category** | Category generating the highest revenue |
| **Top City** | City generating the highest revenue |

---

## Business Formulas

```text
Gross Sales =
Quantity × Unit Price
```

```text
Discount Amount =
Gross Sales × Discount Percentage ÷ 100
```

```text
Net Sales =
Gross Sales − Discount Amount
```

```text
Average Order Value =
Total Revenue ÷ Delivered Orders
```

```text
Delivery Rate =
Delivered Orders ÷ Total Orders × 100
```

> Revenue is calculated using successfully delivered orders only. Cancelled and returned orders are analyzed separately.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| **Python** | Core programming language |
| **Pandas** | Data cleaning and analysis |
| **NumPy** | Numerical processing |
| **Plotly** | Interactive visualizations |
| **Matplotlib** | Static charts |
| **Streamlit** | Interactive web dashboard |
| **Faker** | Synthetic dataset generation |
| **Jupyter Notebook** | Exploratory analysis |
| **Git and GitHub** | Version control and hosting |

---

## Project Structure

```text
Ecommerce-Sales-Analytics/
│
├── .streamlit/
│   └── config.toml
│
├── assets/
│   ├── dashboard-preview.png
│   ├── sales-overview.png
│   ├── product-analysis.png
│   └── customer-analysis.png
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── ecommerce_sales_raw.csv
│   │
│   └── processed/
│       └── ecommerce_sales_cleaned.csv
│
├── notebooks/
│   └── ecommerce_sales_analysis.ipynb
│
├── reports/
│   ├── analysis/
│   └── charts/
│       ├── static/
│       └── interactive/
│
├── src/
│   ├── generate_dataset.py
│   ├── data_cleaning.py
│   ├── analysis.py
│   └── visualizations.py
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

## Dataset Columns

| Column | Description |
|---|---|
| `OrderID` | Unique order identifier |
| `OrderDate` | Date when the order was placed |
| `CustomerID` | Unique customer identifier |
| `CustomerName` | Customer name |
| `City` | Customer city |
| `Category` | Product category |
| `Product` | Product name |
| `Quantity` | Number of purchased items |
| `UnitPrice` | Price per product unit |
| `DiscountPercentage` | Applied discount |
| `PaymentMethod` | Payment method |
| `OrderStatus` | Current order status |
| `GrossSales` | Sales amount before discount |
| `DiscountAmount` | Total discount amount |
| `NetSales` | Final sales amount |
| `Year` | Order year |
| `MonthNumber` | Numeric month |
| `MonthName` | Month name |
| `YearMonth` | Monthly aggregation key |
| `DayName` | Day of the week |

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/MuhammadHamzaDS/Ecommerce-Sales-Analytics.git
```

### 2. Open the Project Folder

```bash
cd Ecommerce-Sales-Analytics
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS or Linux

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Project

### Generate the Dataset

```bash
python src/generate_dataset.py
```

### Clean the Dataset

```bash
python src/data_cleaning.py
```

### Generate Analysis Reports

```bash
python src/analysis.py
```

### Generate Visualizations

```bash
python src/visualizations.py
```

### Launch the Dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will open automatically in your browser.

---

## Dashboard Screenshots

### Sales Overview

<div align="center">

<img
  src="assets/sales-overview.png"
  width="95%"
  alt="Sales Overview"
/>

</div>

### Product Analysis

<div align="center">

<img
  src="assets/product-analysis.png"
  width="95%"
  alt="Product Analysis"
/>

</div>

### Customer and Order Analysis

<div align="center">

<img
  src="assets/customer-analysis.png"
  width="95%"
  alt="Customer and Order Analysis"
/>

</div>

---

## Generated Reports

The analysis pipeline generates the following reports:

```text
reports/analysis/
├── kpis.csv
├── monthly_sales.csv
├── category_sales.csv
├── top_products.csv
├── city_sales.csv
├── payment_methods.csv
├── order_status.csv
└── weekday_sales.csv
```

The project also generates static PNG and interactive HTML visualizations.

---

## Business Questions Answered

This dashboard helps answer:

- How much revenue was generated?
- Which product generates the highest revenue?
- Which product category performs best?
- Which city generates the highest sales?
- How does revenue change over time?
- Which payment method contributes the most revenue?
- What percentage of orders are delivered?
- Which weekdays generate the highest revenue?
- How much discount was provided?
- How many orders were cancelled or returned?

---

## Roadmap

- [x] Synthetic dataset generation
- [x] Data-cleaning pipeline
- [x] Feature engineering
- [x] KPI calculations
- [x] Exploratory data analysis
- [x] Static visualizations
- [x] Interactive Plotly charts
- [x] Streamlit dashboard
- [x] Animated dashboard interface
- [x] Filtered CSV download
- [ ] Streamlit Cloud deployment
- [ ] Automated PDF report
- [ ] Sales forecasting
- [ ] Customer segmentation
- [ ] Product recommendation system
- [ ] Database integration
- [ ] Docker deployment

---

## Future Improvements

Future versions may include:

- Sales forecasting using time-series models
- Customer segmentation using RFM analysis
- Customer lifetime value analysis
- Inventory demand prediction
- Product recommendation engine
- MySQL or PostgreSQL integration
- User authentication
- Automated PDF reports
- Cloud deployment
- Docker containerization
- Automated testing

---

## Author

<div align="center">

### Muhammad Hamza

**Computer Science Student • Python Developer • Data and AI Enthusiast**

Founder of **Depth First Code**

[![GitHub](https://img.shields.io/badge/GitHub-MuhammadHamzaDS-181717?style=for-the-badge&logo=github)](https://github.com/MuhammadHamzaDS)

[![Project](https://img.shields.io/badge/Project-Ecommerce%20Sales%20Analytics-16A34A?style=for-the-badge&logo=github)](https://github.com/MuhammadHamzaDS/Ecommerce-Sales-Analytics)

</div>

---

## Contributing

Contributions and suggestions are welcome.

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/your-feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new analytics feature"
```

4. Push the branch.

```bash
git push origin feature/your-feature-name
```

5. Open a pull request.

---

## License

This project is available under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

---

## Support the Project

If you found this project useful:

- Star the repository
- Share it with other learners
- Fork it and build your own version
- Submit improvements through GitHub Issues

<div align="center">

<img
  src="https://capsule-render.vercel.app/api?type=waving&color=0:4ade80,50:16a34a,100:052e16&height=150&section=footer&animation=fadeIn"
  width="100%"
  alt="Footer"
/>

### Clean Data. Clear Insights. Better Decisions.

**Built with Python, powered by data, and presented by Depth First Code.**

</div>
