SELECT
    amfi_code,
    MAX(nav) AS highest_nav
FROM nav_history
GROUP BY amfi_code;