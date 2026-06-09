# Mutual Fund Analytics Capstone Project

## Overview


## Dashboard Preview

![Dashboard]![Dashboard](dashboard/dashboard.png)

### Live Dashboard Features

- Fund Performance Analysis
- Return Comparison
- Sharpe Ratio Analysis
- Risk Analysis
- Real MFAPI Data Integration

## Features

- Real Mutual Fund NAV Data Integration
- Data Cleaning and Processing
- SQLite Database Storage
- SQL Analytics
- Fund Performance Analysis
- Risk Analysis
- Sharpe Ratio Calculation
- Interactive Streamlit Dashboard
- Performance Visualization


## Bonus Challenges Completed

### B1 - Auto ETL Scheduler
Automated daily NAV update and analytics pipeline execution.

### B2 - Streamlit Dashboard
Interactive Mutual Fund Analytics Dashboard.

### B3 - Monte Carlo Simulation
5-year NAV forecasting using Monte Carlo simulations.

### B4 - Markowitz Portfolio Optimization
Optimal portfolio allocation using Modern Portfolio Theory.

### B5 - Automated Email Reporting
Automated email generation and delivery of mutual fund reports.

## Technology Stack

- Python
- Pandas
- SQLite
- Streamlit
- Matplotlib
- MFAPI

## Scripts Overview

### ETL

* data_ingestion.py
* live_nav_fetch.py

### Database

* create_database.py
* sql_analysis.py

### Analytics

* fund_performance.py
* risk_analysis.py
* cagr_analysis.py
* alpha_beta.py
* sortino_ratio.py
* max_drawdown.py
* fund_scorecard.py

### Visualization

* nav_trend.py
* correlation_matrix.py

### Dashboard

* dashboard_summary.py
* enrich_dashboard.py

### Bonus Challenges

* auto_etl.py
* monte_carlo.py
* portfolio_optimizer.py
* email_report.py


## Project Structure

## How To Run

### Install Dependencies

pip install -r requirements.txt

### Run Dashboard

streamlit run dashboard/app.py

## Author

Ashutosh Raj