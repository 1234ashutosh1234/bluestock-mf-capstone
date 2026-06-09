import schedule
import time
import os

def run_pipeline():
    print("Running ETL Pipeline...")
    
    os.system("python scripts/live_nav_fetch.py")
    os.system("python scripts/fund_performance.py")
    os.system("python scripts/risk_analysis.py")
    os.system("python scripts/dashboard_summary.py")

    print("Pipeline Complete")

schedule.every().day.at("20:00").do(run_pipeline)

print("Scheduler Started")

while True:
    schedule.run_pending()
    time.sleep(60)