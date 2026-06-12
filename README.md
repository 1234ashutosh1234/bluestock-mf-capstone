# Mutual Fund Analytics Capstone Project

## Overview

## 📂 Project Resources

[![Source Code](https://img.shields.io/badge/Source%20Code-GitHub-blue)](https://github.com/1234ashutosh1234/bluestock-mf-capstone)

[![Datasets](https://img.shields.io/badge/Datasets-Google%20Drive-green)](https://drive.google.com/drive/folders/13iZHSjm7H1vCpN3B8zAB4bqRGj51O9w5?usp=drive_link)

[![Documentation](https://img.shields.io/badge/Documentation-Google%20Drive-orange)](https://drive.google.com/drive/folders/1InESRrD7woPMrbI_kTpErgK3iqM1mA4p?usp=drive_link)

[![PPT Slides](https://img.shields.io/badge/PPT%20Slides-Google%20Drive-purple)](https://drive.google.com/drive/folders/1TyfAUtlAbOtUlAt9xsr6rdKuM71LH4WV?usp=drive_link)

[![Demo Video](https://img.shields.io/badge/Demo%20Video-Google%20Drive-red)](https://drive.google.com/drive/folders/1gC8kzzkrs_uzjhgPcdc-8ayYm9GsJJOC?usp=drive_link)

## Dashboard Preview

![Dashboard](dashboard/dashboard.png)

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

## Run Complete Project

Execute the entire analytics pipeline:

```bash
python scripts/run_pipeline.py
```

This script runs:

* Data Ingestion
* Fund Performance Analysis
* Risk Analysis
* Fund Scorecard
* CAGR Analysis
* Alpha-Beta Analysis
* Sortino Ratio Analysis
* Max Drawdown Analysis



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

## Limitations & Assumptions

### Dataset Limitation

The NAV dataset provided for this project contains only a limited number of trading days for the selected mutual funds. As a result, long-term performance metrics such as 1-Year, 3-Year, and 5-Year CAGR could not be calculated using actual historical data.

### Analytical Assumptions

* Daily returns were calculated using available NAV observations.
* Risk metrics such as Sharpe Ratio, Sortino Ratio, Alpha-Beta, and Maximum Drawdown were computed using the provided dataset.
* CAGR values are demonstrated using the available NAV history and should not be interpreted as actual long-term mutual fund performance.

### Future Enhancements

* Integrate multi-year NAV history (2022–2025 or later).
* Compute true 1Y, 3Y, and 5Y CAGR metrics.
* Add rolling return analysis.
* Add benchmark tracking error analysis.
* Expand dashboard with additional fund comparison features.
* Deploy the dashboard to Streamlit Cloud or Render.

### Project Status

✅ Data Ingestion & ETL
✅ Data Cleaning & Processing
✅ SQLite Database Integration
✅ Exploratory Data Analysis (EDA)
✅ Fund Performance Analytics
✅ Risk Analytics
✅ Interactive Streamlit Dashboard
✅ Dashboard PDF & Screenshots
✅ Documentation & Final Report
✅ Bonus Challenges (Auto ETL, Monte Carlo Simulation, Portfolio Optimization, Email Reporting)



## Project Structure

## How To Run

### Install Dependencies

pip install -r requirements.txt

### Run Dashboard

streamlit run dashboard/app.py

## Author

Ashutosh Raj