query = """
SELECT
    amfi_code,
    MIN(CASE WHEN nav > 0 THEN nav END) AS start_nav,
    MAX(nav) AS end_nav
FROM nav_history
GROUP BY amfi_code
"""