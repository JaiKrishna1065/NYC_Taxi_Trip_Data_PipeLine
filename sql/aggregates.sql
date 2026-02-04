CREATE TABLE agg_daily_summary AS
SELECT
    d.full_date,
    COUNT(*) AS total_trips,
    SUM(f.total_amount) AS total_revenue,
    AVG(f.trip_distance) AS avg_distance
FROM fact_nyc_taxi_data f
JOIN dim_date d
    ON f.date_id = d.date_id
GROUP BY d.full_date;
