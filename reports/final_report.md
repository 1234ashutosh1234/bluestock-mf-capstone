# Mutual Fund Analytics Capstone Project Report

## Student

Ashutosh Raj

---

## Project Objective

The objective of this project was to build a complete Mutual Fund Analytics platform using real mutual fund data.

The project collects NAV data from mfapi.in, stores it in SQLite, performs performance and risk analysis, and visualizes insights through an interactive Streamlit dashboard.

---

## Data Collection

Real mutual fund NAV data was collected using the mfapi.in API.

Five major mutual funds were analyzed:

1. HDFC Top 100 Fund
2. SBI Bluechip Fund
3. ICICI Prudential Bluechip Fund
4. Nippon India Large Cap Fund
5. Kotak Bluechip Fund

---

## Data Processing

The collected data was:

- Cleaned
- Validated
- Merged
- Stored in SQLite

Total NAV Records:

16253+

---

## Analytics Performed

### Fund Performance

Calculated:

- Start NAV
- End NAV
- Return Percentage

### Risk Analysis

Calculated:

- Volatility
- Sharpe Ratio

---

## Key Findings

### Highest Return Fund

HDFC Top 100 Fund

Return:

1580.12%

---

### Best Sharpe Ratio

HDFC Top 100 Fund

Sharpe Ratio:

1.52

---

## Limitations

The provided NAV dataset contains only three trading days of historical data (01-Jan-2024 to 03-Jan-2024) for the selected mutual funds.

Due to the limited time horizon, long-term performance metrics such as 1-Year, 3-Year, and 5-Year CAGR could not be calculated accurately. Therefore, short-period return calculations and annualized estimates were used where applicable.

If a multi-year NAV dataset is available, the project can be extended to compute true long-term CAGR, rolling returns, advanced risk metrics, and more comprehensive performance analytics.


## Dashboard

A Streamlit dashboard was developed to visualize:

- Fund Performance
- Risk Metrics
- Top Performing Funds
- Ranking Tables
- Comparative Charts

---

## Technologies Used

- Python
- Pandas
- SQLite
- Streamlit
- Matplotlib
- Requests

---

## Conclusion

The project successfully demonstrates the use of Python for financial data analysis, database management, risk analytics, and dashboard development.

The dashboard provides investors with insights into fund performance and risk characteristics using real mutual fund NAV data.

---

## Author

Ashutosh Raj