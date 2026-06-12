"""
Master Pipeline Script
Runs the complete Mutual Fund Analytics workflow.

Author: Ashutosh Raj
"""

import os

print("Starting Mutual Fund Analytics Pipeline...")

# ETL
os.system("python scripts/data_ingestion.py")

# Analytics
os.system("python scripts/fund_performance.py")
os.system("python scripts/risk_analysis.py")
os.system("python scripts/fund_scorecard.py")

# Advanced Analytics (if files exist)
os.system("python scripts/cagr_analysis.py")
os.system("python scripts/max_drawdown.py")
os.system("python scripts/alpha_beta.py")
os.system("python scripts/sortino_ratio.py")

print("Pipeline Completed Successfully!")