import streamlit as st
import pandas as pd

# ------------------------
# PAGE CONFIG
# ------------------------

st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

# ------------------------
# LOAD DATA
# ------------------------

df = pd.read_csv(
    "data/processed/dashboard_summary_final.csv"
)

# Remove invalid rows
df = df.dropna(subset=["return_pct"])

# ------------------------
# TITLE
# ------------------------

st.title("📈 Mutual Fund Analytics Dashboard")

st.markdown("""
### Project Overview

This dashboard analyzes real Mutual Fund NAV data fetched from **mfapi.in**.

Metrics Included:
- Fund Returns (%)
- Volatility
- Sharpe Ratio
- Top Performing Fund
- Risk Analysis

Developed using:
**Python, Pandas, SQLite, Streamlit, Matplotlib**
""")

st.divider()

# ------------------------
# KPI CARDS
# ------------------------

best_fund = df.loc[df["return_pct"].idxmax()]

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Funds",
    len(df)
)

col2.metric(
    "Best Return %",
    f"{df['return_pct'].max():.2f}"
)

col3.metric(
    "Best Sharpe",
    f"{df['sharpe_ratio'].max():.2f}"
)

col4.metric(
    "Top Fund",
    best_fund["scheme_name"]
)

st.divider()

# ------------------------
# DATA TABLE
# ------------------------

st.subheader("📋 Fund Performance Summary")

display_df = df[
    [
        "scheme_name",
        "return_pct",
        "volatility",
        "sharpe_ratio"
    ]
].copy()

display_df.columns = [
    "Fund Name",
    "Return %",
    "Volatility",
    "Sharpe Ratio"
]

st.dataframe(
    display_df,
    use_container_width=True
)

st.divider()

# ------------------------
# TOP FUND
# ------------------------

st.subheader("🏆 Top Performing Fund")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Fund Name",
    best_fund["scheme_name"]
)

col2.metric(
    "Return %",
    f"{best_fund['return_pct']:.2f}"
)

col3.metric(
    "Sharpe Ratio",
    f"{best_fund['sharpe_ratio']:.2f}"
)

st.divider()

# ------------------------
# CHARTS
# ------------------------

col1, col2 = st.columns(2)

with col1:

    st.subheader("📊 Fund Returns (%)")

    chart_df = df.set_index(
        "scheme_name"
    )["return_pct"]

    st.bar_chart(chart_df)

with col2:

    st.subheader("⚖️ Sharpe Ratio")

    chart_df = df.set_index(
        "scheme_name"
    )["sharpe_ratio"]

    st.bar_chart(chart_df)

st.divider()

# ------------------------
# RANKING TABLE
# ------------------------

st.subheader("🥇 Fund Ranking")

ranking = df[
    [
        "scheme_name",
        "return_pct",
        "sharpe_ratio"
    ]
].sort_values(
    by="return_pct",
    ascending=False
)

ranking.columns = [
    "Fund Name",
    "Return %",
    "Sharpe Ratio"
]

st.dataframe(
    ranking,
    use_container_width=True
)

st.divider()

# ------------------------
# FOOTER
# ------------------------

st.markdown("""
---
### Mutual Fund Analytics Capstone Project

Built using:
- Python
- Pandas
- SQLite
- Streamlit
- mfapi.in

Author: Ashutosh Raj
""")