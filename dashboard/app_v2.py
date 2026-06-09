import streamlit as st
import pandas as pd

# ==================================
# PAGE CONFIG
# ==================================

st.set_page_config(
    page_title="Mutual Fund Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

# ==================================
# LOAD DATA
# ==================================

df = pd.read_csv(
    "data/processed/dashboard_summary_final.csv"
)

score_df = pd.read_csv(
    "data/processed/fund_scorecard.csv"
)

# ==================================
# SIDEBAR
# ==================================

st.sidebar.title("📊 Navigation")

page = st.sidebar.radio(
    "Select Page",
    [
        "Overview",
        "Fund Performance",
        "Risk Analysis",
        "Scorecard"
    ]
)

st.sidebar.markdown("---")

st.sidebar.subheader("🔍 Filters")

selected_funds = st.sidebar.multiselect(
    "Choose Mutual Funds",
    options=df["scheme_name"].unique(),
    default=df["scheme_name"].unique()
)

metric_choice = st.sidebar.selectbox(
    "Choose Metric",
    [
        "return_pct",
        "sharpe_ratio",
        "volatility"
    ]
)

filtered_df = df[
    df["scheme_name"].isin(selected_funds)
]

filtered_score = score_df[
    score_df["scheme_name"].isin(selected_funds)
]

st.sidebar.markdown("---")

st.sidebar.info(
"""
Author: Ashutosh Raj

Bluestock MF Analytics Capstone

Technology:

• Python
• Pandas
• SQLite
• Streamlit
• MFAPI
"""
)

# ==================================
# OVERVIEW PAGE
# ==================================

if page == "Overview":

    st.title(
        "📈 Mutual Fund Analytics Dashboard"
    )

    st.markdown(
        "### Real Mutual Fund Analytics using MFAPI Data"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Funds",
        len(filtered_df)
    )

    col2.metric(
        "Best Return %",
        round(
            filtered_df["return_pct"].max(),
            2
        )
    )

    col3.metric(
        "Best Sharpe Ratio",
        round(
            filtered_df["sharpe_ratio"].max(),
            2
        )
    )

    st.markdown("---")

    st.subheader(
        "📋 Fund Performance Table"
    )

    st.dataframe(
        filtered_df,
        use_container_width=True
    )

    csv = filtered_df.to_csv(
        index=False
    )

    st.download_button(
        label="⬇ Download Dataset",
        data=csv,
        file_name="mutual_fund_report.csv",
        mime="text/csv"
    )

# ==================================
# FUND PERFORMANCE PAGE
# ==================================

elif page == "Fund Performance":

    st.title(
        "🏆 Fund Performance"
    )

    best = filtered_df.loc[
        filtered_df["return_pct"].idxmax()
    ]

    st.success(
        f"Top Fund : {best['scheme_name']}"
    )

    st.metric(
        "Return %",
        round(
            best["return_pct"],
            2
        )
    )

    st.markdown("---")

    st.subheader(
        f"{metric_choice} Comparison"
    )

    chart_df = filtered_df.sort_values(
        metric_choice,
        ascending=False
    )

    st.bar_chart(
        chart_df.set_index(
            "scheme_name"
        )[metric_choice]
    )

# ==================================
# RISK ANALYSIS PAGE
# ==================================

elif page == "Risk Analysis":

    st.title(
        "⚠ Risk Analytics"
    )

    risk_df = filtered_df[
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

    st.markdown("---")

    st.subheader(
        "Volatility Comparison"
    )

    st.bar_chart(
        risk_df.set_index(
            "scheme_name"
        )["volatility"]
    )

    st.markdown("---")

    st.subheader(
        "Sharpe Ratio Comparison"
    )

    st.bar_chart(
        risk_df.set_index(
            "scheme_name"
        )["sharpe_ratio"]
    )

# ==================================
# SCORECARD PAGE
# ==================================

elif page == "Scorecard":

    st.title(
        "🥇 Fund Scorecard"
    )

    st.dataframe(
        filtered_score,
        use_container_width=True
    )

    st.markdown("---")

    st.subheader(
        "Fund Ranking"
    )

    st.bar_chart(
        filtered_score.set_index(
            "scheme_name"
        )["score"]
    )

# ==================================
# FOOTER
# ==================================

st.markdown("---")

st.success(
    "Project Completed Successfully"
)

st.caption(
"""
Developed by Ashutosh Raj

Bluestock Mutual Fund Analytics Capstone Project
"""
)