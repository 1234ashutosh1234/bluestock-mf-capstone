import streamlit as st
import pandas as pd

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.sidebar.title("Navigation")

st.sidebar.info("""
Bluestock MF Analytics

Author:
Ashutosh Raj

Technology:
Python
Pandas
SQLite
Streamlit
MFAPI
""")


st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

# -----------------------------------
# LOAD DATA
# -----------------------------------

df = pd.read_csv("data/processed/dashboard_summary_final.csv")


# Remove invalid rows
dashboard_df = df.dropna(subset=["return_pct"])

# -----------------------------------
# TITLE
# -----------------------------------

st.title("📈 Mutual Fund Analytics Dashboard")

st.markdown("""
### Real Mutual Fund Analytics using MFAPI Data

This dashboard analyzes real NAV data fetched from mfapi.in.

---
""")

# -----------------------------------
# KPI SECTION
# -----------------------------------

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Funds",
    len(df)
)

col2.metric(
    "Best Return %",
    round(df["return_pct"].max(), 2)
)

col3.metric(
    "Best Sharpe Ratio",
    round(df["sharpe_ratio"].max(), 2)
)

st.markdown("---")

# -----------------------------------
# FUND TABLE
# -----------------------------------

st.subheader("📋 Fund Performance Table")

st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------------
# TOP FUND
# -----------------------------------

st.markdown("---")

st.subheader("🏆 Top Performing Fund")

best = df.loc[
    df["return_pct"].idxmax()
]

col1, col2 = st.columns(2)

with col1:
    st.success(
    f"🏆 {best['scheme_name']}"
)

with col2:
    st.info(
    f"Return: {best['return_pct']:.2f}%"
)

# -----------------------------------
# RETURN CHART
# -----------------------------------

st.markdown("---")

st.subheader("📈 Return Comparison")

chart_df = df.sort_values(
    "return_pct",
    ascending=False
)

st.bar_chart(
    chart_df.set_index(
        "scheme_name"
    )["return_pct"]
)

# -----------------------------------
# SHARPE CHART
# -----------------------------------

st.markdown("---")

st.subheader("📊 Sharpe Ratio Comparison")

sharpe_df = df.dropna(
    subset=["sharpe_ratio"]
)

st.bar_chart(
    sharpe_df.set_index(
        "scheme_name"
    )["sharpe_ratio"]
)

# -----------------------------------
# RISK TABLE
# -----------------------------------

st.markdown("---")

st.subheader("⚠ Risk Analysis")

risk_df = df[
    [
        "scheme_name",
        "volatility",
        "sharpe_ratio"
    ]
]

st.dataframe(
    risk_df,
    use_container_width=True
)

# -----------------------------------
# FOOTER
# -----------------------------------
st.markdown("---")

st.markdown(
"""
© 2026 Ashutosh Raj

Bluestock Mutual Fund Analytics Capstone Project
"""
)