CREATE TABLE nav_history (
    amfi_code INTEGER,
    scheme_name TEXT,
    nav REAL,
    date TEXT
);

CREATE TABLE fund_performance (
    amfi_code INTEGER,
    start_nav REAL,
    end_nav REAL,
    return_pct REAL
);

CREATE TABLE risk_analysis (
    amfi_code INTEGER,
    volatility REAL,
    sharpe_ratio REAL
);